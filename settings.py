from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field, field_validator


def validate_threshold(value):
    if value < 0 or value > 1:
        return False

    return True


class MySettings(BaseModel):
    prompt_prefix: str = Field(
        title="Prompt prefix",
        default="""You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
You answer Human with a focus on the following context.
""",
        extra={"type": "TextArea"},
    )
    episodic_memory_k: int = 3
    episodic_memory_threshold: float = 0.7
    declarative_memory_k: int = 3
    declarative_memory_threshold: float = 0.7
    procedural_memory_k: int = 3
    procedural_memory_threshold: float = 0.7
    user_name: str = "Human"
    language: str | None = "English"

    @field_validator("episodic_memory_threshold")
    @classmethod
    def episodic_memory_threshold_validator(cls, threshold):
        if not validate_threshold(threshold):
            raise ValueError("Episodic memory threshold must be between 0 and 1")

    @field_validator("declarative_memory_threshold")
    @classmethod
    def declarative_memory_threshold_validator(cls, threshold):
        if not validate_threshold(threshold):
            raise ValueError("Declarative memory threshold must be between 0 and 1")

    @field_validator("procedural_memory_threshold")
    @classmethod
    def procedural_memory_threshold_validator(cls, threshold):
        if not validate_threshold(threshold):
            raise ValueError("Procedural memory threshold must be between 0 and 1")


@plugin
def settings_model():
    return MySettings
