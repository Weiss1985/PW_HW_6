# Запит 1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів
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
        SELECT s.student_id, s.name, AVG(g.grade) AS average_grade
        FROM Students s
        JOIN Grades g ON s.student_id = g.student_id
        GROUP BY s.student_id
        ORDER BY average_grade DESC
        LIMIT 5;
    """
    students_top5 = await execute_query(conn, query)
    print("Top 5 students with the highest average grades:")
    for record in students_top5:
        print(f"{record['name']}: {record['average_grade']:.2f}")

    await conn.close()


if __name__ == '__main__':
    asyncio.run(main(user, password, database, host))
