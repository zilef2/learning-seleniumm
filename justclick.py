from selenium import webdriver
from selenium.webdriver.common.by import By
# Inicializar el driver de Chrome
driver = webdriver.Chrome()

# Abrir la página de Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Esperar un momento (solo como ejemplo)
driver.implicitly_wait(5)

# Imprimir el título de la página
print("Título de la página:", driver.title)

# Identificar el botón por su selector CSS (cambia este selector por el adecuado)
boton_ejemplo = driver.find_element(By.CSS_SELECTOR, "button.example-button")

# Hacer clic en el botón
boton_ejemplo.click()

# Esperar un momento (solo como ejemplo)
driver.implicitly_wait(15)

# Cerrar el navegador
driver.quit()