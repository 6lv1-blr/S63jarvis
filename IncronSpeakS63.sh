i=$*
if test ${i#*.} = "spk"; then pico2wave -w=/media/ramdiskS63/temp.wav -l=fr-FR ${i%.*} && /usr/bin/aplay /media/ramdiskS63/temp.wav ;fi
if test ${i#*.} = "mp3"; then mpg321 /home/pi/AutomatismeS63/Sound/$i ;fi
if test ${i#*.} = "sms"; then wget -qO- --no-check-certificate "https://smsapi.free-mobile.fr/sendmsg?user=XXXX&pass=XXXXXX&msg="$(perl -MURI::Escape -e 'print uri_escape('"${i%.*}"');' "$*") ;fi
rm /media/ramdiskS63/Cause/"$*"
