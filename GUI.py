import pystray
from PIL import Image


class GUI:
    def __init__(self):
        menus = (
            pystray.MenuItem('退出', self.quit_clicked),
        )
        self.icon = pystray.Icon("icon", Image.open("mouse.ico"), "鼠标定时点击", menus)

    def start(self):
        self.icon.run()

    def quit_clicked(self):
        self.icon.stop()


if __name__ == "__main__":
    gui = GUI()
    gui.start()
