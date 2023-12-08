# ResearchSystem.py
from Researcher import Researcher
from Project import Project
from Publication import Publication

# Create researchers
researcher1 = Researcher(1, "John Doe", "University A")
researcher2 = Researcher(2, "Jane Smith", "University B")

# Create projects
project1 = Project(101, "Study on Artificial Intelligence", "Exploring AI technologies", "2022-01-01", "2023-12-31")
project2 = Project(102, "Environmental Sustainability Research", "Analyzing environmental impact", "2022-03-15", "2023-11-30")

# Create publications
publication1 = Publication(201, "AI and Ethics", ["John Doe", "Jane Smith"], "2023-05-20")
publication2 = Publication(202, "Environmental Impact Report", ["Jane Smith"], "2023-10-15")

# Associate researchers with projects
researcher1.projects.extend([project1, project2])
researcher2.projects.append(project2)

# Associate projects with publications
project1.publications.append(publication1)
project2.publications.extend([publication1, publication2])

# Display information
researcher1.display_info()
print("\n" + "="*50 + "\n")
researcher2.display_info()
