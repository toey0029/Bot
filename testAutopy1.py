import autopy

screen = autopy.bitmap.capture_screen()
debug = autopy.bitmap.Bitmap.open("bug.png")
pos = screen.find_bitmap(debug)
if pos:
    autopy.mouse.smooth_move(pos[0],pos[1])
    autopy.mouse.click()
else:
    print("cannot File bitmap")