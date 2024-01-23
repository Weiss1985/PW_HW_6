#5 Знайти які курси читає певний викладач:

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
        SELECT t.name AS teacher_name, sub.name AS subject_name
        FROM Subjects sub
        JOIN Teachers t ON sub.teacher_id = t.teacher_id
        WHERE sub.teacher_id = 1; 




    """
    students_top5 = await execute_query(conn, query)

    for record in students_top5:
        #print(record)
        print(f"Teacher {record['teacher_name']} subject {record['subject_name']}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))