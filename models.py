from datetime import date
from pydantic import BaseModel

from typing import List, Optional

from pydantic import BaseModel


class Location(BaseModel):
    city: str
    country: str


class Experience(BaseModel):
    company_name: str
    job_title: str
    description: str
    skills: list[str]
    starts_at: date
    ends_at: date
    location: Location


class User(BaseModel):
    first_name: str
    last_name: str
    skills: list[str]
    description: Optional[str]
    location: Location
    experiences: list[Experience]

    def summarize_experiences(self) -> list:
        companies = []
        current_company = self.experiences[0].company_name
        current_start_date = self.experiences[0].starts_at
        current_end_date = self.experiences[0].ends_at

        for exp in self.experiences[:]:
            if current_end_date is not None and current_end_date >= exp.starts_at:
                current_end_date = max(current_end_date, exp.ends_at)
            else:
                companies.append(
                    {
                        "company_name": current_company,
                        "starts_at": current_start_date,
                        "ends_at": current_end_date,
                    }
                )
                current_company = exp.company_name
                current_start_date = exp.starts_at
                current_end_date = exp.ends_at

        companies.append(
            {
                "company_name": current_company,
                "starts_at": current_start_date,
                "ends_at": current_end_date,
            }
        )
        return companies
