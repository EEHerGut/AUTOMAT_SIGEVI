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

NUMERO_COMISIÓN = '00999'
ESTATUS_COMISIÓN = 'Solicitud de comisión en registro'



#mainc048 - mainc044 - uedga193
USUARIOS = {
    "OPERADOR_SIGEVI": {
        "usuario": "mainc044",
        "password": "B@40bR4$1607202$",
        "rol": "Operador SIGEVI"
    },
    "Autorizador_SIGEVI": {
        "usuario": "mainc044",
        "password": "B@40bR4$1607202$",
        "rol": "Autorizador SIGEVI"
    }
}

# --- URLs del sistema ---

BASE_URL = "https://frontend-sigevi-develop.banobras.gob.mx"

URLS = {
    "BASE":  f"{BASE_URL}/auth/login",
    "COMISIONES": f"{BASE_URL}/comision/comisiones"
}

##Tlaxcala
##Apizaco

##Guanajuato
##Celaya
CIUDAD = {
    "state": "Guanajuato",
    "town": "Celaya"
}

VUELO = {
    "trip": "Viaje sencillo",
    "day_off": "14/07/2025",
    "origen": "MEX - MEXICO",
    "arrive": "TLC - TOLUCA",
    "aeroline": "AEROMEXICO",
}

GASTO = {
    "concept": "Gasolina",
    "amount": "2342.13"
}



SOLICITUD_ANTICIPO={
        "anticipo": "Sí",
        "data": "08/15/2025",
        "data2": "08/17/2025",
 }

COMPLEMENTO = {
    "FAVOR": {
        "pdf":r"C:\Users\Lenovo\Downloads\Recibo.pdf",
        "xml":r"C:\Users\Lenovo\Downloads\9XMLfiscal.xml",
        "concepto_oper": "Hospedaje",
        "importe": "476.23",
        "motivo": "complemento nacional a favor"
    },
     "CONTRA": {
        "expediente": "55735",
        "tipo_comision": "NACIONAL",
        "transporte": "Avión",
        "fecha_salida": "07/2025/14",
        "fecha_regreso": "07/2025/16",
        "expediente_autoriza": "48496",
        "area_gasto": "220000",
        "objetivo": "Comisión con anticipo nacional "
    }
}

IMPUESTO = {
        "id_complemento": "1",
        "concepto": "IVA por prestación de servicios",
        "monto": "230.32"
}

COMPROBACION ={
        "concepto":"Alimentos",
        "monto":"286.11",
        "concepto_impuesto": "19",
        "monto_impuesto":"129.41"
}