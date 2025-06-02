# 🚀 Guía Rápida

Plant-IA te permite estructurar mensajes dinámicos con placeholders.

## Crear una plantilla

```python
from plant_ia import Plantilla

plantilla = Plantilla("Hola {nombre}, bienvenido a la app.")
print(plantilla.rellenar(nombre="Luis"))
```

Puedes usar tantos valores como necesites:

```python
p = Plantilla("Pedido {id} para {cliente}")
print(p.rellenar(id=42, cliente="Carlos"))
```