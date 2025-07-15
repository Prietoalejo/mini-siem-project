import json
import datetime
import random
# Tipos de eventos de seguridad comunes
POSSIBLE_EVENTS = [
    "authentication.success",    # Inicio de sesión exitoso
    "authentication.failure",    # Inicio de sesión fallido
    "authorization.denied",      # Acceso a recurso denegado
    "file.access.read",          # Archivo leído
    "file.access.write",         # Archivo modificado/escrito
    "network.port_scan",         # Escaneo de puertos detectado
    "network.brute_force",       # Ataque de fuerza bruta de red
    "system.shutdown",           # Apagado del sistema
    "system.startup",            # Inicio del sistema
    "software.update",           # Actualización de software
    "alert.firewall.block",      # Firewall bloquea tráfico
    "alert.ids.detection",       # Detección de intrusión (IDS)
    "admin.config_change",       # Cambio de configuración de administrador
    "service.start",             # Servicio iniciado
    "service.stop",              # Servicio detenido
    "alert.security_violation"   # (Nuevo evento simulado) Indica una violación de seguridad
]

# Usuarios comunes clasificados por rol
ADMIN_USERS = ["admin", "root", "sysadmin"]
STANDARD_USERS = ["user_dev", "alejandro", "guest"]
SERVICE_ACCOUNTS = ["web_service", "db_user", "svc_account"]

ALL_POSSIBLE_USERS = ADMIN_USERS + STANDARD_USERS + SERVICE_ACCOUNTS


# Mensajes de detalle predefinidos, con placeholders para rellenar
DETAIL_TEMPLATES = {
    "authentication.success": [
        "Login exitoso para {user} desde IP {ip_src}.",
        "Credenciales válidas, acceso concedido a {user}.",
    ],
    "authentication.failure": [
        "Contraseña incorrecta para {user}.",
        "Usuario {user} no encontrado.",
        "Múltiples intentos fallidos para {user} desde IP {ip_src}.",
    ],
    "authorization.denied": [
        "Acceso denegado a recurso restringido (/etc/shadow) para {user}.",
        "Permisos insuficientes para {user} intentando acceder a /var/log/secure.",
        "Intento de acceso no autorizado a clave SSH por {user}.",
    ],
    "file.access.read": [
        "Archivo de configuración leído: {file_path} por {user}.",
        "Acceso a log de auditoría: {file_path} por {user}.",
        "Archivo de datos leído: {file_path} por {user}.",
    ],
    "file.access.write": [
        "Archivo modificado: {file_path} por {user}.",
        "Nuevo archivo creado en directorio sensible: {file_path} por {user}.",
        "Permisos de archivo cambiados en {file_path} por {user}.",
    ],
    "network.port_scan": [
        "Escaneo de puertos detectado desde IP {ip_src}.",
        "Tráfico de escaneo TCP/SYN inusual en puerto 22 desde {ip_src}.",
    ],
    "network.brute_force": [
        "Múltiples intentos fallidos de conexión SSH desde IP {ip_src} para usuario {user}.",
        "Ataque de fuerza bruta detectado en servicio web desde {ip_src}.",
    ],
    "system.shutdown": [
        "Sistema apagado por {user}.",
        "Reinicio del servidor programado por {user}.",
    ],
    "system.startup": [
        "Sistema iniciado en {ip_src}.",
        "Servidor {ip_src} arrancado.",
    ],
    "software.update": [
        "Actualización de seguridad aplicada a {software_name}.",
        "Parche de software {software_name} instalado por {user}.",
    ],
    "alert.firewall.block": [
        "Tráfico bloqueado de {ip_src} en puerto 3389 (RDP).",
        "Intento de conexión no autorizado bloqueado desde {ip_src}.",
    ],
    "alert.ids.detection": [
        "Alerta IDS: Posible inyección SQL detectada desde {ip_src}.",
        "Firma de malware detectada en tráfico de red desde {ip_src}.",
    ],
    "admin.config_change": [
        "Configuración del firewall modificada por {user}.",
        "Cambio en políticas de usuario por {user}.",
        "Regla de enrutamiento modificada por {user}."
    ],
    "service.start": [
        "Servicio {service_name} iniciado exitosamente.",
        "Base de datos {service_name} en línea.",
    ],
    "service.stop": [
        "Servicio {service_name} detenido por {user}.",
        "Base de datos {service_name} apagada."
    ],
    "alert.security_violation": [ # Plantillas para el nuevo tipo de evento de alerta
        "ALERTA DE SEGURIDAD: {user} accedió a archivo sensible {file_path}.",
        "ACCESO SOSPECHOSO: Usuario '{user}' intentó '{event_type}' en recurso privilegiado.",
        "POSIBLE FUERZA BRUTA: Múltiples fallos de autenticación para '{user}' desde '{ip_src}'."
    ]
}

# Recursos comunes (para eventos de archivo/acceso)
POSSIBLE_FILES = [
    "/etc/passwd", "/etc/shadow", "/var/log/syslog", "/var/log/auth.log",
    "/var/www/html/index.php", "/app/config.json", "/opt/data/sensitive.csv",
    "/root/.ssh/id_rsa" # Añadido a esta lista general para ser usado dinámicamente
]
POSSIBLE_SOFTWARE = ["nginx", "apache", "ssh_daemon", "database_server", "web_app", "mail_server"]
POSSIBLE_SERVICES = ["SSH", "HTTPD", "PostgreSQL", "FTP", "DNS", "NTP"]

# Archivos específicamente sensibles (para la lógica de simulación de anomalías)
SENSITIVE_FILES = ["/etc/passwd", "/etc/shadow", "/root/.ssh/id_rsa"]


def generate_simple_log():
    """Genera un unido diccionario que simula entradas a un log de seguridad
    Los logs incluyen, fecha exacta, direccion IP, usuario, el evento a registrar,
    el detalle del evento, Ocasionalmente genera anomalias de seguridad tomando como base
    los usuarios y los eventos para hacer que la simulacion sea un poco mas real
    
    Retorna: un diccionario que es representacion del LOG"""
    timestamp = str(datetime.datetime.today())
    ip_origin = str(f"192.168.1.{random.randint(1,254)}")
    usuario = random.choice(ALL_POSSIBLE_USERS)
    evento = random.choice(POSSIBLE_EVENTS)
    detalle = random.choice(DETAIL_TEMPLATES.get(evento))
    s_file_path = random.choice(POSSIBLE_FILES)
    s_service_name = random.choice(POSSIBLE_SERVICES)
    s_software_name = random.choice(POSSIBLE_SOFTWARE)
    detalle_final = detalle.format(
        user = usuario,
        ip_src = ip_origin,
        file_path = s_file_path,
        service_name = s_service_name,
        software_name = s_software_name)
    log= {
        "Time-Stamp": timestamp,
        "IP-origin" : ip_origin,
        "Usuario" : usuario,
        "Evento": evento,
        "Detalle": detalle_final
    }

    return log

print(generate_simple_log())