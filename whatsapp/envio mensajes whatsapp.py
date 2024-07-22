import pyautogui
import time
import webbrowser

numero = '+5491161495717'
url='http://web.whatsapp.com/send?phone='
webbrowser.open(url+numero)
time.sleep(8)

pyautogui.write('Memichus es mensaje de prueba, estoy programando, api')
pyautogui.press('enter')
