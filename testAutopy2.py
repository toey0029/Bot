import autopy
screen = autopy.bitmap.capture_screen()
debug = autopy.bitmap.Bitmap.open("bug.png")
pos = screen.find_bitmap(debug)
while True:
    mousePos = autopy.mouse.location()
    #color = screen.get_color(mousePos[0],mousePos[1])
    print(mousePos)

#colorPos = screen.find_color((15198957),0.1)
#print(colorPos)16544278  744.0,396.0     16660747