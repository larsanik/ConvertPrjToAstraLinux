# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import easygui
#import io
from pathlib import *

def open_file():
    return easygui.fileopenbox()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if easygui.ccbox("Выбрать файл IEC HMI и заменить TWindow на TGraphicsComposite?",
                  "ConvertPrjToAstraLinux",
                  ("Продолжить", "Выход")):
        lnk=open_file()
        if lnk != None:
            current_dir = PureWindowsPath(lnk)
            bak = str(current_dir.parents[0]) + "\\tmp.bak"
            f = open(lnk, "r")
            t = open(bak, "w")
        #print(f)
            for line in f:
                t.write(line.replace('WindowFBType', 'GraphicsCompositeFBType'))
                #print(line)
            f.close()
            t.close()

            easygui.msgbox("Задача завершена", "ConvertProjToAstra", "Выход")
        #easygui.egdemo()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
