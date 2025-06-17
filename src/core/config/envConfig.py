# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     database_username: str
#     database_password: str
#     database_hostname: str
#     database_portnumber: int
#     database_name: str
#     secret_key: str
#     algorithm: str
#     access_token_exp_time: int

#     class Config:
#         env_file = ".env"

# settings = Settings()

# # this is only for testing the env variable
# if __name__ == "__main__":
#     print("Database username:", settings.database_username)
#     print("Database password:", settings.database_password)
#     print("Hostname:", settings.database_hostname)
#     print("Database name:", settings.database_name)
#     print("Secret key:", settings.secret_key)
#     print("Algorithm:", settings.algorithm)
#     print("Token expiry:", settings.access_token_exp_time)
import os
from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_username: str
    database_password: str
    database_hostname: str
    database_portnumber: int
    database_name: str
    secret_key: str
    algorithm: str
    access_token_exp_time: int

    class Config:
        # Xác định đường dẫn đầy đủ tới file .env nằm trong src
        env_file = str(Path(__file__).resolve().parents[2] / ".env")
        env_file_encoding = "utf-8"

settings = Settings()

# Test biến môi trường
if __name__ == "__main__":
    print("Database username:", settings.database_username)
    print("Database password:", settings.database_password)
    print("Hostname:", settings.database_hostname)
    print("Database name:", settings.database_name)
    print("Secret key:", settings.secret_key)
    print("Algorithm:", settings.algorithm)
    print("Token expiry:", settings.access_token_exp_time)
