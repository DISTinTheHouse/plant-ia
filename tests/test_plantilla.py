from plant_ia import Plantilla

def test_rellenar():
    plantilla = Plantilla("Hola {nombre}, bienvenido a Plant-IA.")
    resultado = plantilla.rellenar(nombre="Carlos")
    assert resultado == "Hola Carlos, bienvenido a Plant-IA."
