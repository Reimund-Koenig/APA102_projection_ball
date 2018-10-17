# thread 1 MQTT
    # callback from MQTT
    # change parameter

# thread 2

frontMatrix = [180][77]
backgroundMatrix = [180][77]

def calcBackgroundLayer():
    #show Background Layer
    if modus=="line":
        # show calibration line
    elif modus=="disco":
        # show random lights
    elif modus=="picture":
        # show picture
        #
    elif modus=="solid":
        # show one solid color
    elif modus=="fade2":
        # fade with 2 colors    
    elif modus=="fade3":
        # fade with 3 colors
    
def calcFrontLayer():
    #show Front Layer
    if info=="off":
        #front.settext("",color)
    elif info=="time":
        #front.settime(color)
    elif info=="date":
        #front.setdate(color)
    elif info=="datetime":
        #front.setdatetime(color)
    elif info=="text":
        #front.settext(msg,color)
    
    #rotate(degree)
if layer=="0":
    print("Alles ausschalten")
elif layer=="1":
    calcBackgroundLayer()
elif layer=="2":
    calcFrontLayer()
elif layer=="1_2":
    calcFrontLayer()
    calcBackgroundLayer()
