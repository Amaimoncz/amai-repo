import xbmc
import xbmcgui
import time

dialog = xbmcgui.DialogProgressBG()
dialog.create("Kodi", "Loading widgets & accesories ...")

def update_progress_bar(percent):
    dialog.update(percent, "Starting Kodi...    Please Wait ...")

def main():
    for i in range(0, 101):
        update_progress_bar(i)
        time.sleep(0.20)  # Simulace čekání na načítání

    dialog.close()

if __name__ == "__main__":
    main()
