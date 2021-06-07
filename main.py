import folium
import pandas


listLongitudes = []
listLatitudes = []
nameOfVolcanoes = []
def getVolcanoesData():
    volcanoesData= pandas.read_csv("Volcanoes.txt")
    global listLatitudes
    global listLongitudes
    global nameOfVolcanoes
    listLongitudes = volcanoesData["LON"]
    listLatitudes = volcanoesData["LAT"]
    nameOfVolcanoes = volcanoesData["NAME"]
    

def makeMap():
    # folium.Map creates a map of the desired co-ordiantes passes as a arument in location parameter 
    # folimn.Map has a tiles parameter where we can set the type of base map for our project.
    # folium.Map has a zoom_start paramter that will allow you to set the initial zoom amount by default it is set to 10
    locationMap = folium.Map(location=[34.155834,-119],tiles="Stamen Terrain",zoom_start=6)
   
    # feature group
    # FeatureGroup is a layer on the map ;where you can put things in it and handle them
    # as a single layer. We have to provide a name to the feature group
    fg = folium.FeatureGroup(name="volcanoes")
    # add item to the featuregroup
    for lat,lon,name in zip(listLatitudes,listLongitudes,nameOfVolcanoes):
        fg.add_child(folium.Marker(location=[lat,lon],popup=f"{name}",icon=folium.Icon(color="green")))
    locationMap.add_child(fg)

    # after generating the map we have to save the map that we can do with save function that takes a name of html file.
    locationMap.save("delhi.html")



getVolcanoesData() 
makeMap()  