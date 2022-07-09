from pydantic import BaseModel


class ProjectSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ProjectCreateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True
