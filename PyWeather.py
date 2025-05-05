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
from datetime import datetime
from tkinter import PhotoImage


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
    global heure_couche_soleil
    global heure_leve_soleil
    with open("weather.json", "r") as fichier_json:
        donnees = json.load(fichier_json)
    temperature = donnees["main"]["temp"]
    temperature_min = donnees["main"]["temp_min"]
    temperature_max = donnees["main"]["temp_max"]
    humidite = donnees["main"]["humidity"]
    meteo = donnees["weather"][0]["description"]
    vent = donnees["wind"]["speed"]
    direction_vent = donnees["wind"]["deg"]
    raw_couche_soleil = donnees["sys"]["sunset"]
    raw_leve_soleil = donnees["sys"]["sunrise"]
    couche_soleil= datetime.fromtimestamp(raw_couche_soleil)
    leve_soleil = datetime.fromtimestamp(raw_leve_soleil)
    heure_couche_soleil = couche_soleil.strftime("%X")
    heure_leve_soleil = leve_soleil.strftime("%X")
    return temperature, temperature_min, temperature_max, humidite, meteo, vent, direction_vent, heure_couche_soleil, heure_leve_soleil


def affichage_meteo():
    def choix_image():
        global image_clear_sky
        global image_few_clouds
        global image_overcast_clouds
        global image_drizzle
        global image_rain
        global image_shower_rain
        global image_thunderstorm
        global image_snow
        global image_mist
        global meteo
        choix=str(meteo)
        match choix:
            case "clear sky":
                label_image_meteo.config(image=image_clear_sky)

            case "few clouds":
                label_image_meteo.config(image=image_few_clouds)

            case"overcast clouds":
                label_image_meteo.config(image=image_overcast_clouds)

            case"drizzle":
                label_image_meteo.config(image=image_drizzle)

            case"rain":
                label_image_meteo.config(image=image_rain)

            case"shower rain":
                label_image_meteo.config(image=image_shower_rain)

            case"thunderstorm":
                label_image_meteo.config(image=image_thunderstorm)

            case"snow":
                label_image_meteo.config(image=image_snow)

            case"mist":
                label_image_meteo.config(image=image_mist)

            case _:
                label_image_meteo.config(text="Image non trouvé")
    resquest_weather()
    lecture_json()
    top_fenetre = Toplevel(root)
    top_fenetre.minsize(400, 250)
    top_fenetre.columnconfigure((0,1),weight =1,uniform='a')
    top_fenetre.rowconfigure((0,1,2,3,4,5,6,7,8),weight =1,uniform='a')
    label_image_meteo = Label(master = top_fenetre, text ="")
    label_image_meteo.grid(row = 0,column = 1,rowspan=9)
    choix_image()
    label_meteo = Label(master = top_fenetre, text="La météo est " + str(meteo), font="Helvetica 12 ")
    label_meteo.grid(row = 0,column = 0)
    label_temperature = Label(master = top_fenetre, text="La tempétature est de "+ str(temperature)+" °C", font="Helvetica 12 ")
    label_temperature.grid(row = 1,column = 0)
    label_temperature_min = Label(master = top_fenetre, text="La tempétature minimal sera de : "+ str(temperature_min)+" °C", font="Helvetica 12 ")
    label_temperature_min.grid(row = 2,column = 0)
    label_temperature_max = Label(master = top_fenetre, text="La tempétature maximal sera de : "+ str(temperature_max)+" °C", font="Helvetica 12 ")
    label_temperature_max.grid(row = 3,column = 0)
    label_humidite = Label(master = top_fenetre, text="L'humidité est de : "+ str(humidite) +"%", font="Helvetica 12 ")
    label_humidite.grid(row = 4,column = 0)
    label_vent = Label(master = top_fenetre, text="Le vent de : "+ str(vent) +"KM/h", font="Helvetica 12 ")
    label_vent.grid(row = 5,column = 0)
    label_direction_vent = Label(master = top_fenetre, text="La direction du vent est de : "+ str(direction_vent) +"°" , font="Helvetica 12 ")
    label_direction_vent.grid(row = 6,column = 0)
    label_leve_soleil = Label(master = top_fenetre, text="Le soleil se lève à "+ str(heure_leve_soleil) , font="Helvetica 12 ")
    label_leve_soleil.grid(row = 7,column = 0)
    label_couche_soleil = Label(master = top_fenetre, text="Le soleil se couche à  "+ str(heure_couche_soleil) , font="Helvetica 12 ")
    label_couche_soleil.grid(row = 8,column = 0)



#initialisation variable global
ville=""
temperature = ""
temperature_min = ""
temperature_max = ""
humidite = ""
meteo = ""
vent = ""
direction_vent = ""
heure_couche_soleil = ""
heure_leve_soleil = ""


#Interface graphique
root = tk.Tk()
root.title("PyWeather")
root.minsize(250, 250)
root.iconbitmap("png/PyWeather_icon.ico")

#déclaration image
image_clear_sky= PhotoImage(file="png/hot_sun_weather_icon.png")
image_few_clouds= PhotoImage(file="png/cloud_cloudy_sun_sunny_weather_icon.png")
image_overcast_clouds= PhotoImage(file="png/cloud_weather_icon.png")
image_drizzle= PhotoImage(file="png/cloud_drizzle_rain_weather_icon.png")
image_rain= PhotoImage(file="png/cloud_rain_weather_icon.png")
image_shower_rain= PhotoImage(file="png/cloud_heavy rain_rain_weather_icon.png")
image_thunderstorm= PhotoImage(file="png/cloud_heavy rain_rain_storm_thunderbolt_icon.png")
image_snow= PhotoImage(file="png/cloud_cold_weather_winter_icon.png")
image_mist= PhotoImage(file="png/cloud_foggy_weather_cloudy_forecast_icon.png")

#Grid
root.columnconfigure((0),weight =1,uniform='a')
root.rowconfigure((0,1,2,3,4,5,6,7),weight =1,uniform='a')

label_bienvenue = Label(master= root, text="Bienvenue dans PyWeather ", font="Helvetica 18 bold")
label_bienvenue.grid(row = 0,column = 0, sticky="n")

image_main = PhotoImage(file="png/weather_icon.png")
label_image = Label(master = root, image= image_main)
label_image.grid(row = 1,column = 0,sticky="nwse")

label_nomville = Label(master = root, text="Le nom de votre ville est : "+ str(ville), font="Helvetica 12 ")
label_nomville.grid(row = 6,column = 0, sticky="n")

bouton_ajouter = Button(master= root, text="Ajoutez le nom de la ville", font="Helvetica 12" ,command=ajout_ville , width = 20)
bouton_ajouter.grid(row = 3,column = 0, sticky="n")

bouton_voir = Button(master= root, text="Voir la météo",font="Helvetica 12",command=affichage_meteo , width = 20)
bouton_voir.grid(row = 4,column = 0, sticky="n")

bouton_quitter = Button(root, text="Quitter",font="Helvetica 12" ,command=quitter_programme)
bouton_quitter.grid(row = 7,column = 0, sticky="n")


#Mainloop
root.mainloop()



