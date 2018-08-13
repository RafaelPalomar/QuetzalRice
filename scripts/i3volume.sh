#!/bin/bash

volume=$(/usr/libexec/i3blocks/volume)

if [ ${volume}  == "MUTE" ];
then
    echo "x"
else
    echo " ${volume}"
fi
