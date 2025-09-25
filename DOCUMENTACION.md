# 📋 DOCUMENTACIÓN TÉCNICA - FRAMEWORK DE AUTOMATIZACIÓN SIGEVI

## 🎯 ÍNDICE
1. [Descripción General](#-descripción-general)
2. [Stack Tecnológico](#-stack-tecnológico)
3. [Estructura del Proyecto](#-estructura-del-proyecto)
4. [Arquitectura del Framework](#-arquitectura-del-framework)
5. [Configuración y Setup](#-configuración-y-setup)
6. [Ejecución de Pruebas](#-ejecución-de-pruebas)
7. [Mantenimiento y Mejores Prácticas](#-mantenimiento-y-mejores-prácticas)

📖 DESCRIPCIÓN GENERAL
Framework de automatización de pruebas para el sistema SIGEM (Sistema de Gestión de Viáticos) de Banobras, desarrollado bajo la metodología BDD (Behavior Driven Development) utilizando Selenium WebDriver con Python.

Objetivo Principal: Automatizar los flujos críticos de negocio relacionados con la gestión de comisiones, viáticos y procesos de comprobación.

🛠 STACK TECNOLÓGICO
Tecnología	            Versión	Propósito
Python	                3.9+	Lenguaje de programación
Selenium WebDriver	    4.0+	Automatización del navegador
Behave	                1.2.6	Framework BDD
Allure Framework	    2.13+	Reportes y dashboards
WebDriver Manager	    3.8+	Gestión automática de drivers
PyAutoGUI	            0.9+	Automatización de interacciones GUI

📁 ESTRUCTURA DEL PROYECTO
AUTOMAT_SIGEM/
├── 📁 features/                 # Escenarios BDD en Gherkin
│   ├── 📄 *.feature            # Archivos de especificaciones
│   ├── 📁 steps/               # Implementación de steps
│   └── 📁 environment.py       # Configuración global de Behave
├── 📁 pages/                   # Page Object Model (POM)
│   ├── 📄 base_page.py         # Clase base con métodos comunes
│   ├── 📄 comprobacion_page.py # Página de comprobaciones
│   └── 📄 *.py                # Otras page classes
├── 📁 data/                    # Datos de prueba
│   ├── 📄 roles.json          # Credenciales y roles
│   ├── 📄 formularios.json    # Datos de formularios
│   └── 📄 entornos.json       # Configuración por ambiente
├── 📁 logs/                    # Logs de ejecución
├── 📁 reports/                 # Reportes de Allure
├── 📁 resultados_1/            # Resultados adicionales
├── 📁 venv/                    # Entorno virtual Python
├── 📄 config.py               # Configuración centralizada
├── 📄 behaves.ini             # Configuración de Behave
└── 📄 .gitignore              # Archivos excluidos de Git

📁 CARPETA FEATURES
Propósito: Contiene los escenarios de prueba en lenguaje Gherkin

Archivos .feature: Especificaciones de comportamiento en lenguaje natural

Steps/: Implementación de los steps en Python

environment.py: Hooks globales de Behave

Ejemplo de escenario:

gherkin
@comision
Scenario: Alta de solicitud sin anticipo - nacional
    Given Seleccionar el menu de comisiones y dar clic en Nueva Solicitud
    When Completamos los campos obligatorios
    Then La solicitud se crea exitosamente

📁 CARPETA PAGES
Propósito: Implementa el Page Object Model (POM)

base_page.py: Métodos comunes y helpers
comprobacion_page.py: Interacciones con página de comprobaciones
Métodos típicos: clic_consultar(), cargar_archivos(), validar_grid()


📁 CARPETA DATA
Propósito: Almacenamiento centralizado de datos de prueba

roles.json: Credenciales de usuarios y roles
formularios.json: Datos para llenado de formularios
entornos.json: Configuración por ambiente (dev, QA, prod)

📁 DESCRIPCIÓN DE LA CARPETA PAGES
Propósito Principal:
La carpeta pages implementa el Page Object Model (POM), un patrón de diseño que representa cada página web o componente de la aplicación SIGEM como una clase de Python. Esto permite encapsular la lógica de interacción con los elementos UI.

🔧 Herencia y Estructura:
python
from .base_page import BasePage  # Hereda de la clase base

class ComprobacionPage(BasePage):
    # Locators (XPath, CSS) como constantes
    # Métodos de interacción específicos
    def __init__(self, driver):
        super().__init__(driver)  # Inicializa herencia

📍 Locators Mapeados:
python
# Ejemplos de locators organizados
MENU_CONSULTAR = (By.XPATH, "//a[contains(text(), 'Consultar')]")
BOTON_ADDCOMPRO = (By.XPATH, "//button[contains(text(), 'Agregar comprobación')]")
PDF = (By.XPATH, "//input[@type='file' and contains(@id, 'invoicePDF')]")

🛠️ Métodos de Acción:
python
def clic_consultar(self):
    self.wait_and_click(self.MENU_CONSULTAR, self.DEFAULT_WAIT)
    return self  # Permite method chaining

def cargar_archivos(self, PATH_PDF, PATH_XML):
    self.upload_file(self.PDF, PATH_PDF)
    self.upload_file(self.XML, PATH_XML)
    return self


📁 DESCRIPCIÓN DE LA CARPETA STEPS
Propósito Principal:
La carpeta steps contiene los step definitions - las implementaciones en Python que dan vida a los escenarios Gherkin. Aquí es donde se conecta el lenguaje natural de los features con las acciones técnicas de Selenium.

Ejemplo Práctico Basado en tu Feature:
En el archivo .feature:
gherkin
@comision
Scenario: Alta de solicitud sin anticipo - nacional
    Given Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud
    and Deberíamos ver el formulario de solicitud de comisión
    and Completamos los campos obligatorios
    When Guardamos la solicitud
    Then La solicitud se crea exitosamente


En steps/solicitud_steps.py:
python
from behave import given, when, then
from pages.solicitud_page import SolicitudPage

@given('Seleccionar el menu de comisiones y dar clic en el boton de Nueva Solicitud')
def step_seleccionar_menu_comisiones(context):
    context.solicitud_page = SolicitudPage(context.driver)
    context.solicitud_page.clic_menu_comisiones()
    context.solicitud_page.clic_nueva_solicitud()

@then('Deberíamos ver el formulario de solicitud de comisión')
def step_ver_formulario(context):
    assert context.solicitud_page.formulario_es_visible()

@when('Completamos los campos obligatorios')
def step_completar_campos(context):
    context.solicitud_page.ingresar_datos_obligatorios(
        destino="Ciudad de México",
        proposito="Reunión de negocios",
        presupuesto=5000
    )

@when('Guardamos la solicitud')
def step_guardar_solicitud(context):
    context.solicitud_page.clic_guardar()

@then('La solicitud se crea exitosamente')
def step_validar_creacion_exitosa(context):
    assert context.solicitud_page.mensaje_exito_es_visible()
    assert context.solicitud_page.estatus_es("Solicitud de comisión en registro")



📄 ANÁLISIS DE environment.py
🔧 Propósito Principal:
El archivo environment.py es el orquestador global de Behave. Maneja el ciclo de vida completo de la ejecución de pruebas con hooks que se ejecutan en diferentes fases.

🎯 Funcionalidades Clave:
1. Configuración Global (before_all):
python
def before_all(context):
    # Configura logging avanzado
    context.logger = logging.getLogger('automatizacion')
    
    # Configura el WebDriver con Chrome
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
2. Gestión de Sesiones (before_scenario):
python
def before_scenario(context, scenario):
    # Carga datos JSON para el escenario
    context.data = {
        "roles": load_json("roles.json"),
        "formularios": load_json("formularios.json"),
        "entornos": load_json("entornos.json")
    }
    
    # Lógica inteligente de login
    if hasattr(context, 'login_exitoso') and context.login_exitoso:
        context.logger.warning("⚠️ Sesión activa detectada - Omitiendo login")
3. Captura de Evidencias (after_step):
python
def after_step(context, step):
    if step.status == "failed":
        allure.attach(  # Captura screenshot en fallos
            context.driver.get_screenshot_as_png(),
            name=f"error_{step.name}",
            attachment_type=AttachmentType.PNG
        )