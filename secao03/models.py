from typing import Optional

from pydantic import BaseModel

class Banda(BaseModel):
    id: Optional[int] = None
    Banda: str
    músicos: list
    vertente: str