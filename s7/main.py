from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text

DB_NAME = "mydbS7"  

engine_default = create_engine(
    "postgresql+psycopg2://postgres:postgresBD1@localhost:5432/postgres",
    isolation_level="AUTOCOMMIT"
)

with engine_default.connect() as conn:
    result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}';")).fetchone()
    if result:
        print(f"La base de datos '{DB_NAME}' ya existe")
    else:
        conn.execute(text(f'CREATE DATABASE "{DB_NAME}";'))
        print(f"Base de datos '{DB_NAME}' creada")

engine = create_engine(f"postgresql+psycopg2://postgres:postgresBD1@localhost:5432/{DB_NAME}")
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False),
)

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
)

stores = Table(
    "stores",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
)

metadata.create_all(engine)
print("Tablas creadas")

with engine.connect() as conn:
    conn.execute(text("ALTER TABLE users ADD COLUMN email VARCHAR(100);"))
    print("Columna 'email' agregada a 'users' ")

    conn.execute(text("ALTER TABLE users RENAME COLUMN username TO user_name;"))
    print("Columna 'username' renombrada a 'user_name' ")

    conn.execute(text("ALTER TABLE users DROP COLUMN email;"))
    print("Columna 'email' eliminada de 'users' ")

    conn.execute(text("ALTER TABLE stores ADD CONSTRAINT check_name CHECK (char_length(name) > 2);"))
    print("CHECK agregado a 'stores' ")

    conn.execute(text("DROP TABLE products;"))
    print("Tabla 'products' eliminada ")

    conn.commit()

    version = conn.execute(text("SELECT version();")).fetchone()
    print("Conexión exitosa a PostgreSQL:", version)
