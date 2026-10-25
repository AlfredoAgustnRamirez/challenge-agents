# Reserva de Laboratorio

## Especificación

*Problema:* Necesitamos un sistema que permita crear, consultar y cancelar reservas de equipos de laboratorio.

*Alcance:* Gestión de reservas para un inventario fijo de equipos. Persistencia de datos entre ejecuciones.

*Supuestos:* 
- Los IDs de los equipos son los definidos en el inventario.
- Las fechas/hora se reciben en formato ISO 8601.
- La zona horaria es la del servidor.

*Criterios de aceptación:*
- Crear reservas válidas.
- Rechazar reservas que se solapen.
- Permitir reservas consecutivas.
- Permitir reservas de equipos diferentes en el mismo rango horario.
- Cancelar reservas sin eliminarlas.
- Persistir datos en SQLite.

## Solución

Estructura del proyecto:
```
challenge/
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # FastAPI aplicación
│  ├─ models.py        # Pydantic y SQLModel definitions
│  ├─ crud.py          # Lógica de negocio
│  └─ db.py            # Conexión SQLite
├─ inventory.json      # Inventario fijo de equipos
├─ tests/
│  └─ test_reservations.py
├─ requirements.txt
└─ README.md
```

### Instalación
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecución
```bash
uvicorn app.main:app --reload
```

### Pruebas
```bash
pytest
```

Los datos se guardan en `sqlite:///./reservas.db` dentro del directorio del proyecto.

## Preparación del agente

Modelo usado: gpt-4o-mini
Entorno: Pi coding agent, acceso a filesystem y bash.
Instrucciones: Crear estructura, código, README y tests siguiendo las reglas del challenge.
Permisos: Lectura y escritura de archivos, ejecución de comandos.

## Registro de decisiones y delegación

*(Este apartado será completado después de la implementación y revisión conjunta.)*
