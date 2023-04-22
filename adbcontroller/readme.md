# adbcontroller.py
Use it by doing `import adbcontroller` while it's in the same folder.

## connect(port=input("What port is adb running on? "))
Connects to adb using given port.

## take_screenshot(name='screenshot')
Takes screenshot then transfers it to the given location.

## write_to_console(command)
Uses subprocess.run() to run any command given a string.

## find_image(image_to_recognize, location='screenshot.png')
Uses the cv2 and numpy library to recognize the first argument, on screenshot.png if location is not given.
The folder the image_to_recognize needs to be in is the recognition folder that's in the same directory as the script.

## swipe(args) text(args) tap(args) keycode(args)
Just runs `adb shell input {function_name} {args}`.
Intended to only be used by adbcreator.py.

# adbcreator.py
the ui is crap lol.
dont put any arguments its probably gonna brick it, as its still being worked on. ui should explain it well.
updates when screenshot.png updates in the same folder.
im really sorry for this shitty description of it but i have no attention span so i just stopped working on this after 10 minutes
