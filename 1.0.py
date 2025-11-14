from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import requests
import os
import time
import signal
import psutil

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("zapret-check")
frm.grid()

otvet = None  

def close_application(app_name):
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] == app_name:
            proc.terminate()
            print(f"Закрыто приложение: {app_name}")

def select():
    folder_path = filedialog.askdirectory(title="Выберите папку с zapret")
    if folder_path: 
        print(folder_path)
        check(folder_path)

def check_connect():
    global otvet  
    try:
        r = requests.get("https://discord.com", timeout=2)
        if r.status_code == 200:
            otvet = r.status_code
            close_application("cmd.exe")
        else:
            otvet = r.status_code
            close_application("cmd.exe")
    except Exception as e:
        otvet = f"Ошибка: {e}" 
        close_application("cmd.exe")
        close_application("winws.exe")
          
    print(otvet)
    

def check(folder_path):
    close_application("winws.exe")
    os.startfile(os.path.join(folder_path, "general.bat"))
    print("Ожидание открытия winws.exe...")
    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
        time.sleep(0)
    check_connect() 

    if otvet == 200:
        ttk.Label(frm, text=("Работает general.bat")).grid(column=0, row=0)
        close_application("cmd.exe")
    else:
        os.startfile(os.path.join(folder_path, "general (ALT).bat"))
        print("Ожидание открытия winws.exe...")
    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
        time.sleep(0)
        check_connect()
        if otvet == 200:
            ttk.Label(frm, text=("Работает general (ALT).bat")).grid(column=0, row=0)
            close_application("cmd.exe")
        else:
            os.startfile(os.path.join(folder_path, "general (ALT2).bat"))
            print("Ожидание открытия winws.exe...")
        while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
            time.sleep(0)
            check_connect()
            if otvet == 200:
                ttk.Label(frm, text=("Работает general (ALT2).bat")).grid(column=0, row=0)
                close_application("cmd.exe")
            else:
                    os.startfile(os.path.join(folder_path, "general (ALT3).bat"))
                    print("Ожидание открытия winws.exe...")
                    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                        time.sleep(0)
                    check_connect()
                    if otvet == 200:
                        ttk.Label(frm, text=("Работает general (ALT3).bat")).grid(column=0, row=0)
                        close_application("cmd.exe")
                    else:
                            os.startfile(os.path.join(folder_path, "general (ALT4).bat"))
                            print("Ожидание открытия winws.exe...")
                            while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                time.sleep(0)
                            check_connect()
                            if otvet == 200:
                                ttk.Label(frm, text=("Работает general (ALT4).bat")).grid(column=0, row=0)
                                close_application("cmd.exe")
                            else:
                                    os.startfile(os.path.join(folder_path, "general (ALT5).bat"))
                                    print("Ожидание открытия winws.exe...")
                                    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                        time.sleep(0)
                                    check_connect()
                                    if otvet == 200:
                                        ttk.Label(frm, text=("Работает general (ALT5).bat")).grid(column=0, row=0)
                                        close_application("cmd.exe")
                                    else:
                                        os.startfile(os.path.join(folder_path, "general (ALT6).bat"))
                                        print("Ожидание открытия winws.exe...")
                                        while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                            time.sleep(0)
                                        check_connect()
                                        if otvet == 200:
                                            ttk.Label(frm, text=("Работает general (ALT6).bat")).grid(column=0, row=0)
                                            close_application("cmd.exe")
                                            
                                        else:
                                            os.startfile(os.path.join(folder_path, "general (ALT7).bat"))
                                            print("Ожидание открытия winws.exe...")
                                            while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                time.sleep(0)
                                            check_connect()
                                            if otvet == 200:
                                                ttk.Label(frm, text=("Работает general (ALT7).bat")).grid(column=0, row=0)
                                                close_application("cmd.exe")
                                            else:
                                                    os.startfile(os.path.join(folder_path, "general (ALT8).bat"))
                                                    print("Ожидание открытия winws.exe...")
                                                    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                        time.sleep(0)
                                                    check_connect()
                                                    if otvet == 200:
                                                        ttk.Label(frm, text=("Работает general (ALT8).bat")).grid(column=0, row=0)
                                                        close_application("cmd.exe")
                                                    else:
                                                        os.startfile(os.path.join(folder_path, "general (FAKE TLS AUTO).bat"))
                                                        print("Ожидание открытия winws.exe...")
                                                        while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                            time.sleep(0)
                                                        check_connect()
                                                        if otvet == 200:
                                                            ttk.Label(frm, text=("Работает general (FAKE TLS AUTO).bat")).grid(column=0, row=0)
                                                            close_application("cmd.exe")
                                                        else:
                                                            os.startfile(os.path.join(folder_path, "general (FAKE TLS AUTO ALT).bat"))
                                                            print("Ожидание открытия winws.exe...")
                                                            while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                                time.sleep(0)
                                                            check_connect()
                                                            if otvet == 200:
                                                                ttk.Label(frm, text=("Работает general (FAKE TLS AUTO ALT).bat")).grid(column=0, row=0)
                                                                close_application("cmd.exe")
                                                            else:
                                                                os.startfile(os.path.join(folder_path, "general (FAKE TLS AUTO ALT2).bat"))
                                                                print("Ожидание открытия winws.exe...")
                                                                while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                                    time.sleep(0)
                                                                check_connect()
                                                                if otvet == 200:
                                                                    ttk.Label(frm, text=("Работает general (FAKE TLS AUTO ALT2).bat")).grid(column=0, row=0)
                                                                    close_application("cmd.exe")
                                                                else:
                                                                    os.startfile(os.path.join(folder_path, "general (FAKE TLS AUTO ALT3).bat"))
                                                                    print("Ожидание открытия winws.exe...")
                                                                    while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                                        time.sleep(0)
                                                                    check_connect()
                                                                    if otvet == 200:
                                                                        ttk.Label(frm, text=("Работает general (FAKE TLS AUTO ALT3).bat")).grid(column=0, row=0)
                                                                        close_application("cmd.exe")
                                                                    else:
                                                                        os.startfile(os.path.join(folder_path, "general (SIMPLE FAKE).bat"))
                                                                        print("Ожидание открытия winws.exe...")
                                                                        while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                                            time.sleep(0)
                                                                        check_connect()
                                                                        if otvet == 200:
                                                                            ttk.Label(frm, text=("Работает general (SIMPLE FAKE).bat")).grid(column=0, row=0)
                                                                            close_application("cmd.exe")
                                                                        else:
                                                                            os.startfile(os.path.join(folder_path, "general (SIMPLE FAKE ALT).bat"))
                                                                            print("Ожидание открытия winws.exe...")
                                                                            while not any(proc.info['name'] == "winws.exe" for proc in psutil.process_iter(attrs=['name'])):
                                                                                time.sleep(0)
                                                                            check_connect()
                                                                            if otvet == 200:
                                                                                ttk.Label(frm, text=("Работает general (SIMPLE FAKE ALT).bat")).grid(column=0, row=0)
                                                                                close_application("cmd.exe")


ttk.Button(frm, text="Начать проверку", command=select).grid(column=1, row=0)
ttk.Button(frm, text="Выйти", command=root.destroy).grid(column=2, row=0)

root.mainloop()
