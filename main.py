import pyautogui 
import time
#Remember: pyoutogui.write -> write a string text
#Remember: pyoutogui.press -> press especific keyboard key
#Remember: pyoutogui.click -> click mouse1

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/tabela')
pyautogui.press('enter')
time.sleep(2)
