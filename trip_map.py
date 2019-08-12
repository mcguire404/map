import folium
map1 = folium.Map(location =[33.7809602, -84.3226822], zoom_start=5, tiles='Stamen Terrain')

folium.Marker(location=[33.7809602, -84.3226822], popup='Home', icon=folium.Icon(icon='cloud')).add_to(map1)

folium.Marker(location=[41.245900, -75.881300], popup='Family', icon=folium.Icon(color='green')).add_to(map1)

folium.PolyLine(locations = [(33.7809602, -84.3226822), (41.245900, -75.881300)], line_opacity = 0.5).add_to(map1)

print(map1.save('trip_map.html'))