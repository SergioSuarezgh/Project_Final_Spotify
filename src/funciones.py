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

##Función para extraer datos de shazam

def shazam(canciones):
    try:
        driver=webdriver.Chrome(PATH)
        driver.get('https://www.shazam.com/es-es')

        time.sleep(2)

        driver.maximize_window()

        time.sleep(5)

        caja=driver.find_element(By.XPATH,'/html/body/div[4]/header/div/div[1]/div[2]/div[1]/div/div[1]/form/input')

        
        time.sleep(5)


        caja.send_keys(canciones)


        caja.send_keys(u'\ue007') 

        time.sleep(5)

        cancion=driver.find_element(By.XPATH,'/html/body/div[4]/header/div/div[1]/div[2]/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div[2]/a').click()

        time.sleep(5)

        can=driver.find_element(By.XPATH,'/html/body/div[4]/div/main/div/div[1]/div/article[2]/div[2]/div[2]/div[1]/div/div/h3').text
        
        time.sleep(3)
        driver.quit()
        division_canciones=canciones.split(',')
        
        dict_cancion={'cancion':division_canciones[0], 'artista': division_canciones[1], 'estilo': can}
        
        df=pd.DataFrame([dict_cancion])
    except:
        dict_cancion={'cancion':division_canciones[0], 'artista': division_canciones[1], 'estilo': 'error'}
        df=pd.DataFrame([dict_cancion])
        
        
    
    return df

##cargamos datos de canciones

canciones=pd.read_excel(r'C:/Users/sersu/IRONHACK/Project_Final_Spotify/data/canciones.xls')

##Ejecutamos
hol=shazam(canciones.aut[0])
print(hol)

lst_canciones=canciones.aut

from tqdm.notebook import tqdm 
lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[:1000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[1000:2000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[2000:3000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[3000:4000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[4000:5000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[5000:6000]))

lst_df=Parallel(n_jobs=-1, verbose=True)(delayed(shazam)(cancion) for cancion in tqdm(lst_canciones[6000:6954]))