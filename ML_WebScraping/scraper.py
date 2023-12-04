import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

class Scraper:

    def __init__(self):
        self.base_url = ""
        self.product_name = ""
        self.page_count = 1
        self.data = []

    def set_country(self, option):
        urls = {
            1: 'https://listado.mercadolibre.com.ar/',
            # Agrega las demás URLs según la lista de países
        }
        self.base_url = urls.get(option, '')
        if not self.base_url:
            raise ValueError("Opción de país no válida.")

    def set_product_name(self, product_name):
        self.product_name = product_name.replace(" ", "-").lower()

    def set_page_count(self, page_count):
        self.page_count = page_count

    def scraping(self):
        urls = [f"{self.base_url}{self.product_name}"]
        for i in range(1, self.page_count):
            urls.append(f"{self.base_url}{self.product_name}_Desde_{i * 50 + 1}_NoIndex_True")

        self.data = []

        for i, url in enumerate(urls, start=1):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('li', class_='ui-search-layout__item')

            if not content:
                print("\nTerminó el scraping.")
                break

            print(f"\nScrapeando página número {i}. {url}")

            for post in content:
                title = post.find('h2').text
                price = post.find('span', class_='andes-money-amount__fraction').text
                post_link = post.find("a")["href"]
                try:
                    img_link = post.find("img")["data-src"]
                except:
                    img_link = post.find("img")["src"]

                post_data = {
                    "Título": title,
                    "Precio": price,
                    "Enlace al Producto": post_link,
                    "Enlace de la Imagen": img_link
                }
                self.data.append(post_data)

    def export_to_csv(self):
        # Asegúrate de que el directorio exista, si no, créalo
        data_directory = os.path.join(os.path.dirname(__file__), 'data')
        os.makedirs(data_directory, exist_ok=True)

        # Exportar a un archivo CSV con nombres de columnas en español y codificación UTF-8
        df = pd.DataFrame(self.data, columns=["Título", "Precio", "Enlace al Producto", "Enlace de la Imagen"])
        csv_path = os.path.join(data_directory, 'mercadolibre_scraped_data.csv')
        df.to_csv(csv_path, sep=";", index=False, encoding='utf-8-sig')
        return csv_path

