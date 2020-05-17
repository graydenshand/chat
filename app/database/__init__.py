from .base import Base, engine

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from .models.user import User
    from .models.message import Message
    Base.metadata.create_all(bind=engine)