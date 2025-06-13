import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from sqlalchemy import create_engine
from core.config.envConfig import settings

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format (
    settings.database_username, 
    settings.database_password, 
    settings.database_hostname,
    settings.database_portnumber,
    settings.database_name
)

engine = create_engine (DATABASE_URL)

if __name__ == "__main__":
    print (DATABASE_URL)