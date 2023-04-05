import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json
import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime, timedelta


# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

# Récupération de la clé API depuis les variables d'environnement
api_key = os.getenv("API_KEY")

# #######################################################################
# Liste des villes disponibles dans l'API OpenWeatherMap
villes = ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Lille', 'Rennes', 'Reims', 'Le Havre', 'Saint-Étienne', 'Toulon', 'Grenoble', 'Dijon', 'Angers', 'Nîmes', 'Villeurbanne']
# Initialisation de la liste des informations météorologiques pour chaque ville
infos_meteo = []

# Fonction pour appeler l'API OpenWeatherMap pour une ville donnée
def get_meteo(ville):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = json.loads(response.text)
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_deg = data['wind']['deg']
    sunrise = pd.to_datetime(data['sys']['sunrise'], unit='s').strftime('%H:%M:%S')
    sunset = pd.to_datetime(data['sys']['sunset'], unit='s').strftime('%H:%M:%S')
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    return {
        'Température actuelle': temp,
        'Température ressentie': feels_like,
        'Température minimale': temp_min,
        'Température maximale': temp_max,
        'Pression atmosphérique': pressure,
        'Humidité': humidity,
        'Vitesse du vent': wind_speed,
        'Direction du vent': wind_deg,
        'Lever du soleil': sunrise,
        'Coucher du soleil': sunset,
        'Latitude': lat,
        'Longitude': lon
    }

# Création d'un DataFrame from the weather data
infos_meteo_df = pd.DataFrame(infos_meteo, columns=['Ville', 'Température', 'Température ressentie', 'Température minimale', 'Température maximale', 'Pression atmosphérique', 'Humidité', 'Vitesse du vent', 'Direction du vent', 'Lever du soleil', 'Coucher du soleil','Latitude','Longitude'])
# Boucle pour ajouter les informations de chaque ville au DataFrame
for ville in villes:
    meteo = get_meteo(ville)
    infos_meteo_df = infos_meteo_df.append({'Ville': ville,
                    'Température actuelle': meteo['Température actuelle'],
                    'Température ressentie': meteo['Température ressentie'],
                    'Température minimale': meteo['Température minimale'],
                    'Température maximale': meteo['Température maximale'],
                    'Pression atmosphérique': meteo['Pression atmosphérique'],
                    'Humidité': meteo['Humidité'],
                    'Vitesse du vent': meteo['Vitesse du vent'],
                    'Direction du vent': meteo['Direction du vent'],
                    'Lever du soleil': meteo['Lever du soleil'],
                    'Coucher du soleil': meteo['Coucher du soleil'],
                    'Latitude': meteo['Latitude'],
                    'Longitude': meteo['Longitude']}, ignore_index=True)
# print(infos_meteo_df)

# Exportation du DataFrame dans un fichier CSV
infos_meteo_df.to_csv('informations_meteo.csv', index=False)
# Création de l'interface utilisateur avec Streamlit
st.title("Informations météorologiques")

# Sélection de la ville par l'utilisateur
ville = st.selectbox("Sélectionnez une ville :", villes)

# Récupération des informations météorologiques pour la ville sélectionnée
infos_meteo = get_meteo(ville)

# Affichage des informations météorologiques
for cle, valeur in infos_meteo.items():
    st.write(cle, ":", valeur)
##################################################
m = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Ajouter un marqueur pour chaque ville
for index, row in infos_meteo_df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Ville']).add_to(m)

# Afficher la carte folium dans Streamlit
st_folium(m)
##################################################
