# Sistema de Reservas de Laboratorio

Este proyecto implementa un sistema robusto y eficiente para la gestión de reservas de equipos de laboratorio, garantizando la integridad de los datos y evitando conflictos de horarios.

---

## 1. Especificación

*   **Problema:** Necesidad de gestionar el uso de equipos de laboratorio compartidos (Microscopios, Osciloscopios, etc.) evitando que dos usuarios reserven el mismo equipo en el mismo intervalo de tiempo.
*   **Alcance:** Backend completo capaz de crear, consultar y cancelar reservas mediante una API REST.
*   **Supuestos:**
    *   Los IDs de los equipos están predefinidos en un inventario estático.
    *   Los tiempos se gestionan en formato ISO 8601.
    *   El sistema utiliza una base de datos local SQLite para persistencia.
*   **Criterios de Aceptación:**
    *   Creación de reservas con validación de datos.
    *   Prevención estricta de superposiciones.
    *   Permiso de reservas consecutivas (ej. 10:00-11:00 y 11:00-12:00).
    *   Capacidad de cancelar una reserva sin eliminar el registro histórico.
    *   Consultas de disponibilidad que ignoran las reservas canceladas.

---

## 2. Solución

### Estructura del Proyecto
```text
challenge/
├── app/
│   ├── __init__.py
│   ├── crud.py          # Lógica de negocio y validación de reglas
│   ├── db.py            # Configuración de SQLite y conexión
│   ├── main.py          # API FastAPI y gestión de endpoints
│   └── models.py        # Modelos de datos (SQLModel/Pydantic)
├── tests/
│   └── test_reservations.py
├── inventory.json       # Inventario fijo de equipos
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación técnica
```

### Instalación
1. Clonar el repositorio.
2. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución
Levanta el servidor con `uvicorn`:
```bash
uvicorn app.main:app --reload
```
Una vez iniciado, accede a la documentación interactiva (Swagger UI) en:
**`http://127.0.0.1:8000/docs`**

### Pruebas
Para ejecutar el conjunto de pruebas automáticas, utiliza `pytest`:
```bash
pytest
```

### Persistencia de Datos
Los datos se almacenan automáticamente en el archivo **`reservas.db`** generado en la raíz del proyecto mediante SQLite.

---

## 3. Preparación del Agente

*   **Modelo:** gpt-4o-mini.
*   **Entorno:** Pi Coding Agent, operando en un entorno Windows con soporte Bash.
*   **Instrucciones:** Construcción modular siguiendo principios de arquitectura limpia y cumplimiento estricto de las reglas del challenge.
*   **Permisos:** Acceso completo a operaciones de archivos, ejecución de comandos del sistema y gestión de control de versiones.

---

## 4. Registro de Decisiones y Delegación

### Episodio 1: Elección de Stack Tecnológico
*   **Decisión:** Se optó por **FastAPI + SQLModel** sobre Flask o Django.
*   **Justificación:** SQLModel ofrece una excelente integración entre Pydantic (validación) y SQLAlchemy (ORM), lo que agiliza el desarrollo de APIs robustas y facilita la persistencia con SQLite.
*   **Verificación:** El agente presentó la estructura de carpetas y el archivo `models.py`. El usuario validó la elección de tecnología por su modernidad y eficiencia.

### Episodio 2: Manejo de Lógica de Negocio y Superposiciones
*   **Decisión:** La validación de superposición (`start < end` y `end > start`) se delegó a la capa de `crud.py` mediante una consulta atómica a la base de datos.
*   **Justificación:** Delegar la validación a la capa de datos asegura que la integridad se mantenga incluso ante múltiples peticiones simultáneas, evitando condiciones de carrera.
*   **Verificación:** El usuario revisó la lógica de consulta en `crud.py` para asegurar que las reservas canceladas (`status == 'active'`) fueran ignoradas en la verificación de solapamiento.

### Episodio 3: Interfaz y Experiencia de Usuario
*   **Decisión:** Se decidió utilizar **Swagger UI** (generado automáticamente por FastAPI) como la interfaz principal para pruebas.
*   **Justificación:** Proporciona un entorno profesional, documentado e interactivo sin necesidad de construir un frontend complejo, cumpliendo con el objetivo de funcionalidad rápida y testeable.
*   **Verificación:** Se confirmó la accesibilidad en `/docs` y se acordó que esta interfaz es suficiente para el alcance del desafío, priorizando la solidez del backend.
