from selenium.webdriver.common.by import By

class BotonesComunes:

    #ELEMENTOS DE CATALOGOS
    BOTON_CREAR=  (By.XPATH, "//button[contains(text(), 'Agregar')]") 
    BOTON_CREAR_ESTADO =  (By.XPATH, "//div[@class='modal-footer']//button[contains(text(), 'Agregar')]") 
    BOTON_CONFIRMAR = (By.XPATH, "//app-confirm-modal//button[contains(text(), 'Aceptar')]")
    BOTON_CONF = (By.XPATH, "//app-confirm-modal//button[contains(@class, 'btn btn-primary h5')]")
    BOTON_MODIFICAR = (By.XPATH, "(//a[contains(@class, 'editOption')])[1]")  
    GRID = (By.XPATH, "//table[@class='table table-striped table-hover clsTable']")
    SWITCH = (By.XPATH, "//span[@class='clase-del-span' or contains(@class, 'slider')]")  

    # Puedes agregar más botones comunes que identifiques
