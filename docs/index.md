# Bienvenido a Plant-IA

**Plant-IA** es una librería escrita en español diseñada para facilitar la creación de prompts dinámicos. Es ideal para integraciones con modelos de lenguaje como ChatGPT, Claude o Llama, especialmente en entornos empresariales donde la generación de contenido automatizado debe ser clara, profesional y reutilizable.

## Instalación

```bash
pip install plant-ia
```

## Ejemplo práctico

A continuación, un ejemplo en un contexto corporativo para un equipo de Recursos Humanos en una empresa tecnológica como Oracle:

```python
from plant_ia import Plantilla

correo = Plantilla(
    "Redacta un correo profesional dirigido a {colaborador}, reconociendo su desempeño como {rol} "
    "dentro del equipo de {departamento}. Menciona brevemente el impacto de sus aportaciones desde su incorporación el {fecha_ingreso}."
)

datos = {
    "colaborador": "María Gómez",
    "rol": "Especialista en Nómina",
    "departamento": "Finanzas",
    "fecha_ingreso": "3 de marzo de 2023"
}

mensaje = correo.rellenar(**datos)
print(mensaje)
```

Este tipo de uso permite escalar la generación de contenido profesional en procesos como onboarding, gestión de talento, atención al cliente y automatización de comunicaciones internas.