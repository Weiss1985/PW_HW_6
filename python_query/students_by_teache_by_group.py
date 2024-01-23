#10 Список курсів, які певному студенту читає певний викладач:

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
        SELECT sub.name AS subject_name
        FROM Subjects sub
        JOIN Grades g ON sub.subject_id = g.subject_id
        WHERE g.student_id = 16 AND sub.teacher_id = 2;







    """
    students_top5 = await execute_query(conn, query)

    for record in students_top5:
        print(record)
        #print(f"Teacher {record['teacher_name']} subject {record['subject_name']}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))