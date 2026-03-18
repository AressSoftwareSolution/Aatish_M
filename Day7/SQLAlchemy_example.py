from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. connect to SQLite database
engine = create_engine("sqlite:///students.db")

# 2. base class for tables
Base = declarative_base()

# 3. define table (model)
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# 4. create table in database
Base.metadata.create_all(engine)

# 5. create session
Session = sessionmaker(bind=engine)
session = Session()

# 6. insert data
student1 = Student(name="Rahul")
student2 = Student(name="Priya")

session.add(student1)
session.add(student2)
session.commit()

print("Data inserted successfully!")



# bind=engine -> Means:connect this session to this database engine
# Session = sessionmaker(bind=engine) -> means:Create a session factory that knows which database to use.

#------- Following are the SQLAlchemy components
# create_engine → connects Python to the database
# Column, Integer, String → define table columns and data types
# declarative_base() → base class for creating tables using Python classes
# sessionmaker → creates a session to talk to the database