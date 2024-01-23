#4 Знайти середній бал на потоці (по всій таблиці оцінок):

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
        SELECT AVG(grade) AS average_grade
        FROM Grades;



    """
    students_top5 = await execute_query(conn, query)
    print(f"Groups with average grades: ")
    for record in students_top5:
        #print(record)
        print(f"Average grade: {record['average_grade']:.2f}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))