# Proyecto: Conexión Python ↔ PostgreSQL con Docker

## Requisitos

- Python 3.10+
- PostgreSQL en Docker
- Librerías:
  ```bash
  pip install sqlalchemy psycopg2
  ```

## Pasos

1. Conectarse a la base de datos PostgreSQL usando SQLAlchemy.

2. Crear base de datos y 2 tablas (users, products) desde Python.

3. Aplicar operaciones DDL:

   - Agregar columnas (ALTER TABLE ... ADD COLUMN).

   - Renombrar columnas (ALTER TABLE ... RENAME COLUMN).

   - Eliminar columnas (ALTER TABLE ... DROP COLUMN).

   - Agregar un CHECK constraint.

   - Eliminar una tabla.

- Verificar los cambios ejecutando consultas en la DB o revisando con psql.

## Ejecución

```bash
python main.py

```
