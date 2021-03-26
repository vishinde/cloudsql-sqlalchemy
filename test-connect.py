from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:pass@IPAddress/dbname", 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)

engine.connect()

print(engine)