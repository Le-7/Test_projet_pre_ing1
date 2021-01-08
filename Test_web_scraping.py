import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pyttsx3
engine = pyttsx3.init()
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
    engine.say("Wesh la zone c'est moi la plus conne des IA, veuillez choisir une fonction")
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
        csv.register_dialect('custom', delimiter=' ',doublequote=True, quoting=csv.QUOTE_NONE, escapechar=' ')
        spamreader = csv.reader( read_obj,dialect='custom') #lecture du contenue
        #print(read_obj)
        for row in spamreader:  
            for field in row:
                if a in field: 
                    i=1
                    while i<101 :
                        try:     #gestion des exceptions
                            spamreader.__next__()
                            for field  in spamreader.__next__():
                                if b in field: 
                                    j=1
                                    while j<7 :
                                        print("caractéristique : ",j)
                                        print(spamreader.__next__())  #affichage des caractéristique
                                        j=j+1
                        except:
                            pass
                        i=i+1
    engine.say("Et voila tes prévisions chakal")
    engine.runAndWait()
   
def reglageauto():    # a finir
    engine.say("Réglage automatique")
    engine.say("La température a été réglée sur")
    cheh=str(temperatureenmemoire)+" degrés"
    engine.say(cheh) 
    engine.say("Dis pas merci chakal ça sert a rien je peut pas te répondre")
    engine.runAndWait()

                           
                    
                        

def tempenmemoire():    #changement de la température favorites
    global temperatureenmemoire
    engine.say("Veuillez saisir la nouvelle température souhaitée")
    engine.runAndWait()
    try :
        temperatureenmemoire = float(input("Nouvelle température : \n"))
        print("Nouvelle température enregistrée : ",temperatureenmemoire,'°C')
    except :
        print("Valeur saisie non valable")
        engine.say("Valeur saisie non valable, je fait exploser ta maison ")
        engine.runAndWait()

def creationbasededonnés():        #web scraping         
    req = requests.get('https://www.meteo60.fr/previsions-meteo-france-paris.html') 
    soup = BeautifulSoup(req.text, "lxml")
    jour =soup.findAll('td', {'class':'jour'})
    with open("info_meteo.csv", 'w', newline=None ) as out_file:
        csv.register_dialect('custom', delimiter=' ',doublequote=True, quoting=csv.QUOTE_NONE, escapechar=' ')
        writer = csv.writer(out_file,'custom')
        informations = soup.find('table', {'class':'previsions'}).findAll('tbody', {'class':'ligne_jour'})
        for informations in informations :
            row = informations.text.strip()
            writer.writerow(row)

#programme principal
creationbasededonnés()
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