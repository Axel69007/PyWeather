#PyWeather V1
#Axel69007
#MIT Licence

from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
import tkinter as tk
import os
import requests
import json

#Déclaration variable
def quitter_programme():
    root.destroy()

def final_url():
    global ville
    def lecture_api():
        with open("api.tmp") as fichier_api:
            raw_api_key=str((fichier_api.read()))
            return raw_api_key
    api_key = lecture_api()
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    ville_url="q="+ ville
    units_url="&units=metric"
    full_url= base_url + ville_url + units_url + "&appid=" + api_key
    return full_url

def resquest_weather():
    raw_weather_data = requests.get(final_url()).json()
    weather_data = str(raw_weather_data)
    with open("weather.json","w") as fichier_weather:
        json.dump(raw_weather_data, fichier_weather, indent=4, sort_keys=True)

def ajout_ville():
    global ville
    demande = simpledialog.askstring("Ajout du nom de la ville","Entrez le nom de la ville : ")
    if demande:
        ville = str(demande)
        label_nomville.config(text="Le nom de votre ville est : " + ville)
    return ville


def lecture_json():
    global temperature
    global temperature_min
    global temperature_max
    global humidite
    global meteo
    global vent 
    global direction_vent 
    global couche_soleil
    global leve_soleil
    with open("weather.json", "r") as fichier_json:
        donnees = json.load(fichier_json)
    temperature = donnees["main"]["temp"]
    temperature_min = donnees["main"]["temp_min"]
    temperature_max = donnees["main"]["temp_max"]
    humidite = donnees["main"]["humidity"]
    meteo = donnees["weather"][0]["description"]
    vent = donnees["wind"]["speed"]
    direction_vent = donnees["wind"]["deg"]
    couche_soleil = donnees["sys"]["sunset"]
    leve_soleil = donnees["sys"]["sunrise"]
    return temperature, temperature_min, temperature_max, humidite, meteo, vent, direction_vent, couche_soleil, leve_soleil

def affichage_meteo():
    resquest_weather()
    lecture_json()
    top_fenetre = Toplevel(root)
    top_fenetre.minsize(300, 250)
    label_meteo = Label(master = top_fenetre, text="La météo est " + str(meteo), font="Helvetica 12 ")
    label_meteo.pack()
    label_temperature = Label(master = top_fenetre, text="La tempétature est de "+ str(temperature), font="Helvetica 12 ")
    label_temperature.pack()
    label_temperature_min = Label(master = top_fenetre, text="La tempétature minimal sera de : "+ str(temperature_min), font="Helvetica 12 ")
    label_temperature_min.pack()
    label_temperature_max = Label(master = top_fenetre, text="La tempétature maximal sera de : "+ str(temperature_max), font="Helvetica 12 ")
    label_temperature_max.pack()
    label_humidite = Label(master = top_fenetre, text="L'humidité est de' : "+ str(humidite) +"%", font="Helvetica 12 ")
    label_humidite.pack()
    label_vent = Label(master = top_fenetre, text="Le vent de : "+ str(vent) +"KMH", font="Helvetica 12 ")
    label_vent.pack()
    label_direction_vent = Label(master = top_fenetre, text="La direction du vent est : "+ str(direction_vent) , font="Helvetica 12 ")
    label_direction_vent.pack()
    label_leve_soleil = Label(master = top_fenetre, text="Le soleil se lève à "+ str(leve_soleil) , font="Helvetica 12 ")
    label_leve_soleil.pack()
    label_couche_soleil = Label(master = top_fenetre, text="Le soleil se couche à : "+ str(couche_soleil) , font="Helvetica 12 ")
    label_couche_soleil.pack()

#initialisation variable global
ville=""
temperature = ""
temperature_min = ""
temperature_max = ""
humidite = ""
meteo = ""
vent = ""
direction_vent = ""
couche_soleil = ""
leve_soleil = ""


#Interface graphique
root = tk.Tk()
root.title("PyWeather")
root.minsize(500, 500)

boite_titre = Frame(root)
boite_bouton = Frame(root)
boite_bottom = Frame(root)

label_bienvenue = Label(master= boite_titre, text="Bienvenue dans PyWeather ", font="Helvetica 18 bold")
label_bienvenue.pack(pady= 15)

label_nomville = Label(master = boite_bottom, text="Le nom de votre ville est : "+ str(ville), font="Helvetica 12 ")
label_nomville.pack()

bouton_ajouter = Button(master= boite_bouton, text="Ajoutez le nom de la ville", font="Helvetica 12" ,command=ajout_ville , width = 20)
bouton_ajouter.pack(pady= 5)

bouton_voir = Button(master= boite_bouton, text="Voir la météo",font="Helvetica 12",command=affichage_meteo , width = 20)
bouton_voir.pack(pady= 5)

bouton_quitter = Button(boite_bouton, text="Quitter programe",font="Helvetica 12" ,command=quitter_programme , width = 20)
bouton_quitter.pack(pady= 5)

boite_titre.pack(side=TOP)
boite_bouton.pack()
boite_bottom.pack(side=BOTTOM, pady = 30)

#Mainloop
root.mainloop()



