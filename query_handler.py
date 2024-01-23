import psycopg2


def execute_sql_from_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_query = file.read()
        cursor.execute(sql_query)
        return cursor.fetchall()


def main():
    connection = None
    try:
        connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='12345',
            host='localhost'
        )
        cursor = connection.cursor()

        query_number = input("Enter query number: ")
        file_path = f"query_{query_number}.sql"

        result = execute_sql_from_file(cursor, file_path)
        for row in result:
            print(row)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    main()
