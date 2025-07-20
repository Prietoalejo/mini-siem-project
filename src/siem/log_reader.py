import json
import os 
from collections import defaultdict
from collections import Counter

def read_log_json(file_path: str):
    """Funcion que funcionara para leer y procesar los logs desde nuestros 
    archivos tipo json para poder manejarlos con python

    args: file_path sera la ruta del archivo que vamos a procesar 

    returns: Como manejamos json vamos a desvolver una lista de los diccioarios
    deberia retorna None si ocurre algun error en la lectura del archivoi
    """
    if not os.path.exists(file_path):
        print(f"El archivo:{file_path}, no fue encontrado")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as f: #as f
            contenido = f.read() #as f
            logs = json.loads(contenido)

        print(f"se cargaron los: {len(logs)}, logs desde el: {file_path}")
        return logs
    except json.JSONDecodeError as e:
        print(f"ERROR: el archivo {file_path}, no e sun Json valido")
        print(f"detalles: {e}")
        return None
    except IOError as e:
        print(f"ERROR: no se pudo leer el archivo: {file_path}")
        print(f"Detalles: {e}")
        print("Sugerencias: Revisar los permisos de lectura de archisvos")
        return None
    except Exception as e:
        print(f"ERROR: Ocurrió un error inesperado al procesar '{file_path}'.")
        print(f"Detalles del error: {e}")
        return None
if __name__ == "__main__":
    # Paso 1 debes estar seguro de que se generaron los logs y estan alamacenados en un arhcivo
    log_cargados = read_log_json("../../data/mis_logs.json")
    if log_cargados:
        print("Primer log cargado")
        print(log_cargados[0])
    else:
        print("No se pudieron cargar los logs")

def analyze_log_eventype(l1 : list):
    "Metodo que analisa los logs por eventos"

    if not l1:
        print(f"No hay logs en: {l1} registrados")
    contador_eventos = {}
    for log in l1:
        event_type = log.get("Evento")
        contador_eventos[event_type] = contador_eventos.get(event_type,0) +1

    print("---------Cuenta de los tipos de eventos----------")
    for event, count in sorted(contador_eventos.items(), key= lambda item: item[1], reverse= True):
        print(f"-{event}:{count}")

    return contador_eventos

def analyze_failed_login(logs_data : list, threshold : int = 3):
    """Analiza los logs para detectar intentos fallidos de inicio de sesion que excenden la cantidad
        args: 
            logs_data = es una lista que de diccionarios donde cada diccionariao sera un log
            threshold = es la cantidad maxima de intentos fallidos permitidos
        return:
            regresa un diccionario donde las claves seran los nombres de los usuarios y los valores
            seran el numero de intentos fallidos solo para los que excenden el limite
    """
    failed_attemps_by_user = defaultdict(int)
    alert = {}

    print("----Iniciando analisis de inicio de sesion ----")

    for log in logs_data:
        event_type = log.get('Evento')
        username = log.get('Usuario')
        if event_type == 'authentication.failure':
            if username:
                failed_attemps_by_user[username] += 1
                print(f"  [DEBUG] Intento fallido para: {username}. Total: {failed_attemps_by_user[username]}")

    print("---RESUMEN DE INTENTOS FALLIDOS---")
    if not failed_attemps_by_user:
        print("No se encontraron intentos fallidos en el log")
    else:
        for user, count in failed_attemps_by_user.items():
            if count >= threshold:
                alert[user] = count
                print(f"  [ALERTA] Usuario '{user}' tiene {count} intentos de login fallidos (max: {threshold}).")
    if not alert and failed_attemps_by_user:
        print(f"No se detectoron alertas de login fallidos que excendan el maximo {threshold}")
    print("---FIN DEL ANALISIS---")
    return alert

if __name__ == "__main__":
    print("---- INICIO DEL PROCESO DE LECTURA Y ANALISIS----")

    script_dir = os.path.dirname(os.path.abspath(__file__))

    log_file_to_read = os.path.join(script_dir, "..", "..", "data", "mis_logs.json")

    log_cargados = read_log_json(log_file_to_read)

    if log_cargados:
        print("Primer log cargar")
        print(log_cargados[0])
    
        analyze_log_eventype(log_cargados)
        failed_login_aletrs = analyze_failed_login(log_cargados,3)

        if failed_login_aletrs:
            print("---RESUMEN DE ALERTAS DE LOGIN FALLIDOS---")
            for user, count in failed_login_aletrs.items():
                print(f" ALERTA!!! usuario: {user}, con {count} intentos fallidos")
        else:
            print("No se detectaron alertas de login fallidas")
    else:
        print("No se pudieron cargar los logs")
    print("--- PROCESO DE ANALISIS Y LECTURA FINALIZADO")

