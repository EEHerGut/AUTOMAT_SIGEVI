import logging
import sys
from datetime import datetime
import os

def setup_global_logger():
    """Configura el logger global para toda la aplicación"""
    
    # Crear directorio de logs si no existe
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configurar formato
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configurar handlers
    file_handler = logging.FileHandler(
        f'logs/app_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    )
    file_handler.setFormatter(formatter)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    
    # Configurar logger principal
    logger = logging.getLogger('APP_LOGGER')
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Crear instancia global
global_logger = setup_global_logger()