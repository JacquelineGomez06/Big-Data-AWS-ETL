from config import connection
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import functools as ft


engine = create_engine(connection)

session = Session(engine)

Base = automap_base()
Base.prepare(engine, reflect = True)

jobs = Base.classes.jobs
skills = Base.classes.skills
salaries = Base.classes.salaries 

jobs_result = session.query(jobs)
skills_result = session.query(skills)
salaries_result = session.query(salaries)

jobs_df = pd.read_sql(sql = jobs_result.statement, con = engine.connect())
skills_df = pd.read_sql(sql = skills_result.statement, con = engine.connect())
salaries_df = pd.read_sql(sql = salaries_result.statement, con = engine.connect())

engine.dispose()

#merge 3 tables on primary key id
dfs = [jobs_df,skills_df,salaries_df]
df_final = ft.reduce(lambda left, right: pd.merge(left, right, on='id'), dfs)
df_merged = ft.reduce(lambda  left,right: pd.merge(left,right,on=['id'], how='outer'), dfs)

# Write this joined dataframe to the data / folder
df_merged.to_csv("data/joined_data.csv", index = False)
