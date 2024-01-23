#7 Знайти оцінки студентів у окремій групі з певного предмета:

import asyncpg
import asyncio


user = 'postgres'
password = '12345'
database = 'postgres'
host = 'localhost'


async def execute_query(conn, query):
    return await conn.fetch(query)


async def main(user, password, database, host):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)

    query = """
        SELECT s.name AS student_name, g.grade
        FROM Students s
        JOIN Grades g ON s.student_id = g.student_id
        JOIN Subjects sub ON g.subject_id = sub.subject_id
        WHERE s.group_id = 1 AND g.subject_id = 2;






    """
    students_top5 = await execute_query(conn, query)

    for record in students_top5:
        print(record)
        #print(f"Teacher {record['teacher_name']} subject {record['subject_name']}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))