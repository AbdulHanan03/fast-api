from sqlalchemy import Column, Integer, String
from blogs.database import Base
#sqlalchemy model = table


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
