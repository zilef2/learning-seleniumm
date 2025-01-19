from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import tensorflow as tf
# tf.config.experimental.set_memory_growth(tf.config.list_physical_devices('GPU')[0], True)

# Inicializar el controlador del navegador (asegúrate de tener el controlador de Chrome o el navegador configurado)
driver = webdriver.Chrome()

# Abrir la página de login
driver.get("http://127.0.0.1:8002/login")

# Esperar de forma implícita (por si tarda en cargar)
driver.implicitly_wait(5)

# Encontrar el campo de correo electrónico y escribir el correo
email_field = driver.find_element(By.ID, "email")  # Cambia "email" si el campo tiene otro nombre
email_field.send_keys("ajelof2+6@gmail.com")

# Encontrar el campo de contraseña y escribir la contraseña
password_field = driver.find_element(By.ID, "password")  # Cambia "password" si el campo tiene otro nombre
password_field.send_keys("1234_modnomsuperadmin00.+-*1234_modnom")

# Encontrar el botón de inicio de sesión y hacer clic
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")  # Cambia el selector si es necesario
login_button.click()

# La ventana permanece abierta para más instrucciones
driver.implicitly_wait(150)
# La ventana permanece abierta para más instrucciones
# centro_costos = driver.find_element(By.XPATH, "//a[contains(text(), 'Centros de Costos')]")
centro_costos = driver.find_element(By.LINK_TEXT, "Centros de Costos")

centro_costos.click()

input("Presiona Enter para cerrar el navegador manualmente...")
