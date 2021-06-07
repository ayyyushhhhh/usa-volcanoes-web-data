
def colorProducer(elevationList:list)->list:
    colorList =[]
    for elevation in elevationList:
        if elevation < 2000 :
            colorList.append("green")
        elif elevation >2000 and elevation<3000:
            colorList.append("orange")
        else:
            colorList.append("red")

    return colorList                
