#!/bin/bash
#author by chuan
#from https://programmer.group/inotify-asynchronous-monitoring-mechanism.html

inotifywait -mrq --timefmt '%y/%m/%d %H:%M' --format '%f' -e close_write /media/ramdiskS63/NumeroCompose/ |\
while read line
do
        /home/pi/AutomatismeS63/IncronNumeroCompose.sh $line &
done
