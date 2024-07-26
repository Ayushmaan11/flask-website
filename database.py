from sqlalchemy import create_engine, text
import logging
import os
from  dotenv import load_dotenv

load_dotenv()
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


username = os.getenv('JOBFINDER_DB_USERNAME')
password = os.getenv('JOBFINDER_DB_PASSWORD')
hostname = os.getenv('JOBFINDER_DB_HOSTNAME')
dbname = 'JobFinder'
port = os.getenv('JOBFINDER_DB_PORT')


DATABASE_URI = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{dbname}?charset=utf8mb4'


engine = create_engine(DATABASE_URI, connect_args={"connect_timeout": 10, "read_timeout": 10, "write_timeout": 10}, pool_recycle=3600)

def load_jobs_from_db():
    with engine.connect() as conn:
      result = conn.execute(text("select * from JOBS"))
      columns = result.keys()
      jobs = []
      for row in result.all():
          jobs.append(dict(zip(columns,row)))
      return jobs


