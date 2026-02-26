
# Libreraias que vamos a usar para este nuevo modelo

import time 
import randomimport tkinder as tk

from pynput import mouse, keyboard
import psutil
import pygetwindow as gw

#Config

Tiempo_Inactivo = 15 #Estos van por segundos
Ultima_Actividad = time.time()
waifu_window = None

#Detector de actividad

def Actividad(*args):
    global Ultima_Actividad
    Ultima_Actividad = time.time()

Mouse.Listener(
    on_move=Actividad,
    on_click=Actividad,
    on_scroll=Actividad
).start()

keyboard.Listener(
    
    on_press=Actividad
).start()


