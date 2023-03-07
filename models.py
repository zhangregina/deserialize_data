from typing import List, Optional
from datetime import date
from pydantic import BaseModel


class Experience(BaseModel):
    company_name: str
    job_title: str
    description: str
    skills: List[str]
    starts_at: date
    ends_at: date
    location: dict


class User(BaseModel):
    first_name: str
    last_name: str
    skills: List[str]
    description: Optional[str]
    location: dict
    experiences: List[Experience]
