from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    class_standing: str
    major: str
    major_class:bool
    upper_division:bool
    ge:bool
    area: str
