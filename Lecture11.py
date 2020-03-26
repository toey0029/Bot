import autopy
import time
def findGameArea():
    for i in range(50):
        screen = autopy.bitmap.capture_screen()
        s = autopy.bitmap.Bitmap.open("GameArea.png")
        gamePos = screen.find_bitmap(s)
        if gamePos:
            print("found game area at",gamePos)
            return gamePos
        else:
            print("cannot find game area" + (i+1) + "/50")
    exit()

def grabAndSave(gamePos):
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    autopy.mouse.move(gamePos[0]+625,gamePos[1]+147)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)
    #time.sleep(0.5)
def findfish(gamePos):
    screen = autopy.bitmap.capture_screen()
    fishPos = screen.find_color((16660747),0.05,((gamePos[0]+19,gamePos[1]+140),(431,257)))
    if not fishPos:
        fishPos = screen.find_color((16544278),0.05,((gamePos[0]+19,gamePos[1]+140),(431,257)))
    print("fish at :" + str(fishPos))
    if fishPos:
        autopy.mouse.move(fishPos[0]+20,fishPos[1])
        grabAndSave(gamePos)
        return True
    else:
        return False

def endGame(gamePos):
    screen = autopy.bitmap.capture_screen()
    ok = autopy.bitmap.Bitmap.open("endGame.png")
    okPos = screen.find_bitmap(ok,0.05,((gamePos[0]+19,gamePos[1]+140),(289,734)))
    if okPos:
        print("Game Over")
        exit()

def startGame():
    gamePos = findGameArea()
    count = 1
    while True:
        if findfish(gamePos):
            count = 1
        else:
            count += 1
            if count >= 50:
                endGame(gamePos)
                count = 1
        
startGame()
