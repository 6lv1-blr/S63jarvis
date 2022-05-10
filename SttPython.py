#!/usr/bin/env python
# coding: utf-8


import speech_recognition as sr
from path import Path

import re
AUDIO_FILE="/media/ramdiskS63/VoiceS63.wav"

r = sr.Recognizer()

def NCmp(NomFichier):
    Path('/media/ramdiskS63/NumeroCompose/'+str(NomFichier)).touch()
    # Path('/media/ramdiskS63/'+str(NomFichier)).touch()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    Phrase = r.recognize_google(audio, language="fr-FR")
    print(Phrase)
    fichier = open("/media/ramdiskS63/VoiceS63.txt", "w")
    fichier.write(Phrase+'\n')
    fichier.close()





    if re.match('.*ANNUL.*',Phrase.upper()):    #pour Annulation si contient annule ou annulation
        Path('/media/ramdiskS63/Cause/Annulation de '+NomFichier+'.spk').touch()
    elif re.match('.*D.FIL.*MONT.*',Phrase.upper()):
        NCmp()
    elif re.match('.*ALLUME.*SALON.*',Phrase.upper()):
        NCmp(1501)
    elif re.match('.*FERME.*VOLET.*PREMIER.*',Phrase.upper()):    # "Ferme Volets du premier";;
        NCmp(18199)
    elif re.match('.*FERME.*VOLET.*DEUXIEME.*',Phrase.upper()):    # "Ferme Volets du Deuxième";;
        NCmp(18299)
    elif re.match('.*FERME.*(TOUS|TOUT).*VOLET.*',Phrase.upper()):    # "Ferme Tous les volets";;
        NCmp(1899)
    #Ouvre Tous
    elif re.match('.*OUVR.*VOLET.*PREMIER.*',Phrase.upper()):    # "Ouvre Volets du premier";;
        NCmp(18100)
    elif re.match('.*STOP.*VOLET.*PREMIER.*',Phrase.upper()):    # "Stoppe Volets du premier";;
        NCmp(18190)
    elif re.match('.*OUVR.*VOLET.*DEUXIEME.*',Phrase.upper()):    # "Ouvre Volets du Deuxième";;
        NCmp(18200)

    elif re.match('.*MODE.*TV',Phrase.upper()):    # "Mode TV";;
        NCmp(188)
    elif re.match('.*VOLET.*SALON.*',Phrase.upper()):    # "VOLET SALON";;
        NCmp(18101)
    elif re.match('.*VOLET.*SALLE .*A MANGER',Phrase.upper()):    # "VOLET SALLE A MANGER";;
        NCmp(18102)
    elif re.match('.*VOLET.*TERRASSE .*1',Phrase.upper()):    # "VOLET TERRASSE 1";;
        NCmp(18103)
    elif re.match('.*VOLET.*TERRASSE .*2',Phrase.upper()):    # "VOLET TERRASSE 2";;
        NCmp(18104)
    elif re.match('.*VOLET.*TERRASSE .*3',Phrase.upper()):    # "VOLET TERRASSE 3";;
        NCmp(18105)
    elif re.match('.*VOLET.*TERRASSE .*4',Phrase.upper()):    # "VOLET TERRASSE 4";;
        NCmp(18106)
    elif re.match('.*VOLET.*TERRASSE .*5',Phrase.upper()):    # "VOLET TERRASSE 5";;
        NCmp(18107)
    elif re.match('.*VOLET.*TERRASSE .*6',Phrase.upper()):    # "VOLET TERRASSE 6";;
        NCmp(18108)
    elif re.match('.*VOLET.*CUISINE.*',Phrase.upper()):    # "VOLET CUISINE";;
        NCmp(18109)
    elif re.match('.*STORE.*TERRASSE.*',Phrase.upper()):    # "STORE TERRASSE";;
        NCmp(18110)
    elif re.match('.*VOLET.*BUREAU .*3',Phrase.upper()):    # "VOLET BUREAU 3";;
        NCmp(18111)
    elif re.match('.*VOLET.*BUREAU .*2',Phrase.upper()):    # "VOLET BUREAU 2";;
        NCmp(18112)
    elif re.match('.*VOLET.*BUREAU .*1',Phrase.upper()):    # "VOLET BUREAU 1";;
        NCmp(18113)
    elif re.match('.*VOLET.*SALLE .*EAU',Phrase.upper()):    # "VOLET SALLE D'EAU";;
        NCmp(18114)

    elif re.match('.*VOLET.*CHAMBRE .*NOUS 1',Phrase.upper()):    # "VOLET CHAMBRE NOUS 1";;
        NCmp(18201)
    elif re.match('.*VOLET.*CHAMBRE .*NOUS 2',Phrase.upper()):    # "VOLET CHAMBRE NOUS 2";;
        NCmp(18202)
    elif re.match('.*VOLET.*BASTIEN .*1',Phrase.upper()):    # "VOLET BASTIEN 1";;
        NCmp(18203)
    elif re.match('.*VOLET.*BASTIEN .*2',Phrase.upper()):    # "VOLET BASTIEN 2";;
        NCmp(18204)
    elif re.match('.*VOLET.*BIBLIOTHEQUE.*',Phrase.upper()):    # "VOLET BIBLIOTHEQUE";;
        NCmp(18205)
    elif re.match('.*VOLET.*CHAMBRE .*BLANCHE 1',Phrase.upper()):    # "VOLET CHAMBRE BLANCHE 1";;
        NCmp(18206)
    elif re.match('.*VOLET.*CHAMBRE .*BLANCHE 2',Phrase.upper()):    # "VOLET CHAMBRE BLANCHE 2";;
        NCmp(18207)
    elif re.match('.*VOLET.*SALLE .*DE BAINS 1',Phrase.upper()):    # "VOLET SALLE DE BAINS 1";;
        NCmp(18208)
    elif re.match('.*VOLET.*SALLE .*DE BAINS 2',Phrase.upper()):    # "VOLET SALLE DE BAINS 2";;
        NCmp(18209)
    elif re.match('.*VOLET.*SALLE .*DE BAINS 3',Phrase.upper()):    # "VOLET SALLE DE BAINS 3";;
        NCmp(18210)

    #L+NumLumière
    elif re.match('.*LUMI.RE.*SALON.*',Phrase.upper()):    # "LUMIERE SALON";;
        NCmp(1501)
    elif re.match('.*LUMI.RE.*SALLE .*A MANGER',Phrase.upper()):    # "LUMIERE SALLE A MANGER";;
        NCmp(1502)
    elif re.match('.*LUMI.RE.*CUISINE.*',Phrase.upper()):    # "LUMIERE CUISINE";;
        NCmp(1503)
    elif re.match('.*LUMI.RE.*PLAN .*TRAVAIL',Phrase.upper()):    # "LUMIERE PLAN TRAVAIL";;
        NCmp(1504)
    elif re.match('.*LUMI.RE.*HALOGÈNE.*',Phrase.upper()):    # "LUMIERE HALOGÈNE";;
        NCmp(1505)
    elif re.match('.*LUMI.RE.*TERRASSE.*',Phrase.upper()):    # "LUMIERE TERRASSE";;
        NCmp(1506)
    elif re.match('.*LUMI.RE.*ESCALIER.*',Phrase.upper()):    # "LUMIERE ESCALIER";;
        NCmp(1507)
    elif re.match('.*LUMI.RE.*COULOIR.*',Phrase.upper()):    #  "Lumiere Couloir";;
        NCmp(1508)
    elif re.match('.*LUMI.RE.*PLACARD.*',Phrase.upper()):    # "LUMIERE PLACARD";;
        NCmp(1509)
    elif re.match('.*LUMI.RE.*BUREAU.*',Phrase.upper()):    # "LUMIERE BUREAU";;
        NCmp(1511)
    elif re.match('.*LUMI.RE.*COULOIR .*WC',Phrase.upper()):    # "LUMIERE COULOIR WC";;
        NCmp(1512)
    elif re.match('.*LUMI.RE.*WC .*1ER',Phrase.upper()):    # "LUMIERE WC 1ER";;
        NCmp(1513)
    elif re.match('.*LUMI.RE.*SALLE .*D''EAU',Phrase.upper()):    # "LUMIERE SALLE D'EAU";;
        NCmp(1514)
    elif re.match('.*LUMI.RE.*ESCALIER .*VERS GARAGE',Phrase.upper()):    # "LUMIERE ESCALIER VERS GARAGE";;
        NCmp(1515)

    elif re.match('.*LUMI.RE.*COULOIR.*',Phrase.upper()):    # "LUMIERE COULOIR";;
        NCmp(1521)
    elif re.match('.*LUMI.RE.*CHAMBRE .*NOUS',Phrase.upper()):    # "LUMIERE CHAMBRE NOUS";;
        NCmp(1522)
    elif re.match('.*LUMI.RE.*BASTIEN.*',Phrase.upper()):    # "LUMIERE BASTIEN";;
        NCmp(1523)
    elif re.match('.*LUMI.RE.*BIBLIOTHEQUE.*',Phrase.upper()):    # "LUMIERE BIBLIOTHEQUE";;
        NCmp(1524)
    elif re.match('.*LUMI.RE.*CHAMBRE .*BLANCHE',Phrase.upper()):    # "LUMIERE CHAMBRE BLANCHE";;
        NCmp(1525)
    elif re.match('.*LUMI.RE.*WC.*',Phrase.upper()):    # "LUMIERE WC";;
        NCmp(1526)
    elif re.match('.*LUMI.RE.*SALLE .*DE BAINS',Phrase.upper()):    # "LUMIERE SALLE DE BAINS";;
        NCmp(1527)

    elif re.match('.TEIN.*PREMIER',Phrase.upper()):    # "Extinction Lumière premier";;
        NCmp(15100)
    elif re.match('.TEIN.*DEUXI.ME',Phrase.upper()):    # "Extinction Lumière deuxième";;
        NCmp(15200)





    else:
        Path('/media/ramdiskS63/NumeroCompose/197').touch()
except Exception as e:
    print(e)
    pass
