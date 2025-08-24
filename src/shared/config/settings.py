from pydantic_settings import BaseSettings

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict, Field
from dotenv import load_dotenv

load_dotenv()


class BaseConfig(BaseSettings):

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env",
        env_file_encoding="utf-8",
    )


class APPConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
    )

    develop: bool = Field(default=False)
    logger_level: str = Field(default="INFO")


class PostgreSQLConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_prefix="POSTGRES_",
    )

    user: str
    password: str
    name: str
    host: str
    port: int
    echo: bool = Field(
        default=False,
    )

    @property
    def database_url_async(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.name}"
        )


class Settings(BaseConfig):
    app: APPConfig = Field(
        default_factory=APPConfig,
    )
    postgresql: PostgreSQLConfig = Field(
        default_factory=PostgreSQLConfig,
    )
