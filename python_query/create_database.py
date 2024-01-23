import asyncpg
import asyncio


user = 'postgres'
password = '12345'
database = 'postgres'
host = 'localhost'


async def create_tables(user, password, database, host):

    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS Groups (
            group_id SERIAL PRIMARY KEY,
            group_name VARCHAR(255) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            group_id INTEGER NOT NULL REFERENCES Groups(group_id)
        );
        CREATE TABLE IF NOT EXISTS Teachers (
            teacher_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Subjects (
            subject_id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            teacher_id INTEGER NOT NULL REFERENCES Teachers(teacher_id)
        );
        CREATE TABLE IF NOT EXISTS Grades (
            grade_id SERIAL PRIMARY KEY,
            student_id INTEGER NOT NULL REFERENCES Students(student_id),
            subject_id INTEGER NOT NULL REFERENCES Subjects(subject_id),
            grade INTEGER NOT NULL,
            date_received TIMESTAMP NOT NULL
        );
    ''')

    # Закриття підключення до бази даних
    await conn.close()

# Асинхронно викликаємо функцію create_tables
# Замініть 'your_username', 'your_password', 'university', 'localhost' на відповідні значення


async def main():
    await create_tables(user, password, database, host)


if __name__ == '__main__':
    asyncio.run(main())

