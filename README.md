# Cuentacuentos

## Descripción
Cuentacuentos es una aplicación web que utiliza la API de OpenAI para generar historias únicas basadas en una variedad de temas y con un número específico de personajes. Es perfecta para escritores en busca de inspiración, para entretener, o simplemente para explorar las capacidades creativas de la inteligencia artificial.

## Características
- Generación de historias basada en temas predefinidos.
- Personalización del número de personajes en las historias.
- Interfaz web amigable y fácil de usar.

## Tecnologías Utilizadas
- Python
- Flask
- OpenAI API

## Instalación

Clona el repositorio

```py
git clone https://github.com/joferte84/Cuentacuentos
```

Configura tus claves API de OpenAI en un archivo `.env`:

Primero, obtén tu clave API de OpenAI registrándote en su [plataforma](https://openai.com/api/). Una vez que tengas tu clave, crea un archivo `.env` en el directorio raíz del proyecto y modifica la siguiente línea en el script principal:
```py
openai.api_key = 'tu_clave_api_aquí'
```

Reemplaza `tu_clave_api_aquí` con tu clave API real de OpenAI.

## Configuración del Entorno Virtual

Se recomienda utilizar un entorno virtual para ejecutar este proyecto. Puedes configurar uno utilizando venv.

Navega al directorio de tu proyecto y ejecuta:
```py
python -m venv "nombre_de_tu_entorno"
```

## Activa el entorno virtual

En windows:
```py
.\venv\Scripts\activate
```

En Unix o MacOS:

```py
source venv/bin/activate
```

## Una vez activado el entorno virtual, instala las dependencias:

```py
pip install -r requirements.txt
```

## Uso
Para iniciar la aplicación, en tu terminal ejecuta:

```py
python cuentacuentos-1.py
```

Navega a `http://localhost:5000` en tu navegador para acceder a la aplicación.

Selecciona un tema, un número de personajes y después clickear en `Generar Historia`.
