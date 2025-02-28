import pyautogui
import time
import keyboard

def tiempo(x):
    tiempo = x
    for i in range(0, tiempo):
        print("Empieza en "+ str(tiempo - i))
        time.sleep(1)
    time.sleep(1)
print("BOT: (Se necesita pyautogui, time y keyboard instalado)")
print("Selecciona:")
print("[1] Minecraft - Minado automático")
print("[2] Spamear Mensajes (Whatsapp)")
print("[3] Spamear Sticker (Whatsapp)")
print()
elec = input()
if (elec == "1"):
    tiempo(5)
    pyautogui.mouseDown()
    pyautogui.keyDown('w')
    pyautogui.keyDown('shift')
    keyboard.wait('ctrl+l')
    pyautogui.keyUp('w')
    pyautogui.keyUp('shift')
    pyautogui.mouseUp()
elif (elec == "2"):
    texto = input("Texto: ")
    veces = int(input("Veces: "))
    print("Tienes 5 segundos para poner el cursor en el input del mensaje")
    tiempo(5)
    for k in range(0, veces):
        pyautogui.typewrite(texto)
        pyautogui.press("enter")
elif (elec == "3"):
    veces = int(input("Veces: "))
    print("Coloca tu cursor en el sticker a enviar")
    tiempo(5)
    for k in range(0, veces):
        pyautogui.click()