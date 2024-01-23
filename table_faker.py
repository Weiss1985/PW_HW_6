import asyncpg
from faker import Faker
import random
from datetime import datetime
import asyncio

user = 'postgres'
password = '12345'
database = 'postgres'
host = 'localhost'
faker = Faker()

async def insert_random_data(user, password, database, host):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)

    group_ids = []
    for _ in range(3):
        group_name = faker.word() + str(faker.random_number(digits=2))
        group_id = await conn.fetchval('INSERT INTO Groups (group_name) VALUES ($1) RETURNING group_id', group_name)
        group_ids.append(group_id)

    teacher_ids = []
    for _ in range(3):
        name = faker.name()
        teacher_id = await conn.fetchval('INSERT INTO Teachers (name) VALUES ($1) RETURNING teacher_id', name)
        teacher_ids.append(teacher_id)

    subject_ids = []
    for _ in range(5):
        name = faker.word()
        teacher_id = random.choice(teacher_ids)
        subject_id = await conn.fetchval('INSERT INTO Subjects (name, teacher_id) VALUES ($1, $2) RETURNING subject_id', name, teacher_id)
        subject_ids.append(subject_id)

    for _ in range(30):
        name = faker.name()
        group_id = random.choice(group_ids)
        student_id = await conn.fetchval('INSERT INTO Students (name, group_id) VALUES ($1, $2) RETURNING student_id', name, group_id)

        for subject_id in subject_ids:
            for _ in range(random.randint(1, 20)):
                grade = random.randint(1, 5)
                date_received = faker.date_between(start_date='-1y', end_date='today')
                await conn.execute('INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES ($1, $2, $3, $4)', student_id, subject_id, grade, date_received)

    await conn.close()

async def main():
    await insert_random_data(user, password, database, host)


if __name__ == '__main__':
    asyncio.run(main())
