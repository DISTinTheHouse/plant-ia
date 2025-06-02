class Plantilla:
    """
    Clase para estructurar prompts con variables dinámicas.
    Ejemplo: Plantilla("Hola {nombre}, ¿cómo estás?").rellenar(nombre="Luis")
    """
    def __init__(self, texto: str):
        self.texto = texto

    def rellenar(self, **valores) -> str:
        try:
            return self.texto.format(**valores)
        except KeyError as e:
            raise ValueError(f"Falta la variable: {e}")
