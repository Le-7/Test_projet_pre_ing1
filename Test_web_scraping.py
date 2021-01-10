import requests                           #importation des différentes bibliothèques
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pyttsx3
engine = pyttsx3.init()        #initialisation de la synthèse voale
voice = engine.getProperty('voices')[2] #Voix francaise
engine.setProperty('voice', voice.id)
engine.setProperty('rate',145) #Vitesse de lecture
temperatureenmemoire= 19

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
    a.encode('cp1252')  #encodage dans le meme format que le fichier csv (on peut voir l encodage avec le print en commentaire plus en bas)
    b.encode('cp1252')

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
   
def reglageauto():    # a finir
    engine.say("Réglage automatique")
    engine.say("La température a été réglée sur")
    cheh=str(temperatureenmemoire)+" degrés"
    engine.say(cheh) 
    engine.say("Dis pas merci chakal ça sert a rien je peut pas te répondre")
    engine.runAndWait()

                           
                    
                        

def tempenmemoire():    #changement de la température favorites
    global temperatureenmemoire     #on change la variable de facon globale dans cette procédure
    engine.say("Veuillez saisir la nouvelle température souhaitée")
    engine.runAndWait()
    try :
        temperatureenmemoire = float(input("Nouvelle température : \n"))
        print("Nouvelle température enregistrée : ",temperatureenmemoire,'°C')
    except :
        print("Valeur saisie non valable")
        engine.say("Valeur saisie non valable, je fait exploser ta maison ")
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

#programme principal
creationbasededonnées()
iaquiparle()
print(" 1 = Date et heure \n 2 = prévisions météo  \n 3 = réglage automatique de la température \n 4 = Changer température en mémoire \n Tout autre caractere = quitter")
while 1 : #menu
    menu= str(input('Veuillez saisir le chiffre correspondant a la fonction souhaitée \n'))
    if menu == '1' :
        DetH()
    elif menu == '2' : 
        print("Les différentes caractéristiques : \n 1 : Température(ressentie) \n 2 : rien \n 3 : Vent moyen en km/h \n 4 : Plus forte rafale en km/h \n 5 : Pression en hPa \n 6 : pluie sous 3 h \n")
        lecteurinfo()
    elif menu == '3' : 
        print("La température en mémoire est de : ",temperatureenmemoire,'°C')
        reglageauto()
    elif menu == '4' :
        print("La température en mémoire est de : ",temperatureenmemoire,'°C')
        tempenmemoire()
       
    else :
        print("Merci de m'avoir utilisé, aurevoir")
        engine.say("Merci de m'avoir utilisé, aurevoir PS: Matheo est le plus BG je le kiff")
        engine.runAndWait()
        break