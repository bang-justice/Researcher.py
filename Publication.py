# Publication.py

class Publication:
    def __init__(self, publication_id, title, authors, publication_date):
        self.publication_id = publication_id
        self.title = title
        self.authors = authors
        self.publication_date = publication_date

    def display_info(self):
        print(f"Publication ID: {self.publication_id}")
        print(f"Title: {self.title}")
        print(f"Authors: {', '.join(self.authors)}")
        print(f"Publication Date: {self.publication_date}")
