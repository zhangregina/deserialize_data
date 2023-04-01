from pydantic import parse_file_as
from models import User
from typing import List
from pathlib import Path


class ParseUsers:
    def __init__(self):
        self.path = Path("profiles.json")
        self.users = parse_file_as(path=self.path, type_=List[User])

    def start(self):
        for user in self.users:
            print(user)

    def main(self):
        self.start()


if __name__ == "__main__":
    user = ParseUsers()
    user.main()
