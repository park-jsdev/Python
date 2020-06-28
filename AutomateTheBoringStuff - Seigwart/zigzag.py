#!/usr/bin/env python

import time, sys
indent = 0 # How many spaces to indent.
indent_increasing = True

try:
    while True: # main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indent_increasing:
            # Increase num of spaces
            indent = indent + 1
            if indent == 20:
                # Change direction
                indent_increasing = False
            else:
                # Decrease num of spaces
                indent = indent - 1
                if indent == 0:
                    # Change direction
                    indent_increasing = True
except KeyboardInterrupt:
    sys.exit()