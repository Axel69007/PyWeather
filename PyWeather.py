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



#initialisation variable
ville=""

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

bouton_voir = Button(master= boite_bouton, text="Voir la météo",font="Helvetica 12",command=resquest_weather , width = 20)
bouton_voir.pack(pady= 5)

bouton_quitter = Button(boite_bouton, text="Quitter programe",font="Helvetica 12" ,command=quitter_programme , width = 20)
bouton_quitter.pack(pady= 5)

boite_titre.pack(side=TOP)
boite_bouton.pack()
boite_bottom.pack(side=BOTTOM, pady = 30)

#main code

#https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

root.mainloop()



