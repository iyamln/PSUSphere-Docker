
from faker import Faker
from studentorg.models import College, Program, Student

fake = Faker()

if College.objects.filter(college_name__startswith="FAKE - ").exists():
    print("Fake data already exists. No new data generated.")
else:
    colleges = []
    programs = []

    for i in range(3):
        college = College.objects.create(
            college_name=f"FAKE - {fake.company()} College"
        )
        colleges.append(college)

    for college in colleges:
        for i in range(2):
            program = Program.objects.create(
                prog_name=fake.catch_phrase()[:150],
                college=college,
            )
            programs.append(program)

    student_number = 1

    for program in programs:
        for i in range(5):
            Student.objects.create(
                student_id=f"FAKE-{student_number:04d}",
                lastname=fake.last_name()[:25],
                firstname=fake.first_name()[:25],
                middlename=fake.first_name()[:25],
                program=program,
            )
            student_number += 1

    print("Fake data generated successfully!")

print("Colleges:", College.objects.count())
print("Programs:", Program.objects.count())
print("Students:", Student.objects.count())
