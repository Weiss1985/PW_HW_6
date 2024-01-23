def create_sql_files(start, end):
    for i in range(start, end + 1):
        file_name = f"query_{i}.sql"
        with open(file_name, 'w') as file:
            file.write("-- SQL query " + str(i) + "\n")


start_number = 11
end_number = 12

create_sql_files(start_number, end_number)
