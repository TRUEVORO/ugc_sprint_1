from pydantic import AnyHttpUrl, BaseSettings, Field


class TestSettings(BaseSettings):
    """Test settings class to read environment variables."""

    service_dsn: AnyHttpUrl = Field(default='http://localhost:81/api/v1/view/view_progress')

    kafka_topic: str = Field(default='progress')


test_settings = TestSettings()
