"""
    Manejo de Excepciones
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error, para el valor ingresado %s, el valor es menor a 20" %(self.valor)
