import folium #converts python to html,css,js

map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles = "Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.2,-99.1], popup="Hi I am a marker",icon=folium.Icon('green'))) 
map.add_child(fg) #add marker to map with popup
map.save("Map1.html")#creates and saves to a html file