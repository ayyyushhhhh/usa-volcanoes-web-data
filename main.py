import folium
import pandas
import color_producer

listLongitudes = []
listLatitudes = []
nameOfVolcanoes = []
elevationOfVolcanoes = []
colorsList = []
def getVolcanoesData():
    volcanoesData= pandas.read_csv("Volcanoes.txt")

    global listLatitudes
    global listLongitudes
    global nameOfVolcanoes
    global colorsList
    global elevationOfVolcanoes

    listLongitudes = volcanoesData["LON"]
    listLatitudes = volcanoesData["LAT"]
    nameOfVolcanoes = volcanoesData["NAME"]
    elevationOfVolcanoes = volcanoesData["ELEV"]
    colorsList = color_producer.colorProducer(elevationList=elevationOfVolcanoes)
    

def makeMap():
    getVolcanoesData()

    # folium.Map creates a map of the desired co-ordiantes passes as a arument in location parameter 
    # folimn.Map has a tiles parameter where we can set the type of base map for our project.
    # folium.Map has a zoom_start paramter that will allow you to set the initial zoom amount by default it is set to 10
    locationMap = folium.Map(location=[34.155834,-119],tiles="Stamen Terrain",zoom_start=6)
   
    # feature group
    # FeatureGroup is a layer on the map ;where you can put things in it and handle them
    # as a single layer. We have to provide a name to the feature group
    fgVolcanoes = folium.FeatureGroup(name="volcanoes")
    fbPop = folium.FeatureGroup(name="population")
    # add item to the featuregroup
    for lat,lon,name,col,ele in zip(listLatitudes,listLongitudes,nameOfVolcanoes,colorsList,elevationOfVolcanoes):
        fgVolcanoes.add_child(folium.CircleMarker(location=[lat,lon],
                            popup=f"{name} \n {ele} m",
                            radius=7,
                            fill = True ,
                            fill_color=col,
                            color = 'black'))
    fbPop.add_child(folium.GeoJson(
        data=open("world.json",'r',encoding="utf-8-sig").read(),
        style_function= lambda x: {"fill_color":"yellow" 
        if x['properties']['POP2005'] < 10000000 else "orange"
        }
    ))
    locationMap.add_child(fgVolcanoes)
    locationMap.add_child(fbPop)
    locationMap.add_child(folium.LayerControl())

    # after generating the map we have to save the map that we can do with save function that takes a name of html file.
    locationMap.save("volcanoes.html")




makeMap()  