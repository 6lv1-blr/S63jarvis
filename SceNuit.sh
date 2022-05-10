touch /media/ramdiskNuit/Scenarios/\"$1\"
pico2wave -w=/media/ramdiskS63/temp.wav -l=fr-FR "\"$2\"" && /usr/bin/aplay /media/ramdiskS63/temp.wav
