import os
import wikipedia

calcerror = "wrong input"
osver = "0.0.8 stable (LINUX/UNIX/PY3.6)"
print("Terminal System " + osver)
print("type HELP to get help window")
nfce = "Command error type HELP to get info about commands"
godmode = "false"
username = "root"
hostname = "os0.0.8"

def clearscreen():
    os.system("clear")


def sshconnect(iptossh):
    os.system("ssh " + iptossh)


def installmodule(moduletoinstall):
    os.system("pip3 install " + moduletoinstall)


def extapt(fn12):
    os.system("python3 " + fn12)


def hello():
    print("hello wolrd")

def w3m(url):
    os.system("w3m " + url)
def calcapp():
    print()
    print("Calc.py 0.0.1")
    print()
    print("type e to exit")
    incalc1 = input("calc :")
    if incalc1 == "+":
        calcin1 = input("calc _ + ? :")
        calcin2 = input("calc " + calcin1 + " + _ :")
        calcout1 = int(calcin1) + int(calcin2)
        print(calcout1)
        calcapp()
    elif incalc1 == "-":
        calcin1 = input("calc _ - ? :")
        calcin2 = input("calc " + calcin1 + " - _ :")
        calcout1 = int(calcin1) - int(calcin2)
        print(calcout1)
        calcapp()
    elif incalc1 == "*":
        calcin1 = input("calc _ * ? :")
        calcin2 = input("calc " + calcin1 + " * _ :")
        calcout1 = int(calcin1) * int(calcin2)
        print(calcout1)
        calcapp()
    elif incalc1 == "/":
        calcin1 = input("calc _ / ? :")
        calcin2 = input("calc " + calcin1 + " / _ :")
        calcout1 = int(calcin1) / int(calcin2)
        print(calcout1)
        calcapp()
    elif incalc1 == "e":
        print("exit")
    else:
        print(calcerror)
        calcapp()
def ping(targetping):
    os.system("ping" + targetping)


def wikipediaAPI(wikiinput):
    wp = wikipedia.summary(wikiinput)
    print(wp)


while True:
    getcommand = input(username + " @[" + hostname + " : ")
    if getcommand == "help":
        if godmode == "true":
            print("============== The Help (GODMODE) ==============")
            print(" ")
            print(" HELP - Show to this")
            print(" SETVAR - Set variable to")
            print(" DEVMODE - devmode")
            print(" WRITE - Write to files")
            print(" READ - Read files")
            print(" OSINFO - Info from os")
            print(" LIST - List all files and dirs in folder")
            print(" MDIR  - Make dir")
            print(" RMDIR - Delete dir")
            print(" RMFILE - Delete File")
            print(" REM - Rename File")
            print(" RUN - Run a python 3 file")
            print(" WIKIPEDIA - wikipedia query")
            print(" EXECUTE -  Run linux shell command")
            print(" SOUCRE - Display os soucre")
            print(" INSTALLMOD - Install python3 module")
            print(" LXDE - (UNSTABLE) Start lxde desktop session")
            print(" SSH - Connect to SSH Server")
            print(" TELNET - telnet")
            print(" W3M - Start w3m")
            print(" PING - Ping ip or domain or hostname")
            print(" ")
            print("================================================")

        else:
            print("============== The Help ==============")
            print(" ")
            print(" HELP Show to this")
            print(" SETVAR Set variable to")
            print(" ")
            print("======================================")
    elif getcommand == "setvar":
        setvarinput = input("variable to edit : ")
        if setvarinput == "nfce":
            nfce = input("value : ")
        elif setvarinput == "godmode":
            godmode = input("value : ")
        else:
            print("not found")
    elif getcommand == "write":
        towrite = input("FILE :")
        infowrite = input("DATA :")
        f = open(towrite, 'w')
        f.write(infowrite)
        f.close()
    elif getcommand == "list":
        dirlist = os.listdir()
        print(dirlist)
    elif getcommand == "listdir":
        dirstolist = input("dir : ")
        outfromlist = os.listdir(dirstolist)
        print(outfromlist)
    elif getcommand == "read":
        pathread = input("Filename :")
        readfile = open(pathread, 'r')
        readoutput = readfile.read()
        print(readoutput)
    elif getcommand == "osinfo":
        print("OS info terminal system " + osver + ".")
    elif getcommand == "mdir":
        newdir = input("folder name :")
        os.mkdir(newdir)
    elif getcommand == "rmdir":
        remdir = input("folder name :")
        os.rmdir(remdir)
    elif getcommand == "rmfile":
        filetorm = input("File to remove :")
        os.remove(filetorm)
    elif getcommand == "ren":
        src = input("file : ")
        dst = input("to : ")
        os.rename(src, dst)
    elif getcommand == "programs":
        print("======================================")
        print(" calc.py")
        print(" exit")
        print(" hello.py")
        print("======================================")
        w12 = input("APP : ")
        if w12 == "calc.py":
            print("loading calc.py")
            calcapp()
        elif w12 == "hello.py":
            hello()
        elif w12 == "exit":
            print("closing")
        else:
            print("not found")
    elif getcommand == "run":
        fn11 = input("filename : ")
        extapt(fn11)
    elif getcommand == "wikipedia":
        winput = input("Query type : ")
        if winput == "who is":
            whoisw = input("Who : ")
            wikipediaAPI(whoisw)
        elif winput == "what is":
            whatisw = input("what :")
            wikipediaAPI(whatisw)
        elif winput == "where is":
            whereisw = input("where :")
            wikipediaAPI(whereisw)
        else:
            print("incorrect value")
    elif getcommand == "execute":
        executestring = input("Command :")
        os.system(executestring)
    elif getcommand == "soucre":
        os.system("nano ts007.py")
        print("Closed NANO")
    elif getcommand == "installmod":
        installmodule(input("Module  name : "))
    elif getcommand == "clear":
        clearscreen()
    elif getcommand == "ssh":
        sshconnect(input("Username : ") + '@' + input("IP : ") + " -p " + input("Port : ") + " " + input("Advanced :"))
    elif getcommand == "lxde":
        os.system("exec startlxde")
    elif getcommand == "telnet":
        os.system("telnet")
    elif getcommand == "w3m":
        w3m(input("Url : "))
    elif getcommand == "ping":
        ping(" " + input("Target : "))
    elif getcommand == "devmode":
        godmode = "true"
    else:
        print(nfce)
