import folium
import pandas as pd

map4=folium.Map(location = [33.7809602, -84.3226822], zoom_start=5, tiles='Stamen Terrain')

df = pd.read_csv('Volcano.txt')

for latitude, longitude, v_name in zip(df['Latitude'], df['Longitude'], df['V_Name']):
  folium.Marker(location=[latitude,longitude], popup = v_name, icon=folium.Icon(icon='cloud')).add_to(map4)

print(map4.save('Vmap.html'))