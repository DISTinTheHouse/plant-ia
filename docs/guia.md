
# Guía Rápida de Uso Empresarial con `Plant-IA`

Esta guía te muestra cómo usar `Plant-IA` en contextos empresariales reales, como **contaduría** y **tecnología**, generando mensajes profesionales personalizados o prompts para modelos como ChatGPT.

---

## Escenario 1: Contaduría — Notificación de factura generada

### 🎯 Objetivo
Enviar un mensaje automatizado a un cliente cuando su factura está lista, incluyendo el monto, la fecha y el número de folio.

### ✅ Paso a paso

```python
from plant_ia import Plantilla

# 1. Definir la plantilla con variables
factura = Plantilla(
    "Estimado {cliente}, su factura con folio {folio} por un monto de ${monto} ha sido generada el {fecha}. "
    "Gracias por confiar en nosotros."
)

# 2. Datos reales
datos = {
    "cliente": "Ana Torres",
    "folio": "FAC-202507",
    "monto": "2,350.75",
    "fecha": "09 de julio de 2025"
}

# 3. Inyectar datos en la plantilla
mensaje = factura.rellenar(**datos)

# 4. Imprimir o enviar por correo
print(mensaje)
```

#### 🧾 Resultado:
```
Estimado Ana Torres, su factura con folio FAC-202507 por un monto de $2,350.75 ha sido generada el 09 de julio de 2025. Gracias por confiar en nosotros.
```

---

## Escenario 2: Tecnología (Oracle Tech) — Evaluación de desempeño con ChatGPT

### 🎯 Objetivo
Redactar un correo formal para reconocer la labor de un colaborador técnico en un proyecto de infraestructura.

### ✅ Paso a paso

```python
from plant_ia import Plantilla
from openai import OpenAI
import os

# 1. Cliente OpenAI con clave segura
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Definir plantilla empresarial
plantilla = Plantilla(
    "Redacta un correo profesional dirigido a {colaborador}, reconociendo su valiosa contribución como {rol} "
    "en el proyecto '{proyecto}'. El correo debe destacar su impacto desde su incorporación el {fecha_inicio}, "
    "usando un tono institucional, técnico y motivador."
)

# 3. Datos personalizados
datos = {
    "colaborador": "Carlos Medina",
    "rol": "Ingeniero Cloud",
    "proyecto": "Migración a Oracle Autonomous DB",
    "fecha_inicio": "2 de mayo de 2025"
}

# 4. Generar prompt dinámico
prompt = plantilla.rellenar(**datos)

# 5. Enviar prompt a ChatGPT
respuesta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente profesional de Recursos Humanos especializado en tecnología."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.6
)

# 6. Mostrar resultado
print(respuesta.choices[0].message.content)
```

---
