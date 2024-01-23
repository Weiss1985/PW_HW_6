#2 Знайти студента із найвищим середнім балом з певного предмета:

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
        SELECT s.student_id, s.name, sub.name AS subject_name, AVG(g.grade) AS average_grade
        FROM Students s
        JOIN Grades g ON s.student_id = g.student_id
        JOIN Subjects sub ON g.subject_id = sub.subject_id
        WHERE g.subject_id = 2
        GROUP BY s.student_id, s.name, sub.name
        ORDER BY average_grade DESC
        LIMIT 1;

    """
    students_top5 = await execute_query(conn, query)
    print(f"Top student with the highest average grades on subject: ")
    for record in students_top5:
        # print(record)
        print(f"{record['subject_name']}: {record['name']}: {record['average_grade']:.2f}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))