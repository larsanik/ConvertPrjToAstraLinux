# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import easygui
import io

def open_file():
    return easygui.fileopenbox()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('Sonata')
    #lnk=open_file()
    #print(lnk)
    f = open("G:\Projects\!ConvertPrjToAstraLinux\Design\AT_BWDCAP6QG42EZAS4IIRAMDJDBU.iec_hmi", "wt")
    print(f)
    #for line in f:
    #    f.write(line.replace('WindowFBType', 'GraphicsCompositeFBType'))
    f.close()
    #easygui.egdemo()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
