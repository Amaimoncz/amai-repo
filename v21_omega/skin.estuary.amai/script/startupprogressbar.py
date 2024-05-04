import xbmc
import xbmcgui
import time
import sys


dialog = xbmcgui.DialogProgressBG()
dialog.create("Kodi", "Loading widgets & accesories ...")

# set delay time from argument
delayTime = int(sys.argv[1])

# progres bar function
def update_progress_bar(percent):
    dialog.update(percent, "Starting Kodi...    Please Wait ...")

def main():
    for i in range(0, 101):
        update_progress_bar(i)
        time.sleep(delayTime / 100)  # delay time for start kodi

    dialog.close()

if __name__ == "__main__":
    main()
