from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env")
    JWT_ACCESS_SECRET: str
    JWT_REFRESH_SECRET: str
    JWT_ACCESS_EXP: int
    JWT_REFRESH_EXP: int


config = Config()  # type: ignore
