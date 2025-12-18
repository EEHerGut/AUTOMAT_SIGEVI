# features/config.py
# Datos estáticos reutilizables en todas las pruebas

# --- Credenciales y roles ---
from pathlib import Path
from utils.data_loader import load_json

BASE_DIR = Path(__file__).parent.resolve()

PATHS = {
    "SCREENSHOTS": str(BASE_DIR / "screenshots"),
    "COOKIES": str(BASE_DIR / "cookies.pkl"),
    "TEST_RESULTS": str(BASE_DIR / "test-results")
}

TIEMPOS_ESPERA = {
    'DEFAULT_WAIT': 15,  # Espera normal para elementos interactivos
    'LONG_WAIT': 30,     # Espera más larga para elementos críticos o lentos
    'SHORT_WAIT': 5      # Espera corta para verificaciones rápidas
}

USUARIOS = load_json("roles.json")
ENV_CONFIG = load_json("entornos.json")["develop"]  # Cambiar a "prod" en producción
FORM_DATA = load_json("formularios.json")
CAT_DATA = load_json("catalogos.json")

ARCHIVOS = {
    "RECIBO_PDF": str(Path.home() / "Downloads" / "Recibo.pdf"),
    "XML": str(Path.home() / "Downloads" / "9XMLfiscal.xml"),
    # Agrega más rutas según necesites
}
#635 nacional
#636 internacional 786 785 783 781 780 
#Solicitud de comisión en registro
#Comisión pendiente de comprobación
#Solicitud de comisión pendiente de autorización

NUMERO_COMISIÓN = '00076'
ESTATUS_COMISIÓN = 'Solicitud de comisión en registro'
ID_SOLICITUD= '00985'
ID_FACTURA= '863'



#mainc048 - mainc044 - uedga193
USUARIOS = {
    "OPERADOR_SIGEVI": {
        "usuario": "mainc049",
        "password": "Banobras17122025",
        "rol": "Operador SIGEVI"
    },
    "Autorizador_SIGEVI": {
        "usuario": "mainc049",
        "password": "Banobras17122025",
        "rol": "Autorizador SIGEVI"
    }
}

# --- URLs del sistema ---
BASE_URL = "https://frontend-sigevi-qa.banobras.gob.mx"

#--- BASE_URL = "https://frontend-sigevi-develop.banobras.gob.mx" ---

URLS = {
    "BASE":  f"{BASE_URL}/auth/login",
    "COMISIONES": f"{BASE_URL}/comision/comisiones"
}

