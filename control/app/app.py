import psycopg2
import sys
import subprocess

print("susan")

#connect to the database
def init():
    conn = psycopg2.connect(
            dbname='postgres_database',
            user='user0',
            port='5432',
            host='localhost',
            password='example'
            )
    cur = conn.cursor()

    #check if CONTROL_TABLE EXISTS
        #IF IT DOES DROP IT
    if_table_exists_drop = '''
    DROP TABLE IF EXISTS CONTROL_TABLE
    '''
    cur.execute(if_table_exists_drop)

    create_table_sql = '''CREATE TABLE CONTROL_TABLE(
        ENTRY_ID INT,
        ENTRY_VALUE INT
    );'''
    cur.execute(create_table_sql)
    
    sample_create_number = 100
    for i in range(sample_create_number):
        create_entry_sql = 'INSERT INTO CONTROL_TABLE (ENTRY_ID, ENTRY_VALUE) VALUES ({id}, {entry_val});'.format(id = i, entry_val = i)
        cur.execute(create_entry_sql)

    conn.commit()

    #thid display isn't working
    cur.execute("select * from CONTROL_TABLE;")
    # result = cur.fetchall()
    # print("result set: ", "\n", result)

    #display table
    # cur.execute("\\dt")    
    # res = subprocess.run('psql -c "\d+ my_table" test postgres', stdout=subprocess.PIPE)
    # print(res.stdout.decode(sys.stdout.encoding))
    #populate the table
    # for i in range(1000):
        #create entries
        # print(i)  

    pass

#bench
def bench():
    
    #time return time
    #for i in 1000();
        #GET thing
    #get an average
    #get a distribution
    pass

init()
