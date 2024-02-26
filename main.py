from ContadorPalabras import ContadorPalabras

def main():
    ruta_carpeta = input("Ingrese la ruta completa de la carpeta: ")
    palabra_buscar = input("Ingrese la palabra que desea buscar en los archivos: ")

    contador = ContadorPalabras(ruta_carpeta)
    contador.contar_palabras(palabra_buscar)

if __name__ == "__main__":
    main()
