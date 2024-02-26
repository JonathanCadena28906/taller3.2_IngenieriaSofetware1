import os

class Archivo:
    def __init__(self, ruta: str, nombre: str):
        self.ruta = ruta
        self.nombre = nombre

    def buscar_palabra(self, palabra: str) -> int:
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}"
