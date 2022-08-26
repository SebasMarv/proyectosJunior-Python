# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'D:\\Descargas\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Iniciarla en pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

driver.get('https://ww3.sunat.gob.pe/ol-ti-itconsvalicpe/ConsValiCpe.htm')

#variables
ruc = '20392664310'
#seleccionar un elemento de un desplegable
serie = 'F001'
numero = '00028799'
total = '11883.25'
fecha = '23/08/2022'

time.sleep(5)

#Ingreso de informacion
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[1]/div[2]/input')))\
    .send_keys(ruc)

time.sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[2]/div[2]/select/option[2]')))\
    .click()

time.sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[5]/div[2]/input[1]')))\
    .send_keys(serie)

time.sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[5]/div[2]/input[2]')))\
    .send_keys(numero)

time.sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '//*[@id="fec_emision"]')))\
    .send_keys(fecha)

time.sleep(5)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/form/div/div[2]/div[2]/div[2]/div[7]/div[2]/input')))\
    .send_keys(total)

time.sleep(5)

#Buscar
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input.btn.btn-primary')))\
    .click()