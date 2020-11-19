mousevalues = {
    1: 0x110,  # "BTN_LEFT"
    3: 0x111,  # "BTN_RIGHT"
    2: 0x112,  # "BTN_MIDDLE"
}

keyvalues = {
    "Escape": 1,  # "KEY_ESC"
    "1": 2,  # "KEY_1"
    "2": 3,  # "KEY_2"
    "3": 4,  # "KEY_3"
    "4": 5,  # "KEY_4"
    "5": 6,  # "KEY_5"
    "6": 7,  # "KEY_6"
    "7": 8,  # "KEY_7"
    "8": 9,  # "KEY_8"
    "9": 10,  # "KEY_9"
    "0": 11,  # "KEY_0"
    "minus": 12,  # "KEY_MINUS"
    "equal": 13,  # "KEY_EQUAL"
    "BackSpace": 14,  # "KEY_BACKSPACE"
    "Tab": 15,  # "KEY_TAB"
    "q": 16,  # "KEY_Q"
    "w": 17,  # "KEY_W"
    "e": 18,  # "KEY_E"
    "r": 19,  # "KEY_R"
    "t": 20,  # "KEY_T"
    "y": 21,  # "KEY_Y"
    "u": 22,  # "KEY_U"
    "i": 23,  # "KEY_I"
    "o": 24,  # "KEY_O"
    "p": 25,  # "KEY_P"
    "braceleft": 26,  # "KEY_LEFTBRACE"
    "braceright": 27,  # "KEY_RIGHTBRACE"
    "Return": 28,  # "KEY_ENTER"
    "Control_L": 29,  # "KEY_LEFTCTRL"
    "a": 30,  # "KEY_A"
    "s": 31,  # "KEY_S"
    "d": 32,  # "KEY_D"
    "f": 33,  # "KEY_F"
    "g": 34,  # "KEY_G"
    "h": 35,  # "KEY_H"
    "j": 36,  # "KEY_J"
    "k": 37,  # "KEY_K"
    "l": 38,  # "KEY_L"
    "semicolon": 39,  # "KEY_SEMICOLON"
    "apostrophe": 40,  # "KEY_APOSTROPHE"
    "grave": 41,  # "KEY_GRAVE"
    "Shift_L": 42,  # "KEY_LEFTSHIFT"
    "backslash": 43,  # "KEY_BACKSLASH"
    "z": 44,  # "KEY_Z"
    "x": 45,  # "KEY_X"
    "c": 46,  # "KEY_C"
    "v": 47,  # "KEY_V"
    "b": 48,  # "KEY_B"
    "n": 49,  # "KEY_N"
    "m": 50,  # "KEY_M"
    "comma": 51,  # "KEY_COMMA"
    "period": 52,  # "KEY_DOT"
    "slash": 53,  # "KEY_SLASH"
    "Shift_R": 54,  # "KEY_RIGHTSHIFT"
    "KP_Multiply": 55,  # "KEY_KPASTERISK"
    "Alt_L": 56,  # "KEY_LEFTALT"
    "space": 57,  # "KEY_SPACE"
    "Caps_Lock": 58,  # "KEY_CAPSLOCK"
    "F1": 59,  # "KEY_F1"
    "F2": 60,  # "KEY_F2"
    "F3": 61,  # "KEY_F3"
    "F4": 62,  # "KEY_F4"
    "F5": 63,  # "KEY_F5"
    "F6": 64,  # "KEY_F6"
    "F7": 65,  # "KEY_F7"
    "F8": 66,  # "KEY_F8"
    "F9": 67,  # "KEY_F9"
    "F10": 68,  # "KEY_F10"
    "Num_Lock": 69,  # "KEY_NUMLOCK"
    "Scroll_Lock": 70,  # "KEY_SCROLLLOCK"
    "KP_7": 71,  # "KEY_KP7"
    "KP_8": 72,  # "KEY_KP8"
    "KP_9": 73,  # "KEY_KP9"
    "KP_Subtract": 74,  # "KEY_KPMINUS"
    "KP_4": 75,  # "KEY_KP4"
    "KP_5": 76,  # "KEY_KP5"
    "KP_6": 77,  # "KEY_KP6"
    "KP_Add": 78,  # "KEY_KPPLUS"
    "KP_1": 79,  # "KEY_KP1"
    "KP_2": 80,  # "KEY_KP2"
    "KP_3": 81,  # "KEY_KP3"
    "KP_0": 82,  # "KEY_KP0"
    "KP_Delete": 83,  # "KEY_KPDOT"
    "F11": 87,  # "KEY_F11"
    "F12": 88,  # "KEY_F12"
    "KP_Enter": 96,  # "KEY_KPENTER"
    "Control_R": 97,  # "KEY_RIGHTCTRL"
    "KP_Divide": 98,  # "KEY_KPSLASH"
    "Print": 99,  # "KEY_SYSRQ"
    "Alt_R": 100,  # "KEY_RIGHTALT"
    "Linefeed": 101,  # "KEY_LINEFEED"
    "Home": 102,  # "KEY_HOME"
    "Up": 103,  # "KEY_UP"
    "Prior": 104,  # "KEY_PAGEUP"
    "Left": 105,  # "KEY_LEFT"
    "Right": 106,  # "KEY_RIGHT"
    "End": 107,  # "KEY_END"
    "Down": 108,  # "KEY_DOWN"
    "Next": 109,  # "KEY_PAGEDOWN"
    "Insert": 110,  # "KEY_INSERT"
    "Delete": 111,  # "KEY_DELETE"
    # "": 113,  # "KEY_MUTE"
    # "": 114,  # "KEY_VOLUMEDOWN"
    # "": 115,  # "KEY_VOLUMEUP"
    # lol no
    #"": 116,  # "KEY_POWER"	# SC System Power Down */
    "KP_Equal": 117,  # "KEY_KPEQUAL"
    "plusminus": 118,  # "KEY_KPPLUSMINUS"
    # "": 119,  # "KEY_PAUSE"
    # "": 120,  # "KEY_SCALE"	# AL Compiz Scale (Expose) */
    "KP_Decimal": 121,  # "KEY_KPCOMMA"
    # "": 122,  # "KEY_HANGEUL"
    # "": 123,  # "KEY_HANJA"
    # "": 124,  # "KEY_YEN"
    "Super_L": 125,  # "KEY_LEFTMETA"
    "Super_R": 126,  # "KEY_RIGHTMETA"
    # "": 127,  # "KEY_COMPOSE"
    # "": 128,  # "KEY_STOP"	# AC Stop */
    # "": 129,  # "KEY_AGAIN"
    # "": 130,  # "KEY_PROPS"	# AC Properties */
    # "": 131,  # "KEY_UNDO"	# AC Undo */
    # "": 132,  # "KEY_FRONT"
    # "": 133,  # "KEY_COPY"	# AC Copy */
    # "": 134,  # "KEY_OPEN"	# AC Open */
    # "": 135,  # "KEY_PASTE"	# AC Paste */
    # "": 136,  # "KEY_FIND"	# AC Search */
    # "": 137,  # "KEY_CUT"	# AC Cut */
    # "": 138,  # "KEY_HELP"	# AL Integrated Help Center */
    # "": 139,  # "KEY_MENU"	# Menu (show menu) */
    # "": 140,  # "KEY_CALC"	# AL Calculator */
    # "": 141,  # "KEY_SETUP"
    # "": 142,  # "KEY_SLEEP"	# SC System Sleep */
    # "": 143,  # "KEY_WAKEUP"	# System Wake Up */
    # "": 144,  # "KEY_FILE"	# AL Local Machine Browser */
    # "": 145,  # "KEY_SENDFILE"
    # "": 146,  # "KEY_DELETEFILE"
    # "": 147,  # "KEY_XFER"
    # "": 148,  # "KEY_PROG1"
    # "": 149,  # "KEY_PROG2"
    # "": 150,  # "KEY_WWW"	# AL Internet Browser */
    # "": 151,  # "KEY_MSDOS"
    # "": 152,  # "KEY_SCREENLOCK"	# AL Terminal Lock/Screensaver */
    # "": 153,  # "KEY_ROTATE_DISPLAY"	# Display orientation for e.g. tablets */
    # "": 154,  # "KEY_CYCLEWINDOWS"
    # "": 155,  # "KEY_MAIL"
    # "": 156,  # "KEY_BOOKMARKS"	# AC Bookmarks */
    # "": 157,  # "KEY_COMPUTER"
    # "": 158,  # "KEY_BACK"	# AC Back */
    # "": 159,  # "KEY_FORWARD"	# AC Forward */
    # "": 160,  # "KEY_CLOSECD"
    # "": 161,  # "KEY_EJECTCD"
    # "": 162,  # "KEY_EJECTCLOSECD"
    # "": 163,  # "KEY_NEXTSONG"
    # "": 164,  # "KEY_PLAYPAUSE"
    # "": 165,  # "KEY_PREVIOUSSONG"
    # "": 166,  # "KEY_STOPCD"
    # "": 167,  # "KEY_RECORD"
    # "": 168,  # "KEY_REWIND"
    # "": 169,  # "KEY_PHONE"	# Media Select Telephone */
    # "": 170,  # "KEY_ISO"
    # "": 171,  # "KEY_CONFIG"	# AL Consumer Control Configuration */
    # "": 172,  # "KEY_HOMEPAGE"	# AC Home */
    # "": 173,  # "KEY_REFRESH"	# AC Refresh */
    # "": 174,  # "KEY_EXIT"	# AC Exit */
    # "": 175,  # "KEY_MOVE"
    # "": 176,  # "KEY_EDIT"
    # "": 177,  # "KEY_SCROLLUP"
    # "": 178,  # "KEY_SCROLLDOWN"
    # "": 179,  # "KEY_KPLEFTPAREN"
    # "": 180,  # "KEY_KPRIGHTPAREN"
    # "": 181,  # "KEY_NEW"	# AC New */
    # "": 182,  # "KEY_REDO"	# AC Redo/Repeat */
    "F13": 183,  # "KEY_F13"
    "F14": 184,  # "KEY_F14"
    "F15": 185,  # "KEY_F15"
    "F16": 186,  # "KEY_F16"
    "F17": 187,  # "KEY_F17"
    "F18": 188,  # "KEY_F18"
    "F19": 189,  # "KEY_F19"
    "F20": 190,  # "KEY_F20"
    "F21": 191,  # "KEY_F21"
    "F22": 192,  # "KEY_F22"
    "F23": 193,  # "KEY_F23"
    "F24": 194,  # "KEY_F24"
    # "": 200,  # "KEY_PLAYCD"
    # "": 201,  # "KEY_PAUSECD"
    # "": 202,  # "KEY_PROG3"
    # "": 203,  # "KEY_PROG4"
    # "": 204,  # "KEY_DASHBOARD"	# AL Dashboard */
    # "": 205,  # "KEY_SUSPEND"
    # "": 206,  # "KEY_CLOSE"	# AC Close */
    # "": 207,  # "KEY_PLAY"
    # "": 208,  # "KEY_FASTFORWARD"
    # "": 209,  # "KEY_BASSBOOST"
    # "": 210,  # "KEY_PRINT"	# AC Print */
    # "": 211,  # "KEY_HP"
    # "": 212,  # "KEY_CAMERA"
    # "": 213,  # "KEY_SOUND"
    # "": 214,  # "KEY_QUESTION"
    # "": 215,  # "KEY_EMAIL"
    # "": 216,  # "KEY_CHAT"
    # "": 217,  # "KEY_SEARCH"
    # "": 218,  # "KEY_CONNECT"
    # "": 219,  # "KEY_FINANCE"	# AL Checkbook/Finance */
    # "": 220,  # "KEY_SPORT"
    # "": 221,  # "KEY_SHOP"
    # "": 222,  # "KEY_ALTERASE"
    # "": 223,  # "KEY_CANCEL"	# AC Cancel */
    # "": 224,  # "KEY_BRIGHTNESSDOWN"
    # "": 225,  # "KEY_BRIGHTNESSUP"
    # "": 226,  # "KEY_MEDIA"
    # "": 227,  # "KEY_SWITCHVIDEOMODE"	# Cycle between available video outputs (Monitor/LCD/TV-out/etc) */
    # "": 228,  # "KEY_KBDILLUMTOGGLE"
    # "": 229,  # "KEY_KBDILLUMDOWN"
    # "": 230,  # "KEY_KBDILLUMUP"
    # "": 231,  # "KEY_SEND"	# AC Send */
    # "": 232,  # "KEY_REPLY"	# AC Reply */
    # "": 233,  # "KEY_FORWARDMAIL"	# AC Forward Msg */
    # "": 234,  # "KEY_SAVE"	# AC Save */
    # "": 235,  # "KEY_DOCUMENTS"
    # "": 236,  # "KEY_BATTERY"
    # "": 237,  # "KEY_BLUETOOTH"
    # "": 238,  # "KEY_WLAN"
    # "": 239,  # "KEY_UWB"
    # "": 240,  # "KEY_UNKNOWN"
    # "": 241,  # "KEY_VIDEO_NEXT"	# drive next video source */
    # "": 242,  # "KEY_VIDEO_PREV"	# drive previous video source */
    # "": 243,  # "KEY_BRIGHTNESS_CYCLE"	# brightness up, after max is min */
    # "": 244,  # "KEY_BRIGHTNESS_AUTO"	# Set Auto Brightness: manual brightness control is off, rely on ambient */
    # "": 245,  # "KEY_DISPLAY_OFF"	# display device to off state */
    # "": 246,  # "KEY_WWAN"	# Wireless WAN (LTE, UMTS, GSM, etc.) */
    # "": 247,  # "KEY_RFKILL"	# Key that controls all radios */
    # "": 248,  # "KEY_MICMUTE"	# Mute / unmute the microphone */
}

# Shifted keysyms: we push modifier key events separately so remap these to
# unshifted key events

keyvalues.update({
    "exclam": 2,  # "KEY_1"
    "at": 3,  # "KEY_2"
    "numbersign": 4,  # "KEY_3"
    "dollar": 5,  # "KEY_4"
    "percent": 6,  # "KEY_5"
    "asciicircum": 7,  # "KEY_6"
    "ampersand": 8,  # "KEY_7"
    "asterisk": 9,  # "KEY_8"
    "parenleft": 10,  # "KEY_9"
    "parenright": 11,  # "KEY_0"
    "underscore": 12,  # "KEY_MINUS"
    "plus": 13,  # "KEY_EQUAL"
    "Q": 16,  # "KEY_Q"
    "W": 17,  # "KEY_W"
    "E": 18,  # "KEY_E"
    "R": 19,  # "KEY_R"
    "T": 20,  # "KEY_T"
    "Y": 21,  # "KEY_Y"
    "U": 22,  # "KEY_U"
    "I": 23,  # "KEY_I"
    "O": 24,  # "KEY_O"
    "P": 25,  # "KEY_P"
    "bracketleft": 26,  # "KEY_LEFTBRACE"
    "bracketright": 27,  # "KEY_RIGHTBRACE"
    "A": 30,  # "KEY_A"
    "S": 31,  # "KEY_S"
    "D": 32,  # "KEY_D"
    "F": 33,  # "KEY_F"
    "G": 34,  # "KEY_G"
    "H": 35,  # "KEY_H"
    "J": 36,  # "KEY_J"
    "K": 37,  # "KEY_K"
    "L": 38,  # "KEY_L"
    "colon": 39,  # "KEY_SEMICOLON"
    "quotedbl": 40,  # "KEY_APOSTROPHE"
    "asciitilde": 41,  # "KEY_GRAVE"
    "bar": 43,  # "KEY_BACKSLASH"
    "Z": 44,  # "KEY_Z"
    "X": 45,  # "KEY_X"
    "C": 46,  # "KEY_C"
    "V": 47,  # "KEY_V"
    "B": 48,  # "KEY_B"
    "N": 49,  # "KEY_N"
    "M": 50,  # "KEY_M"
    "less": 51,  # "KEY_COMMA"
    "greater": 52,  # "KEY_DOT"
    "question": 53,  # "KEY_SLASH"
})
