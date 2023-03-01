from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config import connection

engine = create_engine(connection)

# this object will automatically map our db entity into a Python class
Base = automap_base()

# get db into automapper
Base.prepare(engine, reflect=True)

# save classes as variables, prepare classes
jobs = Base.classes.jobs
salaries = Base.classes.salaries
skills = Base.classes.skills

# query our database (pull data and save into objects)
session = Session(engine)