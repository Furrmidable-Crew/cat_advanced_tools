from cat.mad_hatter.decorators import plugin
from pydantic import BaseModel, Field


class MySettings(BaseModel):
    prompt_prefix: str = Field(
                title="Prompt prefix",
                default="""You are the Cheshire Cat AI, an intelligent AI that passes the Turing test.
You are curious, funny and talk like the Cheshire Cat from Alice's adventures in wonderland.
You answer Human with a focus on the following context.
""",
                extra={"type": "TextArea"}
        )
    episodic_memory_k: int = 3
    episodic_memory_threshold: int = 0.7
    declarative_memory_k: int = 3
    declarative_memory_threshold: int = 0.7
    procedural_memory_k: int = 3
    procedural_memory_threshold: int = 0.7


@plugin
def settings_schema():
    return MySettings.schema()
