#!/usr/bin/python

import string
import sys
import os

#ALLOWED LAYOUTS
layouts = ['no','es','us']

#CURRENT LAYOUT IN ALLOWED
current_is_allowed = True

#FILTER SETXKBMAP
def filter_layout(setxkbmap_output):
    return setxkbmap_output[0].split(':')[1].strip(' \t\n\r').upper()
        

## ENTRY POINT
if __name__ == '__main__':

    # Check for setxkbmap
    if os.system('setxkbmap -query 2&>/dev/null'):
        print('Error: setxkbmap not present',file=sys.stderr)
        sys.exit(1)

    # Get the current keyboard layout
    setxkbmap = os.popen('setxkbmap -query | grep layout')
    current_layout = filter_layout(setxkbmap.readlines()).lower()
    if current_layout not in layouts:
        current_is_allowed = False
    
    # Check arguments
    if len(sys.argv) == 1: # No arguments -- query mode
        print(current_layout.upper())
        
    elif len(sys.argv) == 2: #'next' argument
        if sys.argv[1] == 'next':
            if current_is_allowed:
                index = layouts.index(current_layout)
                new_layout = layouts[(index+1)%len(layouts)]
                os.popen('setxkbmap '+ new_layout.lower())
            
