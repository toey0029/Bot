import autopy
def grabAndSave():
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    autopy.mouse.move(744,396)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)
def findfish():
    screen = autopy.bitmap.capture_screen()
    fishPos = screen.find_color((16544278),0.05)
    print("fish at :" + str(fishPos))
    if fishPos:
        autopy.mouse.move(fishPos[0],fishPos[1])
        grabAndSave()
while True:
    findfish()