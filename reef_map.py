import folium
import pandas as pd

reef_map=folium.Map(location=[33.7809602, -84.3226822], zoom_start=5, tiles ='Stamen Terrain')

reef_df = pd.read_csv('reef_v2.txt')

for latitude, longitude, region in zip(reef_df['latitude'], reef_df['longitude'], reef_df['region']):
  folium.Marker(location=[latitude, longitude], popup=region, icon=folium.Icon(icon='cloud')).add_to(reef_map)
print(reef_map.save('reef_map.html'))