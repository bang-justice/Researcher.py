# Researcher.py

class Researcher:
    def __init__(self, researcher_id, name, affiliation):
        self.researcher_id = researcher_id
        self.name = name
        self.affiliation = affiliation
        self.projects = []

    def display_info(self):
        print(f"Researcher ID: {self.researcher_id}")
        print(f"Name: {self.name}")
        print(f"Affiliation: {self.affiliation}")
        print("Projects:")
        for project in self.projects:
            print(f"  - {project.title}")
