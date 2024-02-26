import os
from archivo import Archivo
import csv
import re

class ArchivoCSV(Archivo):
    def __init__(self, ruta: str, nombre: str):
        self.ruta = ruta
        self.nombre = nombre

    def buscar_palabra(self, palabra: str) -> int:
        ruta_completa = os.path.join(self.ruta, self.nombre)
        try:
            with open(ruta_completa, 'r') as archivo:
                contenido = archivo.read()

                # Contar ocurrencias exactas de la palabra
                contador_palabra = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(palabra), contenido))
                return contador_palabra
        except FileNotFoundError:
            print(f"El archivo {self.nombre} no se encontró en la ruta {self.ruta}")
            return 0
        except Exception as e:
            print(f"Ocurrió un error al procesar el archivo {self.nombre}: {e}")
            return 0