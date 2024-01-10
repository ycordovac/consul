from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.exteriores.gob.es/Consulados/lahabana/es/ServiciosConsulares/Paginas/index.aspx"
id_combobox="ctl00_ctl45_g_edd31fb6_ac81_4417_a981_52a85dac1b3b_ctl00_ddlCategories"
opcion_visado="Visados"

id_segundo_combobox="ctl00_ctl45_g_edd31fb6_ac81_4417_a981_52a85dac1b3b_ctl00_ddlService"
opcion_familiares="Visados de familiares de ciudadanos UE y de beneficiarios Acuerdo de Retirada UE-Reino Unido"

id_boton_buscar="ctl00_ctl45_g_edd31fb6_ac81_4417_a981_52a85dac1b3b_ctl00_btnSearchSC"

id_boton_continuar="idCaptchaButton"

driver = webdriver.Chrome()
result = driver.get(url)



try:
    # Espera hasta que el combo box sea interactuable
    combo_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id_combobox))
    )

    # Crea un objeto Select para el combo box
    select = Select(combo_box)

    # Selecciona una opción por su valor, índice o texto visible
    # select.select_by_value(opcion_visado)
    # o select.select_by_index(2)
    select.select_by_visible_text(opcion_visado)

     # Espera hasta que el segundo combo box sea interactuable después de que se actualice la página
    segundo_combobox = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, id_segundo_combobox))
    )

    # Selecciona una opción en el segundo combo box
    select_segundo_combobox = Select(segundo_combobox)
    select_segundo_combobox.select_by_value(opcion_familiares)

    boton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, id_boton_buscar))
    )

    # Da clic en el botón
    boton.click()

    # Espera hasta que la URL cambie (indicando que se ha cargado la nueva página)
    WebDriverWait(driver, 100).until(
        EC.url_changes(url)
    )

    # Espera hasta que el enlace sea interactuable (puedes ajustar el selector según tu HTML)
    enlace = WebDriverWait(driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="https://www.citaconsular.es/es/hosteds/widgetdefault/2f9880d8d5b8feb958c81d2a08157bcf1/bkt871926"]'))
    )

    # Da clic en el enlace
    enlace.click()

    boton_continuar = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.ID, id_boton_continuar))
    )

    # Da clic en el botón
    boton_continuar.click()


finally:
    # Cierra el navegador
    driver.quit()
