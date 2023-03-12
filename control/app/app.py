import psycopg2
import sys
import subprocess
import timeit, time

def init():
    print("starting init")
    conn = psycopg2.connect(
            dbname='postgres_database',
            user='user0',
            port='5432',
            host='localhost',
            password='example'
            )
    cur = conn.cursor()

    #check if CONTROL_TABLE EXISTS, IF IT DOES DROP IT
    if_table_exists_drop = '''
    DROP TABLE IF EXISTS CONTROL_TABLE
    '''
    cur.execute(if_table_exists_drop)

    create_table_sql = '''CREATE TABLE CONTROL_TABLE(
        ENTRY_ID INT,
        ENTRY_VALUE INT
    );'''
    cur.execute(create_table_sql)
    
    #we could throw booleean flags for read and writen                                 
    sample_create_number = 10
    for i in range(sample_create_number):
        create_entry_sql = 'INSERT INTO CONTROL_TABLE (ENTRY_ID, ENTRY_VALUE) VALUES ({id}, {entry_val});'.format(id = i, entry_val = i)
        cur.execute(create_entry_sql)
    conn.commit()

    cur.execute("select * from CONTROL_TABLE;")
    res = cur.fetchall()
    print("result set: ", "\n", res)
    return sample_create_number

def bench(sample_number):
    print("starting bench...")
    conn = psycopg2.connect(
            dbname='postgres_database',
            user='user0',
            port='5432',
            host='localhost',
            password='example'
            )
    cur = conn.cursor()

    #BENCH 1: read every value from the database, this might only measure the front of house's speed at generating these requests
    read_times = []
    for i in range(sample_number):
        add = 'SELECT * FROM CONTROL_TABLE WHERE ENTRY_ID = \'{id}\''.format(id = i)
        tic = time.perf_counter()
        cur.execute(add)
        res = cur.fetchall()
        toc = time.perf_counter()
        time_elapsed_for_one = toc - tic
        read_times.append(time_elapsed_for_one)
    print('times are ', read_times)
    pass

sample_num = init()
bench(sample_num)