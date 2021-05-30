import os
from time import sleep
import sys
from sys import platform
import subprocess
import platform 





#Main Service Initalizations

#def upcred():

#def multirep():

def clonehistory():
        print(">>>>>>>> History >>>>>>>>")
        print("    repositories cloned")
        print(">>>>>>>>>  ----- >>>>>>>>")


        gethist =  open('reposnit.txt', 'r')

        print(gethist.read())

        sleep(5)
        
        gbck = input("Menu (0) :  ")

        if gbck == "0":
                mainlaunch()
                mainopt()
        elif gbck == "":
                print("Invalid Option ..... exiting")


def fetchrep():

        print("Github / Gitlab repository")
        grep = input("> ")
        with open('reposnit.txt', 'w') as f:
                f.write(grep)
        runsys = os.system("git clone " + grep)
        print(runsys)

        print(" >>>>>>>>>>>>>> ----- >>>>>>>>>>>>>")
        sleep (5)

        gmenu = input("Menu (0):  ")
        if gmenu == "0":
                mainlaunch()
                mainopt()
        elif gmenu == "":
                print("Invalid Option.... Exiting")
def sclear():
        sysproc = sys.platform
        if  sysproc == ['linux2', 'linux']:
                _ = os.system("clear")
        elif sysproc == ['Windows', 'win64']:
               _= os.system("cls")



#Main screen

sclear()

def mainlaunch(): 
        printmain = print("""


        
  ________.____________________________.___.
 /  _____/|   \__    ___/   _____/\__  |   |
/   \  ___|   | |    |  \_____  \  /   |   |
\    \_\  \   | |    |  /        \ \____   |
 \______  /___| |____| /_______  / / ______|
        \/                     \/  \/       



(1) ---> Clone Repository 

(2) ---> Clone History 

(3) ---> Multiple Repos 

(4)  --> Update & Credits

(5) ---> Exit Program

(6) ---> Get Resources

""")
mainlaunch()

def mainopt():
        uoption = input("Option: ")
        if uoption == "1":
                sclear()
                print("We are working on it.....")
                sleep(2)
                fetchrep()
        elif uoption == "2":
                print("We are working on it.....")
                sleep(2)
                sclear()
                clonehistory()
        elif uoption == "4":
                sclear()
                print("We are working on it.....")
                sleep(2)
                #  multirep()
        elif uoption == "4":
                print("We are working on it.....")
                sleep(2)
        
        elif uoption == "5":
                try:
                        print("Exiting....")
                except:
                        os.system(exit)

mainopt()

