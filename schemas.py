from pydantic import BaseModel #pydantic model = class that we map to the table


class Blog(BaseModel):
    title: str
    body: str


class ShowBlog(Blog):
    class Config:
        orm_mode = True
