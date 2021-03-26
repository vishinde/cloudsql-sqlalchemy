from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:pass@146.148.95.51/guestbook", 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)

engine.connect()

print(engine)