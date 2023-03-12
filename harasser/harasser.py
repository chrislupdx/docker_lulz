import psycopg2

def harass():
    conn = psycopg2.connect(
        dbname='harasser_db',
        user='user0',
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
        write_entry_to_db_sql = 'INSERT INTO '

    #this does the init
    #then fills everything up, by a large number

    #method 1 a shitload of writes

    #method 2 a boatload of reads

