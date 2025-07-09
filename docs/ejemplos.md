
# 💡 Ejemplos de uso con Plant-IA

Este archivo muestra cómo utilizar `Plant-IA` desde lo más básico hasta casos aplicados a proyectos reales.

---

### Saludo simple para asistentes virtuales
```python
from plant_ia import Plantilla

saludo = Plantilla("Hola {nombre}, ¿en qué puedo ayudarte hoy?")
print(saludo.rellenar(nombre="Guillermo"))
# Hola Guillermo, ¿en qué puedo ayudarte hoy?
```

### Generador de nombre de archivo
```python
from plant_ia import Plantilla

archivo = Plantilla("reporte_{mes}_{usuario}.pdf")
print(archivo.rellenar(mes="julio", usuario="jesus"))
# reporte_julio_jesus.pdf
```

---

##  Intermedio

### Email automatizado de confirmación
```python
from plant_ia import Plantilla

correo = Plantilla("Hola {cliente}, tu cita está confirmada para el {fecha} a las {hora}.")
print(correo.rellenar(cliente="Carlos", fecha="10 de julio", hora="11:00 AM"))
```

### Enlace dinámico para login seguro
```python
from plant_ia import Plantilla

url = Plantilla("https://empresa.com/{usuario}/login?token={token}")
print(url.rellenar(usuario="ana.solis", token="ABC123XYZ"))
```

---

## Avanzado

### Generación de correo profesional con IA (ChatGPT)
```python
from plant_ia import Plantilla
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

correo = Plantilla(
    "Redacta un correo profesional dirigido a {colaborador}, reconociendo su desempeño como {rol} "
    "en el proyecto '{proyecto}'. Menciona su impacto y motívalo a seguir contribuyendo. "
    "Usa un tono institucional, claro y profesional."
)

datos = {
    "colaborador": "Laura Ramírez",
    "rol": "Engineering Manager",
    "proyecto": "Desarrollo de la plataforma OCI Next-Gen"
}

prompt = correo.rellenar(**datos)

respuesta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres parte del equipo de Recursos Humanos de Oracle."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.6
)

print(respuesta.choices[0].message.content)
```

---


## 🧪 Ideas para escalar

- Agregar selector de tono (formal, casual, inspirador).
- Exportar resultados como PDF o email.
- Integrar con sistemas internos, CRMs o APIs.
- Usar en dashboards, chatbots o pipelines de IA.
