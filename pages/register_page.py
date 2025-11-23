from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    # --- LOCATORS (Identificadores de elementos) ---
    # Nota: Como no tengo el HTML real, asumo que usan 'name' o 'id'.
    # Si al correr el test falla, inspecciona la web y ajusta estos valores.
    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Registrarse')]")
    SUCCESS_MSG = (By.XPATH, "//h2[contains(text(), 'Bienvenido')]") # Ajustar según mensaje real

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://talentolab-test.netlify.app" # URL de tu PDF

    def open(self):
        """Abre la página de registro."""
        self.driver.get(self.url)

    def complete_form(self, name, email, password):
        """Llena el formulario completo y envía."""
        self.type(self.NAME_INPUT, name)
        self.type(self.EMAIL_INPUT, email)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BTN)

    def is_registration_successful(self):
        """Verifica si aparece el mensaje de éxito."""
        try:
            return self.get_text(self.SUCCESS_MSG)
        except:
            return None