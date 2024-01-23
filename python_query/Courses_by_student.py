#9 Знайти список курсів, які відвідує студент:

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
        SELECT DISTINCT sub.name AS subject_name
        FROM Grades g
        JOIN Subjects sub ON g.subject_id = sub.subject_id
        WHERE g.student_id = 6;







    """
    students_top5 = await execute_query(conn, query)

    for record in students_top5:
        print(record)
        #print(f"Teacher {record['teacher_name']} subject {record['subject_name']}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))