# Web-Scraping-Ml---Python

```markdown
# Proyecto de Web Scraping con Flask

Este proyecto tiene como objetivo realizar web scraping en el sitio web de MercadoLibre y mostrar los resultados en un archivo CSV. La aplicación, creada con Flask, permite a los usuarios ingresar un producto y seleccionar un país para buscar información sobre el mismo en MercadoLibre. Los resultados del web scraping se almacenan en un archivo CSV para su fácil acceso y análisis.

## Funcionalidades

- **Búsqueda de Productos:** Los usuarios pueden ingresar el nombre de un producto y seleccionar el país para buscar información en MercadoLibre.
- **Web Scraping:** La aplicación realiza web scraping para obtener información detallada sobre el producto, incluyendo títulos, precios, enlaces a productos y enlaces a imágenes.
- **Exportación a CSV:** Los resultados del web scraping se exportan a un archivo CSV para su posterior análisis.

## Integrantes del Proyecto

- **William Leyton:** Desarrollador principal, responsable de la implementación del web scraping y la lógica de la aplicación.
- **Alejandro Leyton:** Desarrollador Colaborador, contribuyó al diseño de la interfaz web y la estructura general del proyecto.

## Requisitos

- Python 3.x
- Flask
- requests
- BeautifulSoup
- pandas

## Configuración

1. Clona el repositorio:

   ```bash
   git clone https://github.com/TuUsuario/ProyectoWebScraping.git
   cd ProyectoWebScraping
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   # En Windows: venv\Scripts\activate
   # En Linux/Mac: source venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

   Visita [http://localhost:5000](http://localhost:5000) en tu navegador.

## Uso

1. Accede a la aplicación web.
2. Ingresa el nombre del producto y selecciona el país.
3. Selecciona la cantidad de páginas a scrapear.
4. Haz clic en "Buscar" y espera a que se completen las operaciones de web scraping.
5. Los resultados se exportarán automáticamente a un archivo CSV ubicado en la carpeta `data`.

## Contribuciones

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes una mejora, por favor, abre un problema o envía una solicitud de extracción.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).
```

Recuerda reemplazar `TuUsuario` en la URL del repositorio con tu nombre de usuario de GitHub.
