# Project.py

class Project:
    def __init__(self, project_id, title, description, start_date, end_date):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.publications = []

    def display_info(self):
        print(f"Project ID: {self.project_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("Publications:")
        for publication in self.publications:
            print(f"  - {publication.title}")
