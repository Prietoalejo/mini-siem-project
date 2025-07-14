# 🚀 Mini-SIEM: Mi Viaje para Construir un Cerebro de Seguridad Básico

¡Hola! Soy Alejandro, y este repositorio documenta mi primer gran proyecto de ingeniería de sistemas y ciberseguridad: un **Mini-SIEM**. Aún estoy explorando y aprendiendo un montón, pero la idea es construir un sistema que pueda masticar logs, encontrar cosas interesantes y guardarlas. Esto es un trampolín para entender cómo funciona la seguridad a un nivel más práctico.

---

## 🎯 **¿Por Qué Estoy Haciendo Esto? Mis Ganas de Aprender**

Este proyecto es mi area de entrenamiento personal. Con él, busco:

* **Dominar Python:** Ir más allá de los scripts básicos. Quiero que Pandas y el manejo de datos (especialmente JSON) sean mi segunda naturaleza.
* **Aprender mas de PostgreSQL y SQL:** Entender cómo se almacenan y se sacan datos de una base de datos relacional de forma eficiente y segura.
* **Uniendo Mundos (Python y C++):** Explorar cómo Python puede hablar con código más de bajo nivel en C++ para cuando necesite ese empuje extra de rendimiento o control.
* **Pensar como un Hacker (para defenderme):** Aprender sobre vulnerabilidades comunes (como la inyección SQL) para entender cómo prevenirlas y construir sistemas más robustos.
* **Escribir Código de Calidad:** Poner en práctica principios de diseño de software (como SOLID) desde el principio, incluso si al inicio no sale perfecto. Quiero que mi código sea legible y mantenible.
* **Automatizar Tareas:** Hacer que mi sistema trabaje solo.
* **Construir mi Portafolio:** Dejar evidencia de mi capacidad para aprender, resolver problemas y completar proyectos. Esto es lo que quiero mostrar.

---

## 🛠️ **Mis Herramientas de Batalla**

Aquí está el arsenal que estoy usando en este proyecto:

* **Python 3:** Mi lenguaje principal para la lógica, el análisis y la automatización.
    * **Pandas:** Para procesar datos de logs como si fueran hojas de cálculo.
    * **`psycopg2-binary`:** El "traductor" de Python para hablar con mi base de datos PostgreSQL.
    * **`requests`:** Por si algún día necesito traer datos de alguna API web (¡nunca se sabe!).
* **PostgreSQL:** Mi base de datos para guardar todos los logs, alertas y la información relevante.
* **SQL:** El idioma para preguntarle cosas a mi base de datos.
* **C++:** Lo estoy incorporando para algunas tareas que necesitan ser súper rápidas o muy cerca del hardware.
* **Git & GitHub:** Para llevar un registro de cada cambio que hago y para que mi código sea público y portable.
* **Notion / Craft:** (Mi cuaderno digital para apuntes, enlaces y lluvias de ideas. No está en el repo, pero es clave para mi proceso).

---

## 🚀 **¡Manos a la Obra! Configurando el Proyecto (Paso a Paso para Mi y para Ti)**

Si quieres replicar o echar un ojo a este proyecto, aquí te dejo mi propia guía de configuración:

1.  **Clona el Repositorio (y métete en la carpeta):**
    ```bash
    git clone [https://github.com/tu_usuario/mini-siem-project.git](https://github.com/tu_usuario/mini-siem-project.git)
    cd mini-siem-project
    ```
    *(**Nota para mí:** ¡No olvidar cambiar `tu_usuario` por el mío!)*

2.  **Prepara el Entorno Python (¡Con el `venv` para no armar un desastre!):**
    * Asegúrate de tener **Python 3.x** instalado.
    * Dentro de la carpeta del proyecto, crea y activa tu entorno virtual:
        ```bash
        python -m venv venv
        # Si estás en Windows (PowerShell/CMD):
        .\venv\Scripts\activate
        # Si estás en macOS (Terminal):
        source venv/bin/activate
        ```
    * Instala todas las librerías que estoy usando (`requirements.txt`):
        ```bash
        pip install -r requirements.txt
        ```

3.  **Instala PostgreSQL (Mi Base de Datos de Confianza):**
    * Descárgalo e instálalo desde [postgresql.org/download/](https://www.postgresql.org/download/) (elige tu sistema: Windows o macOS).
    * **¡Súper importante!** Crea una base de datos llamada `seguridad_logs` y un usuario `siem_user` con una contraseña que no se me olvide. Y dale los permisos necesarios para trabajar con esa DB. `pgAdmin` es útil para esto.

4.  **Prepara tu Compilador C++:**
    * **En Windows:** Recomiendo instalar **MinGW-w64** para tener `g++` disponible en la terminal. Otra opción es instalar Visual Studio Community y seleccionar los componentes de C++.
    * **En macOS:** Abre la terminal y ejecuta `xcode-select --install`. Esto te dará `clang++`.

5.  **Configuración de la Base de Datos (¡NUNCA subas contraseñas a GitHub!):**
    * Necesito crear un archivo `config/db_config.ini` (o usar variables de entorno) para guardar las credenciales de mi base de datos (host, puerto, usuario, contraseña). **Este archivo NO se sube al repositorio porque ya está en mi `.gitignore`.**
    * **Ejemplo de cómo se vería `config/db_config.ini` (solo para referencia, no copiar credenciales reales aquí):**
        ```ini
        [postgresql]
        host=localhost
        port=5432
        database=seguridad_logs
        user=siem_user
        password=tu_contraseña_segura
        ```

---

## 📁 **¿Cómo Está Organizado Todo? (Mi Mapa del Tesoro)**

Aquí te dejo cómo estoy estructurando mi código y archivos. Esto puede crecer y cambiar, pero esta es la idea inicial:

mini-siem-project/
├── src/                       # Aquí va todo mi código Python y C++
│   ├── core/                  # La lógica principal del SIEM (cómo procesa los logs, etc.)
│   ├── db_manager/            # Código para hablar con la base de datos
│   ├── utils/                 # Herramientas pequeñas que usaré en varios lugares (ej. generador de logs)
│   └── cpp_components/        # Mis partes de código escritas en C++
├── data/                      # Aquí pondré mis archivos de logs simulados de ejemplo
├── config/                    # Para archivos de configuración (¡donde van las cosas sensibles!)
├── sql/                       # Mis scripts SQL para crear las tablas de la base de datos
├── .gitignore                 # ¡Súper importante! Le dice a Git qué archivos ignorar (como mi venv/ o las contraseñas).
├── README.md                  # El archivo que estás leyendo ahora (mi guía y carta de presentación).
└── requirements.txt           # La lista de todas las librerías de Python que usa este proyecto.


---

## 🗺️ **Mi Hoja de Ruta Personal (¡Dónde Estoy y Hacia Dónde Voy!)**

Esta es la lista de tareas que me he propuesto. A medida que las complete, las marcaré.

* [x] **Fase 1: Preparando el Terreno y Dominando Python**
    * [x] Configuración inicial del repositorio Git, `venv` y las dependencias Python.
    * [ ] **Dominar Diccionarios y JSON en Python:** Necesito ser un experto manipulando estos formatos.
    * [ ] **Primeros Pasos con Pandas:** Aprender a cargar datos y hacer análisis sencillos.
    * [ ] **Hacer mi Código a Prueba de Balas:** Implementar manejo de errores y excepciones.
    * [ ] **¡Tarea Divertida!** Crear `src/utils/log_generator.py` para inventar logs de seguridad.
    * [ ] **¡Tarea Clave!** Crear `src/core/log_processor_basic.py` para leer y analizar esos logs que genere.

* [ ] **Fase 2: Construyendo la Base de Datos (Mi Memoria del SIEM)**
    * [ ] Instalar y configurar PostgreSQL en mi máquina.
    * [ ] Aprender SQL de verdad: cómo crear tablas y hacer las consultas que necesito.
    * [ ] **Conectar Python y PostgreSQL:** Hacer que mis scripts puedan guardar y sacar datos de la base de datos.
    * [ ] **Tarea:** Escribir el script SQL (`sql/create_tables.sql`) para mis tablas.
    * [ ] **Tarea:** Crear el módulo `src/db_manager/db_ops.py` con funciones para interactuar con la DB.
    * [ ] **Tarea:** Modificar el procesador de logs para que guarde los resultados en la base de datos.

* [ ] **Fase 3: Añadiendo Potencia con C++**
    * [ ] **Punteros y Memoria en C++:** Entender cómo C++ maneja las cosas a bajo nivel.
    * [ ] **Integrar C++ con Python:** Lograr que Python pueda usar funciones compiladas en C++.
    * [ ] **Tarea:** Crear un pequeño componente C++ (`src/cpp_components/ip_validator.cpp`) para, por ejemplo, validar IPs de forma súper rápida.

* [ ] **Fase 4: Pulido y Pensamiento de Seguridad**
    * [ ] **Código más Limpio con SOLID:** Aplicar principios de diseño para que mi código sea más fácil de entender y mantener.
    * [ ] **Entendiendo Vulnerabilidades:** Investigar el OWASP Top 10 y, especialmente, cómo prevenir la inyección SQL.

---

## 💭 **Mis Reflexiones y Aprendizajes (¡Esto es un Diario Abierto!)**

* *Aquí iré poniendo mis notas honestas: si algo fue más difícil de lo esperado, un "¡Eureka!" que tuve, un error que me costó horas o una solución genial que encontré. Esto es para mí, para recordar el camino.*
* *Por ejemplo, hoy aprendí la importancia del `.gitignore` para no subir mi `venv/` y cómo `pip install` descarga todo de golpe. ¡Increíble!*

---

## 📧 **Contacto**

Puedes encontrarme en mi perfil de GitHub. ¡Abierto a comentarios y sugerencias!
