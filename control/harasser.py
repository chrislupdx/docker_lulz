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
    cur.execute(if_table_exists_drop) #i don't know if this is happening

    create_table_sql = '''CREATE TABLE HARASSER_TABLE(
        ENTRY_ID INT,
        ENTRY_VALUE INT
    );'''
    cur.execute(create_table_sql)

    #TODO THIS SHOULD BE HARASS 1  
    #the number could be a factof of whatever you're initting in control
    interference_number = 1000
    for i in range(interference_number):
        write_entry_to_db_sql = 'INSERT INTO HARASSER_TABLE (ENTRY_ID, ENTRY_VALUE) VALUES ({id}, {entry_val});'.format(id = i, entry_val = i)
        cur.execute(write_entry_to_db_sql)
        conn.commit()
    
    #an update would be vicious
    conn.commit()

    #TODO close connection

    print("harasser done")
    pass

# def harass():
# a_harass = Harasser()
harassinit()

#todo do we need a harass->start?   
