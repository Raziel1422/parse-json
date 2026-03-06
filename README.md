# JSON Parser Simplificado

Este repositorio contiene una implementación sencilla de un **analizador léxico (lexer)** y un **analizador sintáctico (parser)** en Python para reconocer una versión simplificada del formato **JSON**.

El objetivo del proyecto es comprender cómo una **gramática libre de contexto** puede implementarse mediante un **parser descendente recursivo**.

Este material se utiliza como parte de una práctica del curso de **Teoría Matemática de la Computación**.

---

# ¿Por qué JSON?

**JSON (JavaScript Object Notation)** es uno de los formatos más utilizados para el intercambio de información entre sistemas.

Se utiliza ampliamente en:

- APIs REST
- aplicaciones web
- microservicios
- sistemas distribuidos

Un objeto JSON está formado por **pares clave–valor**.

Ejemplo simple:

```json
{"nombre":"Juan"}
