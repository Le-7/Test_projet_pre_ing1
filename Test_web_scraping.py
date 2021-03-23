import requests                           #importation des différentes bibliothèques (certains bouts de codes ont été empruntés directement de ces bibliothèques) 
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pyttsx3
import face_recognition
import cv2
import numpy as np
engine = pyttsx3.init()        #initialisation de la synthèse voale
voice = engine.getProperty('voices')[2] #Voix francaise
engine.setProperty('voice', voice.id)
engine.setProperty('rate',145) #Vitesse de lecture


def iaquiparle() :   #message d accueil
    print("""

   _____ _        _   _               __  __      _               ___    ___  
  / ____| |      | | (_)             |  \/  |    | |             |__ \  / _ \ 
 | (___ | |_ __ _| |_ _  ___  _ __   | \  / | ___| |_ ___  ___      ) || | | |
  \___ \| __/ _` | __| |/ _ \| '_ \  | |\/| |/ _ \ __/ _ \/ _ \    / / | | | |
  ____) | || (_| | |_| | (_) | | | | | |  | |  __/ ||  __/ (_) |  / /_ | |_| |
 |_____/ \__\__,_|\__|_|\___/|_| |_| |_|  |_|\___|\__\___|\___/  |____(_)___/                                                                                                                                                                                                                                                                                                                                                                              
""")
    engine.say("Bonjour c'est moi la meilleure des IA, veuillez choisir une fonction")
    engine.runAndWait()



def DetH():        #affichage date et heure
    engine.say("Voici la date et l'heure")
    engine.runAndWait()
    print(str(datetime.now()))

def lecteurinfo() :                 #prevision méteo
    engine.say("Veuillez saisir le jour")
    engine.runAndWait()
    a= str(input('Veuillez saisir le jour sous format Lun17Déc (4jours de marge):\n'))
    engine.say("Veuillez saisir l'heure")
    engine.runAndWait()
    b= str(input('Veuillez saisir l heure sous format 0h (Commence a 1h et incrémenté de 3):\n'))
    #a.encode('cp1252')  #encodage dans le meme format que le fichier csv (on peut voir l encodage avec le print en commentaire plus en bas)
    #b.encode('cp1252')

    with open('info_meteo.csv', newline='') as  read_obj:  #ouverture du fichier en mode lecture seule avec parametres personalisés
        csv.register_dialect('custom', delimiter=' ',doublequote=True, quoting=csv.QUOTE_NONE, escapechar=' ')  # création des parametres personalisés (consulter doc pour plus d info)
        spamreader = csv.reader( read_obj,dialect='custom') #lecture du contenue avec les parametres 'custom' créés juste avant
        #print(read_obj)
        for row in spamreader:  #bon ca normalement faut juste traduire mais bon : pour chaque 'field'(champs de texte) de chaque 'row'(rangée)
            for field in row:
                if a in field:  #on regarde si 'a'(la date) est dans le champ
                    i=1
                    while i<101 :
                        try:     #gestion des exceptions
                            spamreader.__next__()                   #si a est dedans on prend les 100 champs suivants
                            for field  in spamreader.__next__():
                                if b in field:                      #si 'b'(heures) est dans les 100 champs suivants on affiche les 6 lignes(caractéristiques) apres 'b' 
                                    j=1
                                    while j<7 :
                                        print("caractéristique : ",j) #chiffre de la caractéristique
                                        print(spamreader.__next__())  #affichage des caractéristique
                                        j=j+1
                        except:
                            pass       #si il y a un bug alors on passe la procédure pour que l erreur ne soit pas fatal, d'où le 'try' avant 
                        i=i+1
    engine.say("Et voila tes prévisions")
    engine.runAndWait()

def creationbasededonnées():        #web scraping         
    req = requests.get('https://www.meteo60.fr/previsions-meteo-france-paris.html')  #URL du site ciblé
    soup = BeautifulSoup(req.text, "lxml")       #on créé une soupe de données, lire doc de BS
    jour =soup.findAll('td', {'class':'jour'})   #on cherche les données voulue
    with open("info_meteo.csv", 'w', newline=None ) as out_file:   #on creer un fichier csv avec nos données
        csv.register_dialect('custom', delimiter=' ',doublequote=True, quoting=csv.QUOTE_NONE, escapechar=' ')   #parametres personalisés
        writer = csv.writer(out_file,'custom')  #on initialise le writer avec nos parametres donnés avant
        informations = soup.find('table', {'class':'previsions'}).findAll('tbody', {'class':'ligne_jour'})  #on cherche dans la soup les informaations nous étant utiles
        for informations in informations :
            row = informations.text.strip() #les rangées prennent comme valeurs les informations
            writer.writerow(row)   #on ecrit les rangées dans le fichier

def detection():
  video_capture = cv2.VideoCapture(0)

    # Création d'un profil avec encodage du visage dans le systeme neuronale.
  personne1_image = face_recognition.load_image_file("Matheo_Costa.jpg")
  personne1_face_encoding = face_recognition.face_encodings(personne1_image)[0]
  temperatureenmemoire1= 78
  print("p1 : Matheo Costa a comme temperature favorite :",temperatureenmemoire1,"°C \n")

  
  # Pareillement.
  personne2_image = face_recognition.load_image_file("Orcan_Og.jpg")
  personne2_face_encoding = face_recognition.face_encodings(personne2_image)[0]
  temperatureenmemoire2= 84
  print("p2 : Orcan Og a comme temperature favorite :",temperatureenmemoire2,"°C \n")

   # Pareillement.
  personne3_image = face_recognition.load_image_file("Matheo_Pereira.jpg")
  personne3_face_encoding = face_recognition.face_encodings(personne3_image)[0]
  temperatureenmemoire3= 44
  print("p3 : Matheo Pereira a comme temperature favorite :",temperatureenmemoire3,"°C \n")

   # Pareillement.
  personne4_image = face_recognition.load_image_file("Anissa_Aït-Chadi.jpg")
  personne4_face_encoding = face_recognition.face_encodings(personne4_image)[0]
  temperatureenmemoire4= 24
  print("p4 : Anissa Aït-Chadi a comme temperature favorite :",temperatureenmemoire4,"°C \n")

   # Pareillement.
  personne5_image = face_recognition.load_image_file("Antoine_Warlet.jpg")
  personne5_face_encoding = face_recognition.face_encodings(personne5_image)[0]
  temperatureenmemoire5= 667
  print("p5 : Antoine Warlet a comme temperature favorite :",temperatureenmemoire5,"°C \n")



  engine.say("Pour quitter le mode détection veuillez sélectionner la fenetre et appuyer sur la lettre 'Q'")
  engine.runAndWait()

    # Création des champs de données avec visages, noms et temperatures favorites 
  known_face_encodings = [
      personne1_face_encoding,
      personne2_face_encoding,
      personne3_face_encoding,
      personne4_face_encoding,
      personne5_face_encoding
    ]
  known_face_names = [
      "Matheo Costa",
      "Orcan Og",
      "Matheo Pereira",
      "Anissa Ait-Chadi",
      "Antoine Warlet"
  ]

  temppref =[
      temperatureenmemoire1,
      temperatureenmemoire2,
      temperatureenmemoire3,
      temperatureenmemoire4,
      temperatureenmemoire5,
  ]

    # Initialisation de variables utiles au fonctionnement
  face_locations = []
  face_encodings = []
  face_names = []
  process_this_frame = True

  while True:
        # On lit frame par frame la vidéo
        ret, frame = video_capture.read()

        # On réajuste l'image en format 1/4 pour une plus grande rapidité d'execution
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # On convertit l'image de format BGR(que OpenCV utilise) en RGB (que face_recognition utilise)
        rgb_small_frame = small_frame[:, :, ::-1]

        # On utilise que les frames qui nous interessent pour gagner du temps
        if process_this_frame:
            # On cherche tous les visages et leurs localisations dans chaque frame 
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # On regarde si les visages sont connus
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Inconnu"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    tempeaff = temppref[best_match_index] 
                    print(name," détecté(e), temperature changée à :",tempeaff,"°C\n")
                face_names.append(name)

        process_this_frame = not process_this_frame


        # On affiche les résultats
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # On remet l'image au format initiale (on l'avais passé en 1/4)
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # On met un rectangle pour chaque visage
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # On met une étiquette avec le nom pour chaque visage
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
          

        # on affiche le résultat
        cv2.imshow('Video', frame)

        # On appuie sur 'Q' pour casser la boucle infinie
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # On relache et détruit les fenetres
  video_capture.release()
  cv2.destroyAllWindows()
    
#programme principal
creationbasededonnées()
iaquiparle()
print(" 1 = Date et heure \n 2 = prévisions météo  \n 3 = réglage automatique de la température \n exit = quitter")
while 1 : #menu
    menu= str(input('Veuillez saisir le chiffre correspondant a la fonction souhaitée \n'))
    if menu == '1' :
        DetH()
    elif menu == '2' : 
        print("\n_______________________________________\n Les différentes caractéristiques : \n 1 : Température(ressentie) \n 2 : rien \n 3 : Vent moyen en km/h \n 4 : Plus forte rafale en km/h \n 5 : Pression en hPa \n 6 : pluie sous 3 h\n_______________________________________\n")
        lecteurinfo()
    elif menu == '3' : 
        detection()
    elif menu == 'exit' :
        print("Merci de m'avoir utilisé, aurevoir")
        engine.say("Merci de m'avoir utilisé, aurevoir PS: Matheo est le plus BG je le kiff")
        engine.runAndWait()
        break
    else :
        print("Caractère non reconnu")
        engine.say("Veuillez saisir un caractère valide")
        engine.runAndWait()
            
    