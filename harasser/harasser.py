import psycopg2

def harassinit():
    #when this gets called, harasser-db doesn't exist
    conn = psycopg2.connect(
        dbname='postgres_database_harasser',
        user='userharasser',
        port='5555',
        host='localhost',
        password='example'
    )
    cur = conn.cursor()

    if_table_exists_drop = '''
    DROP TABLE IF EXISTS HARASSER_TABLE
    '''
    cur.execute(if_table_exists_drop)

    create_table_sql = '''CREATE TABLE HARASSER_TABLE(
        ENTRY_ID INT,
        ENTRY_VALUE INT
    );'''
    cur.execute(create_table_sql)

    #if we can make that run n number of times concurrently?
    interference_number = 10000
    for i in range(interference_number):
        write_entry_to_db_sql = 'INSERT INTO HARASSER_TABLE (ENTRY_ID, ENTRY_VALUE) VALUES ({id}, {entry_val});'.format(id = i, entry_val = i)
        # create_entry_sql = 'INSERT INTO CONTROL_TABLE (ENTRY_ID, ENTRY_VALUE) VALUES ({id}, {entry_val});'.format(id = i, entry_val = i)
        print(write_entry_to_db_sql)
        cur.execute(write_entry_to_db_sql)
    conn.commit()

    #this does the init
    #then fills everything up, by a large number

    #method 1 a shitload of writes

    #method 2 a boatload of reads
    pass

# def harass():
harassinit()
