#Python
import time
import digitalio
import board
import adafruit_matrixkeypad
import gpiozero as gz
from path import Path

# Membrane 3x4 matrix keypad on Raspberry Pi - https://www.adafruit.com/product/419
cols = [digitalio.DigitalInOut(x) for x in (board.D14, board.D18, board.D15)]
rows = [digitalio.DigitalInOut(x) for x in (board.D4, board.D17, board.D27, board.D22)]

# 3x4 matrix keypad on Raspberry Pi - rows and columns are mixed up for https://www.adafruit.com/product/3845 cols = [digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]
# rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D21, board.D20, board.D19)]

keys = 	((1, 2, 3),
	 (4, 5, 6),
	 (7, 8, 9),
	 ("*", 0, "#"))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


CombineDecroche=gz.Button(24)
BoutonR=gz.Button(3)
MemoFrontMontantDecroche = False
MemoFrontMontantR = False
MemoFrontMontantK = False
SequenceEnCours = ""
TimeoutSequence = 0
import simpleaudio as sa
filename = '/home/pi/AutomatismeS63/Sound/Numero/'
# https://realpython.com/playing-and-recording-sound-python/#playsound


# python dtmf-generator.py -p 1 -f 8000 -t 0.08 -s 0.08 -o ./Sound/Numero/1.wav -d -a 10000
DTMF_TABLE = {
    "1": sa.WaveObject.from_wave_file(filename+"1.wav"),
    "2": sa.WaveObject.from_wave_file(filename+"2.wav"),
    "3": sa.WaveObject.from_wave_file(filename+"3.wav"),
    "A": sa.WaveObject.from_wave_file(filename+"1.wav"),
    "4": sa.WaveObject.from_wave_file(filename+"4.wav"),
    "5": sa.WaveObject.from_wave_file(filename+"5.wav"),
    "6": sa.WaveObject.from_wave_file(filename+"6.wav"),
    "B": sa.WaveObject.from_wave_file(filename+"1.wav"),
    "7": sa.WaveObject.from_wave_file(filename+"7.wav"),
    "8": sa.WaveObject.from_wave_file(filename+"8.wav"),
    "9": sa.WaveObject.from_wave_file(filename+"9.wav"),
    "C": sa.WaveObject.from_wave_file(filename+"1.wav"),
    "*": sa.WaveObject.from_wave_file(filename+"E.wav"),
    "0": sa.WaveObject.from_wave_file(filename+"0.wav"),
    "#": sa.WaveObject.from_wave_file(filename+"S.wav"),
    "D": sa.WaveObject.from_wave_file(filename+"1.wav"),
}

while True:
	keys = keypad.pressed_keys
	if CombineDecroche.is_pressed:
		if MemoFrontMontantDecroche:
			print("Décroché")
			#DECO 3320
			Path('/media/ramdiskS63/NumeroCompose/13320').touch()
		MemoFrontMontantDecroche=False
	else:
		if not MemoFrontMontantDecroche:
			print("Raccroché")
		MemoFrontMontantDecroche=True

	if BoutonR.is_pressed:
		if MemoFrontMontantR:
			print("R")
			Path('/media/ramdiskS63/NumeroCompose/AnnuleSequence').touch()
		SequenceEnCours=""
		MemoFrontMontantR=False
	else:
		MemoFrontMontantR=True

	if keys:
		if MemoFrontMontantK:
			# print("Pressed: ", keys)
			SequenceEnCours += str(keys[0])
			DTMF_TABLE[str(keys[0])].play()
			MemoFrontMontantK=False
		TimeoutSequence = 14
	else:
		MemoFrontMontantK=True

	time.sleep(0.1)
	if TimeoutSequence>0:
		TimeoutSequence-=1
	elif SequenceEnCours != "":
		print(SequenceEnCours)
		Path('/media/ramdiskS63/NumeroCompose/1'+SequenceEnCours).touch()
		SequenceEnCours=""

