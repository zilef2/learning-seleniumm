from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#C:\\ruta\\a\\tu\\driver\\msedgedriver.exe
#URL_de_tu_página
#id_del_elemento
#id_de_la_celda_A1


# Inicializa el controlador de Selenium para Microsoft Edge

driver = webdriver.Edge(executable_path="C:\\ruta\\a\\tu\\driver\\msedgedriver.exe")

# Abre Microsoft Edge y navega a la página web deseada
driver.get("URL_de_tu_página")

# Encuentra y almacena las ventanas actuales
ventanas_actuales = driver.window_handles

# Haz clic en el elemento que abrirá una nueva ventana o pestaña
driver.find_element(By.ID, "id_del_elemento").click()

# Espera hasta que se abra la nueva ventana o pestaña
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Identifica la nueva ventana o pestaña
nueva_ventana = [ventana for ventana in driver.window_handles if ventana not in ventanas_actuales][0]

# Cambia el enfoque a la nueva ventana o pestaña
driver.switch_to.window(nueva_ventana)

# Ahora puedes interactuar con elementos en la nueva ventana o pestaña
# Por ejemplo, haz clic en la celda A1
driver.find_element(By.ID, "id_de_la_celda_A1").click()

# Cierra el navegador al finalizar
driver.quit()
