#  Plant-IA

[![PyPI version](https://img.shields.io/pypi/v/plant-ia?label=pypi)](https://pypi.org/project/plant-ia/)
![Tests](https://github.com/DISTinTheHouse/plant-ia/actions/workflows/tests.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)


**Plant-IA** es una librería en español diseñada para ayudarte a estructurar prompts dinámicos de forma sencilla, elegante y reutilizable. Ideal para integraciones con modelos de lenguaje como ChatGPT, Claude o Llama.

---

## ¿Qué hace?

Te permite crear plantillas con variables e inyectarlas fácilmente:

```python
from plant_ia import Plantilla

p = Plantilla("Hola {nombre}, ¿cómo estás hoy?")
print(p.rellenar(nombre="Luis"))
# Resultado: Hola Luis, ¿cómo estás hoy?")
```

---

## Instalación

```bash
pip install plant-ia
```

---

## ¿Por qué Plant-IA?

- ✅ Sintaxis simple y en español  
- ✅ Ligera, sin dependencias externas  
- ✅ Pensada para escalar y extenderse  
- ✅ Ideal para proyectos de inteligencia artificial, asistentes, bots o flujos automatizados  

---

## Estructura del Proyecto

```
plant_ia/
├── __init__.py        # Lógica principal
tests/
└── test_plantilla.py  # Pruebas unitarias
```

---

## 🤝 Contribuciones

¿Quieres aportar? ¡Abre un issue o haz un pull request!  
Plant-IA está abierta a crecer junto a la comunidad hispana.

---

## 🧑‍💻 Autor

Desarrollado por **Jesús Ibarra**  
📦 Publicado en PyPI: [plant-ia](https://pypi.org/project/plant-ia/)

---

## 📝 Licencia

MIT © 2025 – Plant-IA
