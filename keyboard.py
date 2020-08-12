import os
from time import sleep
import sys


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./140)
def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')

       
       
os.system("clear")   
os.system("print MR.414N|figlet -f banner|lolcat -a")
os.system("print LOVE|figlet -f banner|lolcat -a ")
os.system("print QueenLia|figlet -m banner|lolcat -a")
os.system("clear")
os.system("print ====================================|lolcat -a")
os.system("print author=MR.414N|lolcat -a")
os.system("print CINTA KU LIA😙😙😙❤️❤️❤️😙😙😙|lolcat -a")
os.system("print WA=082292838634|lolcat -a")
os.system("print TEAM=CYBER CRIMINAL PUBLIC|lolcat -a")
os.system("print ====================================|lolcat -a")

def banner():
    os.system('clear')
    print(a+'sc ini hanya membantu pemula yah😂 yang pro masa nggak bisa buat sendiri'.center(40))
    print(b+'SC keyboard✌️'.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rbentar cok🖕 '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print(c+'Silahkan hubungi '+a+'082292838634'+c+' jika ada yang mau di cerita cerita kek apa kek terkait sc ini')
    print('\033[1;93mterimakasih')

    f=input("\033[1;97m[\033[1;91m?\033[1;97m]Kembali? (y/t): ")
    if f == "y":
       os.system("python keyboard.py")
    else:
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mterimakasih telah menggunakan sc ini\033[1;97m")
