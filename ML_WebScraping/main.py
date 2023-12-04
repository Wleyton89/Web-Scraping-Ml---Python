import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class Scraper():

    def menu(self):
        # Menú para que el usuario elija un país
        menu_paises = ("""
    Escoge el país:
    1. Argentina
    2. Bolivia
    3. Brasil
    4. Chile
    5. Colombia
    6. Costa Rica
    7. Dominicana
    8. Ecuador
    9. Guatemala
    10. Honduras
    11. México
    12. Nicaragua
    13. Panamá
    14. Paraguay
    15. Perú
    16. Salvador
    17. Uruguay
    18. Venezuela
        """)

        # Lista de opciones válidas
        valid_options = list(range(1, 19))

        # Bucle hasta que se elija una opción válida
        while True:
            print(menu_paises)
            opcion = int(input('Número de país (Ejemplo: 5): '))

            if opcion in valid_options:
                # Asignar la URL base según la opción seleccionada
                urls = {
                    1: 'https://listado.mercadolibre.com.ar/',
                    2: 'https://listado.mercadolibre.com.bo/',
                    3: 'https://listado.mercadolibre.com.br/',
                    4: 'https://listado.mercadolibre.cl/',
                    5: 'https://listado.mercadolibre.com.co/',
                    6: 'https://listado.mercadolibre.com.cr/',
                    7: 'https://listado.mercadolibre.com.do/',
                    8: 'https://listado.mercadolibre.com.ec/',
                    9: 'https://listado.mercadolibre.com.gt/',
                    10: 'https://listado.mercadolibre.com.hn/',
                    11: 'https://listado.mercadolibre.com.mx/',
                    12: 'https://listado.mercadolibre.com.ni/',
                    13: 'https://listado.mercadolibre.com.pa/',
                    14: 'https://listado.mercadolibre.com.py/',
                    15: 'https://listado.mercadolibre.com.pe/',
                    16: 'https://listado.mercadolibre.com.sv/',
                    17: 'https://listado.mercadolibre.com.uy/',
                    18: 'https://listado.mercadolibre.com.ve/',
                }

                self.base_url = urls[opcion]
                break
            else:
                print("Escoge un número del 1 al 18")

    def menu_paginas(self):
        # Menú para que el usuario elija la cantidad de páginas a scrapear
        while True:
            try:
                cantidad_paginas = int(input("\nIngresa la cantidad de páginas para hacer el scraping: "))
                if cantidad_paginas > 0:
                    self.cantidad_paginas = cantidad_paginas
                    break
                else:
                    print("La cantidad de páginas debe ser mayor a 0.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def scraping(self):
        # Búsqueda del usuario
        product_name = input("\nProducto: ")
        # Limpiar la entrada del usuario
        cleaned_name = product_name.replace(" ", "-").lower()
        # Crear las URL para hacer scraping
        urls = [self.base_url + cleaned_name]

        # Preguntar al usuario la cantidad de páginas a scrapear
        self.menu_paginas()

        # Crear las URLs adicionales para páginas adicionales
        for i in range(1, self.cantidad_paginas):
            urls.append(f"{self.base_url}{cleaned_name}_Desde_{i * 50 + 1}_NoIndex_True")

        # Crear una lista para guardar los datos
        self.data = []
        # Crear contador
        c = 1
            
        # Iterar sobre cada URL
        for i, url in enumerate(urls, start=1):
            # Obtener el HTML de la página
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
                
            # Obtener todos los productos
            content = soup.find_all('li', class_='ui-search-layout__item')
            
            # Verificar si no hay contenido para hacer scraping
            if not content:
                print("\nTerminó el scraping.")
                break

            print(f"\nScrapeando página número {i}. {url}")
            
            # Iteración para hacer scraping de los productos
            for post in content:
                # Obtener el título
                title = post.find('h2').text
                # Obtener el precio
                price = post.find('span', class_='andes-money-amount__fraction').text
                # Obtener el enlace al producto
                post_link = post.find("a")["href"]
                # Obtener el enlace de la imagen
                try:
                    img_link = post.find("img")["data-src"]
                except:
                    img_link = post.find("img")["src"]
                
                # Guardar en un diccionario
                post_data = {
                    "Título": title,
                    "Precio": price,
                    "Enlace al Producto": post_link,
                    "Enlace de la Imagen": img_link            
                }
                # Guardar los diccionarios en una lista
                self.data.append(post_data)
                c += 1

    def export_to_csv(self):
        # Exportar a un archivo CSV con nombres de columnas en español y codificación UTF-8
        df = pd.DataFrame(self.data, columns=["Título", "Precio", "Enlace al Producto", "Enlace de la Imagen"])
        df.to_csv(r"data/mercadolibre_scraped_data.csv", sep=";", index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    s = Scraper()
    s.menu()
    s.scraping()
    s.export_to_csv()
