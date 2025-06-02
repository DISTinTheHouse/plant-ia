
# 💡 Ejemplos

Este archivo te mostrará cómo utilizar `Plant-IA` desde lo más básico hasta casos avanzados.  

---

## 🧑‍🎓 Nivel Principiante

### Saludo para asistentes virtuales
```python
Plantilla("Hola {nombre}, ¿qué puedo hacer por ti hoy?")
```

### Email automatizado
```python
Plantilla("Estimado {cliente}, su pedido {id} está en camino.")
```

### Nombre de archivo generado
```python
Plantilla("factura_{fecha}_{cliente}.pdf")
```

---

## ⚙️ Nivel Intermedio

### Mensaje de confirmación con múltiples variables
```python
Plantilla("Hola {nombre}, confirmamos tu cita el {dia} a las {hora}.")
```

### Generador de mensajes de marketing
```python
Plantilla("¡Hola {nombre}! Descubre nuestras ofertas exclusivas en {producto}. Solo por hoy.")
```

### Composición de URLs dinámicas
```python
Plantilla("https://miapp.com/{usuario}/dashboard?token={token}")
```

---

## 🧠 Nivel Avanzado

### Secuencia tipo prompt pipeline para IA
```python
# Paso 1: Plantilla base
entrada_usuario = Plantilla("Usuario: {pregunta}")
pregunta_formateada = entrada_usuario.rellenar(pregunta="¿Qué es Python?")

# Paso 2: Encabezado de contexto
contexto = Plantilla("Sistema: Eres un asistente experto en programación. {input}")
entrada_final = contexto.rellenar(input=pregunta_formateada)

print(entrada_final)
```

### Generador de mensajes formales con tono variable
```python
Plantilla("Hola {nombre}, lamento informarte que {asunto}. Atte, {equipo}.")
```

---

## 📤 Bonus: Cadenas desde CSV
```python
import csv
from plant_ia import Plantilla

with open('prompts.csv', encoding='utf-8') as f:
    lector = csv.DictReader(f)
    for fila in lector:
        plantilla = Plantilla(fila['mensaje'])
        print(plantilla.rellenar(nombre=fila['nombre']))
```

---

## 🧪 ¿Ideas para escalar?
- Agregar selector de tono (formal, casual, técnico).
- Exportar a PDF, HTML o email.
- Crear múltiples plantillas por flujo.
- Integrar con herramientas como Zapier, Make o APIs.
