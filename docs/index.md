# Bienvenido a Plant-IA

**Plant-IA** es una librería en español para estructurar prompts dinámicos de forma clara, rápida y reutilizable. Diseñada especialmente para proyectos que usan modelos de lenguaje como ChatGPT.

## 📦 Instalación

```bash
pip install plant-ia
```

## 🚀 Ejemplo de uso

```python
from plant_ia import Plantilla

p = Plantilla("Hola {nombre}, ¿cómo estás hoy?")
print(p.rellenar(nombre="Luis"))
```
