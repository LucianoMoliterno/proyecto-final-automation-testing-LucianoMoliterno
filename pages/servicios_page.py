from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

class ServiciosPage(BasePage):
    """Page Object para la sección de Servicios."""

    # Locators
    TITULO_SERVICIOS = (By.XPATH, "//h2[contains(text(), 'Servicios')]")
    TARJETAS_SERVICIOS = (By.CSS_SELECTOR, ".service-card, .card")
    TARJETA_RECLUTAMIENTO = (By.XPATH, "//*[contains(text(), 'Reclutamiento')]")
    TARJETA_HEADHUNTING = (By.XPATH, "//*[contains(text(), 'Headhunting')]")
    TARJETA_EVALUACION = (By.XPATH, "//*[contains(text(), 'Evaluación')]")
    TARJETA_CONSULTORIA = (By.XPATH, "//*[contains(text(), 'Consultoría')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Logger.get_logger(__name__)

    def get_cantidad_tarjetas(self):
        """Cuenta la cantidad de tarjetas de servicios visibles."""
        try:
            tarjetas = self.driver.find_elements(*self.TARJETAS_SERVICIOS)
            cantidad = len(tarjetas)
            self.logger.info(f"Se encontraron {cantidad} tarjetas de servicios")
            return cantidad
        except Exception as e:
            self.logger.error(f"Error al contar tarjetas: {str(e)}")
            return 0

    def verificar_servicio_existe(self, nombre_servicio):
        """Verifica si un servicio específico está visible."""
        try:
            locator = (By.XPATH, f"//*[contains(text(), '{nombre_servicio}')]")
            element = self.find(locator)
            self.logger.info(f"Servicio '{nombre_servicio}' encontrado")
            return True
        except:
            self.logger.warning(f"Servicio '{nombre_servicio}' no encontrado")
            return False

    def get_servicios_disponibles(self):
        """Retorna lista de servicios disponibles."""
        servicios = ["Reclutamiento", "Headhunting", "Evaluación", "Consultoría"]
        disponibles = []

        for servicio in servicios:
            if self.verificar_servicio_existe(servicio):
                disponibles.append(servicio)

        return disponibles

