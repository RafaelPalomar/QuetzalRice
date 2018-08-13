#!/bin/bash


# No arguments given, then check current layout and change to next (cycle)
if [ ${#} -eq 0 ]; then
    current_layout=$(setxkbmap -query | grep layout | awk '{print $2 }')
    
    if [ "${current_layout}" == "us" ]; then
	echo "US"
    elif [ "${current_layout}" == "no" ]; then
	echo "NO"
    else
	echo "ES"
    fi
elif [[ ${#} -eq 1 && "${1}" == "next" ]]; then # Argument given (expected layout)
    current_layout=$(setxkbmap -query | grep layout | awk '{print $2 }')

    if [ "${current_layout}" == "us" ]; then
	setxkbmap no
	echo "NO"
    elif [ "${current_layout}" == "no" ]; then
	setxkbmap es
	echo "ES"
    else
	setxkbmap us
	echo "US"
    fi
else
    exit 0
fi


[[ -f ~/.Xmodmap ]] && xmodmap ~/.Xmodmap
