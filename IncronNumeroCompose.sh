echo "$*"
#if test ${i##*.} = "mp3"; then
#mpg321 /media/ramdiskJour/Cause/$i
#;fi


case $* in
	#COU Lumière couloir
	1208) touch /media/ramdiskJour/Scenarios/8015;touch /media/ramdiskJour/Scenarios/8002;touch /media/ramdiskJour/Scenarios/8505;touch /media/ramdiskJour/Scenarios/8014; pico2wave -w=/media/ramdiskS63/temp.wav -l=fr-FR "Lumière couloir" && aplay /media/ramdiskS63/temp.wav;;

	13320) mpg123 /home/pi/AutomatismeS63/Sound/DomovoyTchenada.mp3 &
		/bin/sleep 2
		rec -V1 -q -r 16000 -c 1 -b 16 -e signed-integer --endian little /media/ramdiskS63/VoiceS63.wav gain 15 silence 1 0.1 0.1% 1 0.5 0.1% pad 0.5 0.5 trim 0 5 && /home/pi/AutomatismeS63/SttPython.py;;
	#V+NumVolet
	#Ferme tous
	1899)  /home/pi/AutomatismeS63/SceJour.sh 8902 "Ferme Tous les volets"; /home/pi/AutomatismeS63/SceNuit.sh 2790 " ";;
	18199) /home/pi/AutomatismeS63/SceJour.sh 8902 "Ferme Volets du premier";;
	18299) /home/pi/AutomatismeS63/SceNuit.sh 2790 "Ferme Volets du Deuxième";;
	#Ouvre Tous
	18100) /home/pi/AutomatismeS63/SceJour.sh 8901 "Ouvre Volets du premier";;
	18190) /home/pi/AutomatismeS63/SceJour.sh 8903 "Stoppe Volets du premier";;
	18200) /home/pi/AutomatismeS63/SceNuit.sh 1102 "Ouvre Volets du Deuxième";;

	188)   /home/pi/AutomatismeS63/SceJourTV.sh 9588 "Mode TV";;
	18101) /home/pi/AutomatismeS63/SceJour.sh 9509 "Volet Salon";;
	18102) /home/pi/AutomatismeS63/SceJour.sh 9525 "Volet Salle A Manger";;
	18103) /home/pi/AutomatismeS63/SceJour.sh 9511 "Volet Terrasse 1";;
	18104) /home/pi/AutomatismeS63/SceJour.sh 9515 "Volet Terrasse 2";;
	18105) /home/pi/AutomatismeS63/SceJour.sh 9513 "Volet Terrasse 3";;
	18106) /home/pi/AutomatismeS63/SceJour.sh 9517 "Volet Terrasse 4";;
	18107) /home/pi/AutomatismeS63/SceJour.sh 9519 "Volet Terrasse 5";;
	18108) /home/pi/AutomatismeS63/SceJour.sh 9521 "Volet Terrasse 6";;
	18109) /home/pi/AutomatismeS63/SceJour.sh 9523 "Volet Cuisine";;
	18110) /home/pi/AutomatismeS63/SceJour.sh 9527 "Store Terrasse";;
	18111) /home/pi/AutomatismeS63/SceJour.sh 9507 "Volet Bureau 3";;
	18112) /home/pi/AutomatismeS63/SceJour.sh 9505 "Volet Bureau 2";;
	18113) /home/pi/AutomatismeS63/SceJour.sh 9503 "Volet Bureau 1";;
	18114) /home/pi/AutomatismeS63/SceJour.sh 9501 "Volet Salle d'eau";;

	18201) /home/pi/AutomatismeS63/SceNuit.sh 9527 "Volet Chambre Nous 1";;
	18202) /home/pi/AutomatismeS63/SceNuit.sh 9519 "Volet Chambre Nous 2";;
	18203) /home/pi/AutomatismeS63/SceNuit.sh 9531 "Volet Bastien 1";;
	18204) /home/pi/AutomatismeS63/SceNuit.sh 9529 "Volet Bastien 2";;
	18205) /home/pi/AutomatismeS63/SceNuit.sh 9547 "Volet Bibliotheque";;
	18206) /home/pi/AutomatismeS63/SceNuit.sh 9543 "Volet Chambre Blanche 1";;
	18207) /home/pi/AutomatismeS63/SceNuit.sh 9545 "Volet Chambre Blanche 2";;
	18208) /home/pi/AutomatismeS63/SceNuit.sh 9521 "Volet Salle de bains 1";;
	18209) /home/pi/AutomatismeS63/SceNuit.sh 9523 "Volet Salle de bains 2";;
	18210) /home/pi/AutomatismeS63/SceNuit.sh 9541 "Volet Salle de bains 3";;

	#L+NumLumière
	1501) /home/pi/AutomatismeS63/SceJour.sh 8007 "Lumiere Salon";;
	1502) /home/pi/AutomatismeS63/SceJour.sh 8012 "Lumiere Salle A Manger";;
	1503) /home/pi/AutomatismeS63/SceJour.sh 8004 "Lumiere Cuisine";;
	1504) /home/pi/AutomatismeS63/SceJour.sh 8001 "Lumiere Plan Travail";;
	1505) /home/pi/AutomatismeS63/SceJour.sh 8008 "Lumiere Halogène";;
	1506) /home/pi/AutomatismeS63/SceJour.sh 8009 "Lumiere Terrasse";;
	1507) /home/pi/AutomatismeS63/SceJour.sh 8011 "Lumiere Escalier";;
	1508) /home/pi/AutomatismeS63/SceJour.sh 301  "Lumiere Couloir";;
	1509) /home/pi/AutomatismeS63/SceJour.sh 8505 "Lumiere Placard";;
	1511) /home/pi/AutomatismeS63/SceJour.sh 8013 "Lumiere Bureau";;
	1512) /home/pi/AutomatismeS63/SceJour.sh 8014 "Lumiere Couloir WC";;
	1513) /home/pi/AutomatismeS63/SceJour.sh 8003 "Lumiere WC 1er";;
	1514) /home/pi/AutomatismeS63/SceJour.sh 8016 "Lumiere Salle d'eau";;
	1515) /home/pi/AutomatismeS63/SceJour.sh 8010 "Lumiere Escalier Vers Garage";;

	1521) /home/pi/AutomatismeS63/SceNuit.sh 8007 "Lumiere Couloir";;
	1522) /home/pi/AutomatismeS63/SceNuit.sh 8006 "Lumiere Chambre Nous";;
	1523) /home/pi/AutomatismeS63/SceNuit.sh 8001 "Lumiere Bastien";;
	1524) /home/pi/AutomatismeS63/SceNuit.sh 8007 "Lumiere Bibliotheque";;
	1525) /home/pi/AutomatismeS63/SceNuit.sh 8005 "Lumiere Chambre Blanche";;
	1526) /home/pi/AutomatismeS63/SceNuit.sh 8010 "Lumiere WC";;
	1527) /home/pi/AutomatismeS63/SceNuit.sh 201  "Lumiere Salle de bains";;

	15100) /home/pi/AutomatismeS63/SceJour.sh 390 "Extinction Lumière premier";;
	15200) /home/pi/AutomatismeS63/SceNuit.sh 1190 "Extinction Lumière deuxième";;

	#FR
	137) cp /home/pi/AutomatismeS63/Sound/DemarrageFR.mp3 /home/pi/AutomatismeS63/Sound/DomovoyTchenada.mp3;;
	#RU
	178) cp /home/pi/AutomatismeS63/Sound/DomovoyTchenada.RU.mp3 /home/pi/AutomatismeS63/Sound/DomovoyTchenada.mp3;;

	#IPA annonce l'ip courante pour retrouver sur windows
	1472) touch /media/ramdiskS63/Cause/$(ip -4 addr show dev wlan0 | awk '/inet / { print $2 }' | sed -e 's/\./point/g' | sed -e 's/\/..//g').spk;;
	15) /home/pi/AutomatismeS63/SceMicroPython.sh;;
	1533) /home/pi/AutomatismeS63/SceMicroPython.sh;;
	16) /home/pi/AutomatismeS63/SceMicroPythonDesc.sh;;

	1737529) aplay /media/ramdiskS63/VoiceS63.wav;;
	17375298) cat /media/ramdiskS63/VoiceS63.txt | sudo pico2wave -w=/media/ramdiskS63/temp.wav -l=fr-FR $* && /usr/bin/aplay /media/ramdiskS63/temp.wav;;

	#12) aplay Liste des commande
	#12) aplay
	#XP
	197) mpg123 /home/pi/AutomatismeS63/Sound/DemarrageWindowsXP.mp3 -g 300;;

	# reboot
	1732008) touch "/media/ramdiskS63/Cause/Arret en cours.spk" 
        	sudo reboot;;

	178304258) touch "/media/ramdiskS63/Cause/Arret en cours..." 
		sudo halt;;

	178687) /home/pi/AutomatismeS63/svnup.sh;;

	AnnuleSequence) killall mpg321;mpg321 /home/pi/AutomatismeS63/Sound/NumeroNonAttribueTonalite.mp3 -g 30;;
	*) killall mpg321;mpg321 /home/pi/AutomatismeS63/Sound/NumeroNonAttribue.mp3 -g 200;;
esac

rm /media/ramdiskS63/NumeroCompose/"$*"
