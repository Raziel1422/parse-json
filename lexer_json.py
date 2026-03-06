import re
import sys

# Lista de tipos de token y su patron
patrones_token = [
    ("LLAVE_IZQ", r"\{"),
    ("LLAVE_DER", r"\}"),
    ("DOS_PUNTOS", r":"),
    ("COMA", r","),
    ("NUMERO", r"\d+"),
    ("CADENA", r'"[^"]*"'),
    ("ESPACIOS", r"\s+"),
    ("ERROR", r".")
]

# Se construye una expresion regular general con todos los patrones
patron_general = "|".join(
    "(?P<%s>%s)" % (nombre, patron)
    for nombre, patron in patrones_token
)


def obtener_tokens(texto):
    """
    Recorre un texto y genera la lista de tokens encontrados.

    Esta funcion ignora los espacios en blanco y produce una lista
    de tuplas con la forma:
        (tipo_token, valor)

    Args:
        texto (str): Contenido del archivo a analizar.

    Returns:
        list: Lista de tokens encontrados.

    Raises:
        Exception: Si se encuentra un caracter no valido.
    """
    tokens = []

    for coincidencia in re.finditer(patron_general, texto):
        tipo = coincidencia.lastgroup
        valor = coincidencia.group()

        if tipo == "ESPACIOS":
            continue

        if tipo == "ERROR":
            raise Exception("Caracter no valido: " + valor)

        tokens.append((tipo, valor))

    return tokens


def leer_archivo(ruta):
    """
    Lee el contenido completo de un archivo de texto.

    Args:
        ruta (str): Ruta del archivo que se desea leer.

    Returns:
        str: Contenido del archivo.
    """
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()
    return contenido


def main():
    """
    Funcion principal del programa.

    Lee la ruta de un archivo desde los argumentos de la linea de comandos,
    obtiene los tokens del contenido y los muestra en pantalla.

    Uso:
        python lexer_json.py archivo.json
    """
    if len(sys.argv) != 2:
        print("Uso: python lexer_json.py archivo.json")
        return

    ruta = sys.argv[1]

    try:
        texto = leer_archivo(ruta)
        tokens = obtener_tokens(texto)

        print("Tokens encontrados:")
        for token in tokens:
            print(token)

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
