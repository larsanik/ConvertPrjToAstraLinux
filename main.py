# This is converter TWindow to TGraphicsComposite for files IEC HMI SCADA Sonata.

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
            file_name = current_dir.name
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
