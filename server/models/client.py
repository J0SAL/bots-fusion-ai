from pydantic import BaseModel
from typing import Optional
class Client(BaseModel):
    name: str
    email: str
    mobile: str
    dob: str
    city: str
    gender: str

class UpdateClient(BaseModel):
    name: Optional[str]
    email: Optional[str]
    mobile: Optional[str]
    dob: Optional[str]
    city: Optional[str]
    gender: Optional[str]