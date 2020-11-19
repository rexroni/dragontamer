import tkinter
import sys
import time
import threading
import queue
import selectors
import socket

import lut

# Linux event types
EV_SYN = 0
EV_KEY = 1

# EV_SYN codes
SYN_REPORT = 0


def marshal(type, code, value, now):
    # syntax is: type:value:code:sec:usec\n
    sec = int(now)
    usec = int((now - sec) * 1000000)
    return b"%d:%d:%d:%d:%d\n"%(type, code, value, sec, usec)

def is_press(event):
    return event.type in (
        tkinter.EventType.ButtonPress, tkinter.EventType.KeyPress
    )

def is_button(event):
    return event.type in (
        tkinter.EventType.ButtonPress, tkinter.EventType.ButtonRelease
    )

class DragonTamer:
    def __init__(self, q):
        self.q = q

        # prepare the gui
        self.tkroot = tkinter.Tk()
        self.tkroot.bind("<Key>", self.event)
        self.tkroot.bind("<KeyRelease>", self.event)
        self.tkroot.bind("<Button>", self.event)
        self.tkroot.bind("<ButtonRelease>", self.event)

        # prepare the key states
        self.keys_pressed = set()


    def event(self, event):
        # print('event:', event, file=sys.stderr)

        button = is_button(event)

        if is_press(event):
            # filter out key repeats
            if button and event.keysym in self.keys_pressed:
                return
            self.keys_pressed.add(event.keysym)
            code = 1
        else:
            self.keys_pressed.discard(event.keysym)
            code = 0

        if button:
            value = lut.mousevalues[event.num]
        else:
            value = lut.keyvalues[event.keysym]

        now = time.time()

        msg = marshal(EV_KEY, code, value, now) \
                + marshal(EV_SYN, SYN_REPORT, 0, now)

        self.q.put(msg)

    def run(self):
        self.tkroot.mainloop()


class Server(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        self.queue = queue.Queue()

        self.listener = socket.socket()
        # set the magic "reuse addr" bits
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind(("", port))
        self.listener.listen()

        # create a control connection
        self.ctl_w = socket.socket()
        self.ctl_w.connect(("127.0.0.1", self.port))

        # accept the other side of the control connection
        self.ctl_r, _ = self.listener.accept()
        self.ctl_r.setblocking(False)

        self.listener.setblocking(False)

        # configure event loop
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.ctl_r, selectors.EVENT_READ)
        self.sel.register(self.listener, selectors.EVENT_READ)

    def run(self):
        # per-connection loop
        while True:
            # wait for a new connection or a wakeup-and-die message
            events = self.sel.select()
            for key, mask in events:
                # check if this was a wakeup-and-die message
                if key.fileobj == self.ctl_r:
                    return

                # Flush the queue
                for i in range(self.queue.qsize()):
                    if self.queue.get() is None:
                        return

                # accept the next connection
                conn, _ = self.listener.accept()
                with conn:
                    # per-keypress loop
                    while True:
                        # wait for a keypress from the other thread
                        msg = self.queue.get()
                        if msg is None:
                            return
                        try:
                            conn.sendall(msg)
                        except BrokenPipeError:
                            break


    def close(self):
        # To be called from the main thread only

        # Exit the loop if we have a connection.
        self.queue.put(None)

        # Exit the loop if we don't have a connection.
        self.ctl_w.send(b'die!')

        self.join()

        self.sel.unregister(self.ctl_r)
        self.sel.unregister(self.listener)

        self.listener.close()
        self.ctl_w.close()
        self.ctl_r.close()

        self.sel.close()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.close()


def main():
    with Server(12345) as server:
        DragonTamer(server.queue).run()


if __name__ == "__main__":
    main()
