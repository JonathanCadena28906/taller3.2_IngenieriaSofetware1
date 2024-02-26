import os
from archivo_txt import ArchivoTXT
from archivo_xml import ArchivoXML
from archivo_json import ArchivoJSON
from archivo_csv import ArchivoCSV

class ContadorPalabras:
    def __init__(self, ruta: str):
        self.ruta = ruta

    def extraerArchivos(self):
        
        try:
            archivos_en_carpeta = os.listdir(self.ruta)
        except FileNotFoundError:
            print(f"La carpeta '{self.ruta}' no se encuentra en el sistema.")
        return None
 
        archivos = []
        for nombre_archivo in archivos_en_carpeta:
            extension = os.path.splitext(nombre_archivo)[1].lower()
            if extension in ['.txt']:
                archivo = ArchivoTXT(self.ruta, nombre_archivo)
            elif extension in ['.xml']:
                archivo = ArchivoXML(self.ruta, nombre_archivo)
            elif extension in ['.json']:
                archivo = ArchivoJSON(self.ruta, nombre_archivo)
            elif extension in ['.csv']:
                archivo = ArchivoCSV(self.ruta, nombre_archivo)
            else:
                continue  # Ignorar archivos con extensiones no reconocidas
            archivos.append(archivo)

        if not archivos:
            print("No se encontraron archivos de texto en la carpeta.")
            return None

        return archivos

    def contar_palabras(self, palabra: str) -> None:
        archivos = self.extraerArchivos()
        
        if archivos is None:
            return

        contador_total = 0
        for archivo in archivos:
            contador_palabra = archivo.buscar_palabra(palabra)
            print(f"La palabra '{palabra}' aparece {contador_palabra} veces en el archivo {archivo.nombre}")
            contador_total += contador_palabra

        print(f"La palabra '{palabra}' aparece un total de {contador_total} veces en todos los archivos de la carpeta.")
