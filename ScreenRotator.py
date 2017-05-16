#!/usr/bin/env python3

import os
import signal
from subprocess import call
from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

APPINDICATOR_ID = "screenrotator"
orientation = "normal"

def main():
    indicator = AppIndicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/fabio/.local/share/ScreenRotator/icon.svg'), AppIndicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    Gtk.main()

def build_menu():
    menu = Gtk.Menu()
    #rotate
    item_rotate = Gtk.MenuItem('Rotate')
    item_rotate.connect('activate', rotate_screen)
    menu.append(item_rotate)

    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
#seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)

    #flip
    item_flip = Gtk.MenuItem('Flip')
    item_flip.connect('activate', flip_screen)
    menu.append(item_flip)
   
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
#seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)
    #seperator
    seperator = Gtk.SeparatorMenuItem()
    menu.append(seperator)

    #quit
    item_quit = Gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def rotate_screen(source):
    global orientation
    if orientation == "normal":
        direction = "left"
    elif orientation == "left":
        direction ="normal"
    call(["xrandr", "-o", direction])
    orientation = direction

def flip_screen(source):
    global orientation
    if orientation == "normal":
        direction = "inverted"
        call(["xinput", "float", "13"]) #disabilito la tastiera
    elif orientation == "inverted":
        direction ="normal"
        call(["xinput", "reattach", "13", "3"]) #abilita tastiera
    call(["xrandr", "-o", direction])
    orientation = direction

if __name__ == "__main__":
    #make sure the screen is in normal orientation when the script starts
    call(["xrandr", "-o", orientation])
    #keyboard interrupt handler
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()