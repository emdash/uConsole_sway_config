#! /usr/bin/env python
#
# Watch input events on the gamepad, and re-inject as keyboard events
# according to this config.
#
# Depends: input-utils, wtype, and python3-pexpect packages.
#
# A word of caution: this script has to do a fair amount of processing
# per event, so you probably want to disable this script for actual
# gaming.

# TBD: implement an easy way to inhibit this script for actual
#      gameplay.
# TBD: allow binding arbitrary shell commands / sway commands.

import os
import pexpect
import re

# Symbolic names for the keycodes. Don't touch these.
SELECT = b"128"
START  = b"129"
Y      = b"123"
X      = b"120"
B      = b"122"
A      = b"121"

# Edit this table to suit your preferences.
KEYMAP = {
    SELECT: "Super_L",
    START:  "Super_R",
    Y:      "Insert",
    X:      "Prior",
    B:      "Delete",
    A:      "Next",
}

# Corresponds to /dev/input/event5, which seems to be the gamepad. Not
# sure if it can change. I guess we'll see.
DEV_NUMBER = 5

# Regular expressions given to `expect()`.
EVENT_RES  = [
    # Matches the actual information we want, so it's given first.
    r"\(0x(\d+)\) (pressed|released)\r\n",
    # Matches anything else to avoid a match error.
    r"\.*\r\n",
]

# Send the key code via wtype.
def send_key(code, state):
    keysym = KEYMAP[code]
    if state == b"pressed":
        print(f"{code} -> {keysym} pressed")
        os.system(f"wtype -P {keysym}")
    else:
        print(f"{code} -> {keysym} released")
        os.system(f"wtype -p {keysym}")

# Run forever
while True:
    # Spawn `input-events` subprocess and wait for it to signal that
    # it is ready.
    print("spawning")
    child = pexpect.spawn(f"input-events -t 3000 {DEV_NUMBER}")
    child.expect("waiting for events")
    try:
        # decode each event as it comes in.
        while True:
            if child.expect(EVENT_RES, timeout=None) == 0:
                (code, state) = child.match.groups(1)
                send_key(code, state)
    except KeyboardInterrupt:
        exit(1)
    except pexpect.exceptions.EOF:
        # The process might time out or otherwise fail. -- there is no
        # way to tell `input-events` that you want an infinite
        # timeout.
        print(f"subprocess terminated {e}")
