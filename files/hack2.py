import ctypes
import os

class Hack2(object):

    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    def main(self):
        self.image_path1 = os.path.abspath("sprites\\wallpaper\\ghost1.png")
        self.image_path2 = os.path.abspath("sprites\\wallpaper\\ghost2.png")


        ctypes.windll.user32.MessageBoxW(None,"HAHAHHA YOU HAVE BEEN HACKED","ERROR",0)
        ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, ctypes.c_wchar_p(self.image_path1), self.SPIF_UPDATEINIFILE | self.SPIF_SENDWININICHANGE)
        ctypes.windll.user32.MessageBoxW(None,"WANNA SEE MY POWER? HERE YOU GO","ERROR",0)
        ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, ctypes.c_wchar_p(self.image_path2), self.SPIF_UPDATEINIFILE | self.SPIF_SENDWININICHANGE)
