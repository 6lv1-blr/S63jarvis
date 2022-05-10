#!/bin/bash
#author by chuan
#from https://programmer.group/inotify-asynchronous-monitoring-mechanism.html
# %w pour le répertoire
# %f pour le fichier

inotifywait -mrq --timefmt '%y/%m/%d %H:%M' --format '%f' -e close_write /media/ramdiskS63/Cause/ |\
while read line
do
        /home/pi/AutomatismeS63/IncronSpeakS63.sh $line &
done
