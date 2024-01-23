#6 Знайти список студентів у певній групi:

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
        SELECT s.name AS student_name, gr.group_name
        FROM Students s
        JOIN Groups gr ON s.group_id = gr.group_id
        WHERE s.group_id = 1;





    """
    students_top5 = await execute_query(conn, query)

    for record in students_top5:
        print(record)
        #print(f"Teacher {record['teacher_name']} subject {record['subject_name']}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))