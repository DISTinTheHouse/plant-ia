#  Plant-IA

[![PyPI version](https://img.shields.io/pypi/v/plant-ia?label=pypi)](https://pypi.org/project/plant-ia/)
![Tests](https://github.com/DISTinTheHouse/plant-ia/actions/workflows/tests.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)


**Plant-IA** es una librería en español pensada para programadores que trabajan con inteligencia artificial; Te permite estructurar prompts dinámicos de forma sencilla, elegante y reutilizable, ideal para integraciones con modelos de lenguaje como ChatGPT, Claude, LLaMA o asistentes personalizados.

---

## Instalación

```bash
pip install plant-ia
```

---

## ¿Qué hace?

Te permite crear plantillas con variables e inyectarlas fácilmente:

```python
from plant_ia import Plantilla

p = Plantilla("Hola {nombre}, ¿cómo estás hoy?")
print(p.rellenar(nombre="Alberto"))
# Resultado: Hola Alberto, ¿cómo estás hoy?")
```

---

## Uso en proyectos reales

Por ejemplo, puedes usar `plant-ia` para generar textos personalizados como correos profesionales, resúmenes automáticos o respuestas inteligentes:

```python
from plant_ia import Plantilla

correo = Plantilla(
    "Redacta un correo profesional dirigido a {cliente}, informando que su pedido {pedido_id} está {estatus} "
    "y será entregado el {fecha_entrega}. Agrega un tono cordial y profesional."
)

datos = {
    "cliente": "David R.",
    "pedido_id": "ORD-9083",
    "estatus": "en camino",
    "fecha_entrega": "12 de junio de 2025"
}

prompt = correo.rellenar(**datos)
print(prompt)
```

Este `prompt` puede usarse con cualquier modelo de lenguaje (como GPT, Claude, Mistral, etc.) o integrarse en sistemas de atención al cliente, generación de reportes, bots o automatización de tareas.

---

## ¿Por qué Plant-IA?

- ✅ Sintaxis simple y en español  
- ✅ Ligera, sin dependencias externas  
- ✅ Pensada para escalar y extenderse  
- ✅ Ideal para proyectos de inteligencia artificial, asistentes, bots o flujos automatizados  

---

## Extras (opcional)

Si deseas usr 'Plant-IA' junto con un modelo de lenguaje como ChatGPT:

```bash
pip install openai
```

```bash
from plant_ia import Plantilla
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

correo = Plantilla(
    "Redacta un correo profesional dirigido a {colaborador}, reconociendo su valiosa contribución como {rol} "
    "en el proyecto '{proyecto}'. Destaca brevemente la importancia de su trabajo y los avances logrados desde su inicio el {fecha_inicio}. "
    "Usa un tono institucional, motivador y bien estructurado."
)

datos = {
    "colaborador": "Iván N. Rodríguez",
    "rol": "Lead Backend Developer",
    "proyecto": "Oracle Cloud Infrastructure (OCI) Gen AI Services",
    "fecha_inicio": "1 de marzo de 2024"
}

prompt = correo.rellenar(**datos)

respuesta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente profesional del área de Recursos Humanos."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.6
)

print(respuesta.choices[0].message.content)

```


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
