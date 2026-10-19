data_structure={
    "id1": {"name": "Kridha", "class":"9", "subject_integration":"english"},
    "id2": {"name": "Kridha", "class":"9", "subject_integration":"english"},
    "id3": {"name": "Manya", "class":"9", "subject_integration":"maths"},
    "id4": {"name": "Pakhi", "class":"9", "subject_integration":"science"},
}
result1={}
unique=set()

for student_id, details in data_structure.items():
    key_unique=(details["name"],details["class"],details["subject_integration"])
    if key_unique not in unique:
        unique.add(key_unique)
        result1[student_id]=details

print(result1)