
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


#APP ACTIVA

def get_active_window():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title.lower()
    except:
        return ""
    return ""


#Bot wiafu personalizado

def waifu_comment(context):
    context = context.lower()

    if "youtube" in context:
        return random.choice([
            "¿Otro videíto? dizque 5 minutos y llevas media hora jsjsjs xd",
            "Eso no era lo que ibas a hacer, pero bueno... :v",
            "Dale pues, 'solo uno más' y te creo ",
            "Uy no nea, ese algoritmo ya te tiene secuestrado JAJA"
        ])

    if "steam" in context:
        return random.choice([
            "¿Otro juego? pero si tienes como 40 sin instalar jsadjsa",
            "En oferta todo suena buena idea, luego lloras :v",
            "Comprando felicidad digital otra vez  xd",
            "Ese backlog ya está pidiendo auxilio JAJA"
        ])

    if "visual studio" in context or "pycharm" in context:
        return random.choice([
            "Esooo, modo ingeniero activado pues ",
            "Ah bueno, ahora sí estamos facturando conocimiento 😌",
            "Programando o peleando con el bug? jsjs",
            "Uy qué pro, me siento orgullosa la buena"
        ])

    if "chrome" in context:
        return random.choice([
            "¿Cuántas pestañas tienes abiertas? 38? JAJA",
            "Tu RAM está diciendo 'ya no más mi rey' 😭",
            "Eso ya parece mercado persa de pestañas abiertas xd",
            "Investigando o procrastinando elegante? :v"
        ])

    if "whatsapp" in context:
        return random.choice([
            "¿Chisme nuevo o qué? ",
            "Eso suena a conversación importante... o puro meme jsjs",
            "Responde rápido que luego te dicen seco 😭"
        ])

    return random.choice([
        "Te quedaste mirando fijo... todo bien? xd",
        "Modo NPC activado por 15 segundos JAJA",
        "Descansito mental, válido la verdad ",
        "¿Pensando en la vida o en comida? porque same",
        "Yo aquí existiendo y tú quieto jsjsjs"
    ])
        