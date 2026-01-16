import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

input_file = BASE_DIR / "students.json"
output_file = BASE_DIR / "students_updated.json"

with open(input_file, "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = round(sum(grades) / len(grades), 2)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)
