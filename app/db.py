from sqlmodel import SQLModel, create_engine, Session

def get_engine():
    return create_engine("sqlite:///./reservas.db", echo=False, future=True)

def init_db():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
