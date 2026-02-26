
# Libreraias que vamos a usar para este nuevo modelo
#C:/Users/Administrador/AppData/Local/Programs/Python/Python312/python.exe -m pip install pygetwindow pillow


import time
import random
import tkinter as tk
from pynput import mouse, keyboard
import psutil
import pygetwindow as gw
#Config

INACTIVITY_TIME = 15  # segundos
last_activity = time.time()
waifu_window = None

#Detector de actividad

def update_activity(*args):
    global last_activity
    last_activity = time.time()

mouse.Listener(
    on_move=update_activity,
    on_click=update_activity,
    on_scroll=update_activity
).start()

keyboard.Listener(
    on_press=update_activity
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
def show_waifu(message):
    global waifu_window

    if waifu_window is not None:
        return

    waifu_window = tk.Tk()
    waifu_window.overrideredirect(True)
    waifu_window.attributes("-topmost", True)
    waifu_window.attributes("-alpha", 0.9)
    waifu_window.configure(bg="#2b2b2b")

    width = 300
    height = 120

    screen_width = waifu_window.winfo_screenwidth()
    screen_height = waifu_window.winfo_screenheight()

    x = screen_width - width - 20
    y = screen_height - height - 60

    waifu_window.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(
        waifu_window,
        text=message,
        bg="#2b2b2b",
        fg="white",
        font=("Segoe UI", 10),
        wraplength=260,
        justify="left"
    )
    label.pack(padx=15, pady=15)

    # Destruir después de 6 segundos
    waifu_window.after(6000, destroy_waifu)

    waifu_window.mainloop()

def destroy_waifu():
    global waifu_window
    if waifu_window:
        waifu_window.destroy()
        waifu_window = None
        
print("🌸 Waifu virtual iniciada...")

while True:
    if time.time() - last_activity > INACTIVITY_TIME:
        context = get_active_window()
        message = waifu_comment(context)
        show_waifu(message)
        last_activity = time.time()
    time.sleep(1)
