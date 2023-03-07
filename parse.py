import json
from pydantic import parse_obj_as
from models import User
from typing import List

json_data = """
[
   {
      "first_name":"Eren",
      "last_name":"Yeagar",
      "skills":[
         "Python",
         "Django",
         "SQL",
         "FastAPI"
      ],
      "description":"Solution-Oriented Python Developer with a demonstrated history of working in the IT. Lifelong learner. Enjoy solving/developing apps and writing scripts.",
      "location":{
         "city":"London",
         "country":"UK"
      },
      "experiences":[
         {
            "company_name":"Apple",
            "job_title":"Backend developer",
            "description":"Solution-Oriented Python Developer",
            "skills":[
               "Python",
               "Django",
               "SQL"
            ],
            "starts_at":"2020-01-01",
            "ends_at":"2022-01-01",
            "location":{
               "city":"London",
               "country":"UK"
            }
         },
         {
            "company_name":"Google",
            "job_title":"Backend developer",
            "description":"Solution-Oriented Python Developer",
            "skills":[
               "Python",
               "Django",
               "SQL",
               "FastAPI"
            ],
            "starts_at":"2021-01-01",
            "ends_at":"2031-01-01",
            "location":{
               "city":"London",
               "country":"UK"
            }
         }
      ]
   },
   {
      "first_name":"Annie",
      "last_name":"LeonHeart",
      "skills":[
         "Figma",
         "Sketch",
         "UX-research",
         "Miro"
      ],
      "description":"Experienced UX-UI designer",
      "location":{
         "city":"Milan",
         "country":"Europe"
      },
      "experiences":[
         {
            "company_name":"Berlin Company",
            "job_title":"UX-designer",
            "description":"UX (user experience) designers measure and optimise applications (usually web based) to improve ease of use (usability)",
            "skills":[
               "Figma",
               "Sketch",
               "UX-research",
               "Miro"
            ],
            "starts_at":"2020-02-02",
            "ends_at":"2022-02-02",
            "location":{
               "city":"Berlin",
               "country":"Europe"
            }
         }
      ]
   }
]
"""

# Deserialize the JSON data into a list of User objects
data = json.loads(json_data)
users = parse_obj_as(List[User], data)

# General information of User
print(users[0])
print(users[1])
