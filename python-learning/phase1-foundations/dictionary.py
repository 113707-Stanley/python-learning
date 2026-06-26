people = [
    {"name": "Stanley", "role": "Associate Director", "department": "QEA"},
    {"name": "John", "role": "QA Engineer", "department": "QEA"},
    {"name": "Sarah", "role": "Test Lead", "department": "QEA"},
    {"name": "Emily", "role": "QA Analyst", "department": "QEA"},
    {"name": "Michael", "role": "QA Manager", "department": "QEA"},
]

for person in people:
    print(f"Name: {person['name']}, Role: {person['role']}")
    
# Adding a new key to an existing dictionary
people[0]["experience"] = 10
people[1]["experience"] = 8
people[3]["experience"] = 12
people[2]["experience"] = 15
# I Want to use one print statement to print the updated list of dictionaries only 
# once after adding the new key to the existing dictionaries.

print(f"\nUpdated list of dictionaries with experience added:")
for person in people:
    print(f"  Name: {person['name']}, Experience: {person.get('experience','NA')} years")

# Checking if a key exists
if "department" in people[0]:
    print(f"\nDepartment found: {people[0]['department']}")

for person in people:
    print(f"Name: {person['name']}")
    print(f"Role: {person['role']}")
    print(f"Department: {person['department']}")
    print(f"Experience: {person.get('experience', 'NA')} years")
    print(f"---")
