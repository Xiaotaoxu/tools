#########
# author: xutao
# data:2022/4/1
# version:
# version history:
#########

import json
import re
import os
import time


def genrate_log():
    os.system('adb wait-for-device')
    os.system('adb root')
    #id = os.system('adb shell logcat -v threadtime > ./logcat2.txt &')
    #print(os.system('adb shell logcat -v threadtime > ./logcat2.txt &'))
    #print(os.getpid())
    os.system('adb shell setprop persist.bluetooth.btsnooplogmode full')
    os.system('adb shell setprop persist.bluetooth.btsnoopenable true')
    os.system('adb shell svc bluetooth disable')
    os.system('adb shell svc bluetooth enable')
    os.system('adb shell logcat -v threadtime > ./logcat2.txt &')
    #os.system('kill ' + str(os.getpid()))

def load_file():
    i = 0
    dir = os.getcwd()
    print(dir, type(dir))
    fs = open('logcat2.txt', 'rb')
    while True:
        i += 1
        #print(i)
        line = fs.readline()
        if not line:
            break
        else:
            #print(line)
            #line.decode('utf-8')
            strline = str(line)
            blue = re.findall(r'profile started successfully', strline)
            if blue:
                print(strline)


if __name__ == '__main__':
    print("test start------------")
    if os.path.exists("logcat2.txt"):
        print("logcat2.txt already exists, to rm logcat2.txt")
        os.system('rm logcat2.txt')
    genrate_log()
    time.sleep(3)
    load_file()
    print("test end------------")