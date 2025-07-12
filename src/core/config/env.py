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
    refresh_token_exp_time: int
    verification_code_exp_time: int
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    max_attempt_require_code: int
    MINIO_ROOT_USER:str
    MINIO_ROOT_PASSWORD:str
    MINIO_ACCESS_KEY:str
    MINIO_SECRET_KEY:str
    MINIO_ENDPOINT:str


    class Config:
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
