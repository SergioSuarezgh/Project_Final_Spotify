from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC  # condiciones esperadas...

from selenium.webdriver import ActionChains as AC   # acciones encadenadas, rollo doble click

from selenium.webdriver.common.keys import Keys  # manejar teclas

import time

import pandas as pd
pd.set_option('display.max_columns', None)   
pd.set_option('display.max_rows', None)

from webdriver_manager.chrome import ChromeDriverManager

PATH=ChromeDriverManager().install()

import warnings
warnings.filterwarnings('ignore')

opciones=Options()

# quita la bandera de ser robot
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)

opciones.headless=False   # si True, no aparece la ventana (headless=no visible)

opciones.add_argument('--start-maximized')         # comienza maximizado

#opciones.add_extension('driver/adblock.crx')       # adblocker

opciones.add_argument('user-data-dir=selenium')    # mantiene las coockies

import Utils
from datetime import date

from decouple import config
user_spoty = config('user_spoty', default='')
pass_spoty = config('pass_spoty', default='')

from joblib import Parallel, delayed

def extraer_autores():
    
    driver=webdriver.Chrome(PATH)
    driver.get('https://www.shazam.com/es-es')
    
    time.sleep(2)
    texto=driver.find_element(By.XPATH, '//*[@id="DSqSkSTy"]')
    time.sleep(2)
    
    texto.send_keys('Manowar Master of the wind')
    
    texto.send_keys(u'\ue007') 
    
    time.sleep(2)

extraer_autores()
    
'''input_autor=driver.find_element(By.XPATH, '/html/body/form/input[1]')
    
    time.sleep(2)
    
    input_autor.send_keys(str(autor))  # escribe texto

    input_autor.send_keys(u'\ue007')  # tecla ENTER

    time.sleep(2)
    
    datos=driver.find_element(By.XPATH,'/html/body/div').text
    
    
    
    
    cadena_final=datos
    
    #cadena_final=pd.DataFrame(cadena_final)
    
    driver.quit()
    '''
    #return cadena_final