# features/config.py
# Datos estáticos reutilizables en todas las pruebas

# --- Credenciales y roles ---
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent.resolve()

PATHS = {
    "SCREENSHOTS": str(BASE_DIR / "screenshots"),
    "COOKIES": str(BASE_DIR / "cookies.pkl"),
    "TEST_RESULTS": str(BASE_DIR / "test-results")
}

ARCHIVOS = {
    "RECIBO_PDF": str(Path.home() / "Downloads" / "Recibo.pdf"),
    "XML": str(Path.home() / "Downloads" / "9XMLfiscal.xml"),
    # Agrega más rutas según necesites
}
#635 nacional
#636 internacional 786 785 783 781 780 



NUMERO_COMISIÓN = '786'
ESTATUS_COMISIÓN = 'Solicitud de comisión en registro'

#mainc048 - mainc044 - uedga193
USUARIOS = {
    "OPERADOR_SIGEVI": {
        "usuario": "uedga193",
        "password": "B@40bR4$1607202$",
        "rol": "Operador SIGEVI"
    },
    "Autorizador_SIGEVI": {
        "usuario": "uedga193",
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



CIUDAD = {
    "state": "Colima",
    "town": "Colima"
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

# --- Datos de formularios ---
#meinc048
#area_gasto: 192100
SOLICITUDES = {
    "SIN_ANTICIPO": {
        "con_anticipo": "No", 
        "expediente": "112313",
        "tipo_comision": "NACIONAL",
        "transporte": "Avión",
        "fecha_salida": "07/2025/14",
        "fecha_regreso": "07/2025/16",
        "expediente_autoriza": "48496",
        "area_gasto": "220000",
        "objetivo": "Comisión con anticipo nacional "
    },
    "CON_ANTICIPO": {
        "fecha_salida": "07/22/2025",
        "fecha_regreso": "07/24/2025",
    }

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
        "expediente": "112313",
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


