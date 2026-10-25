# Reserva de Laboratorio - Challenge IA

## Especificación

**Problema:** La coordinación de un laboratorio necesita un sistema para registrar pedidos de reserva de equipos, evitando superposiciones y permitiendo cancelar reservas sin perder el historial.

**Alcance:** Gestión de reservas para un inventario fijo de equipos (MIC-01, MIC-02, OSC-01, MUL-01, FUE-01). Persistencia de datos en SQLite entre ejecuciones. API local con FastAPI.

**Supuestos:**
- Los IDs de los equipos son los definidos en `inventory.json`.
- Las fechas/hora se reciben en formato ISO 8601 (con o sin zona horaria).
- La zona horaria es la del servidor (UTC).
- Se permite una reserva por unidad y por intervalo.

**Criterios de aceptación:**
- Crear reservas válidas (unidad conocida, solicitante no vacío, inicio < fin).
- Rechazar reservas que se superpongan con reservas activas de la misma unidad.
- Permitir reservas consecutivas (ej. 10:00-11:00 y 11:00-12:00).
- Permitir reservas de equipos diferentes en el mismo rango horario.
- Cancelar reservas cambiando su estado (sin eliminarlas) y liberando el horario.
- Persistir datos en SQLite.

## Solución

**Estructura del proyecto:**
```text
challenge/
├─ app/
│  ├─ __init__.py
│  ├─ main.py          # FastAPI aplicación
│  ├─ models.py        # Modelos SQLModel
│  ├─ crud.py          # Lógica de negocio
│  └─ db.py            # Conexión SQLite
├─ inventory.json      # Inventario fijo de equipos
├─ tests/
│  └─ test_reservations.py
├─ requirements.txt
└─ README.md
