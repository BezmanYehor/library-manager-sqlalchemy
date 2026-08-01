from database.db import Base, engine
import database.models

Base.metadata.create_all(engine)
