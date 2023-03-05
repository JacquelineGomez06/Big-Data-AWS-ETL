from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from config import connection
import pandas as pd

#prepairing connection to database
engine = create_engine(connection).connect()

#allows querying database(pulling data)
session = Session(engine)

# this object will automatically map our db entity into a Python class
Base = automap_base()
# get db into automapper
Base.prepare(engine, reflect=True)

#mapped classes are created with default matching of the table names
jobs = Base.classes.jobs
salaries = Base.classes.salaries
skills = Base.classes.skills

#a query with filtering and selection
jobs_rows = session.query(jobs)
salaries_rows=session.query(salaries)
skills_rows=session.query(skills)

jobs_df = pd.read_sql(jobs_rows.statement, engine)
skills_df = pd.read_sql(skills_rows.statement, engine)
salaries_df = pd.read_sql(salaries_rows.statement, engine)


