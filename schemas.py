from typing import Optional
from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: str | None = None  # Optional[str] = None


class STask(STaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class STaskID(BaseModel):
    ok: bool = True
    id: int
