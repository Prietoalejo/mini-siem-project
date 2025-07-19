import json
import os

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

    if not l1:
        print(f"No hay logs en: {l1} registrados")
    
    contador_eventos = {}
    for log in l1:
        event_type = log.get("Evento")
        contador_eventos[event_type] = contador_eventos.get(event_type,0) +1

    print("---------Cuenta de los tipos de eventos----------")
    for event, count in sorted(contador_eventos.items(), key= lambda item: item[1], reverse= True):
        print(f"-{event}:ñ{count}")

    return contador_eventos

