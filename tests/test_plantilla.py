from plant_ia import Plantilla

def test_simple_reemplazo():
    p = Plantilla("Hola {nombre}")
    assert p.rellenar(nombre="Ana") == "Hola Ana"

def test_reemplazo_multiple():
    p = Plantilla("Hola {nombre}, hoy es {dia}")
    assert p.rellenar(nombre="Luis", dia="lunes") == "Hola Luis, hoy es lunes"

def test_variable_faltante():
    p = Plantilla("Hola {nombre}")
    try:
        p.rellenar()
        assert False  # No debería llegar aquí
    except ValueError as e:
        assert "Falta la variable" in str(e)
