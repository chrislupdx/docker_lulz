import psycopg2
import sys, os
import subprocess
import timeit, time
from pprint import pprint

from harasser import harassinit

def avg(list):
    length = len(list)
    sum_list = sum(list)
    return sum_list / length

def init():
    #when init happens, we should also start up our harasser init

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

    #TODO CLOSE CONNECTION
    return sample_create_number

#what does bench actually call and what is it for?
def bench(sample_number):
    #when we call our control bench, we should also call harasser.harass()

    print("starting bench...")
    conn = psycopg2.connect(
            dbname='postgres_database',
            user='user0',
            port='5432',
            host='localhost',
            password='example'
            )
    cur = conn.cursor()

    #TODO MAKE THIS BENCH WORK 
    #bench 2: write every value from the database
    # read_times_2 = []
    # write_number = sample_number
    # for i in range(1, sample_number):
    #     print(' i is', i)
    #     #what is the harasser table called
    #     write = 'UPDATE CONTROL_TABLE SET ENTRY_VAlUE = \'{entry_value_to_edit}\' WHERE ENTRY_ID = \'{idval_to_id}\';'.format(entry_value_to_edit= write_number, idval_to_id=i)
    #     print(write)
    #     cur.execute(write)
    #     conn.commit()
    #     res = cur.fetchall()
    #     write_number -= 1

    #TODO we might want to loop this a few times
    #BENCH 2: read every value from the database, this might only measure the front of house's speed at generating these requests
    read_times = []
    for i in range(sample_number):
        read_cmd = 'SELECT * FROM CONTROL_TABLE WHERE ENTRY_ID = \'{id}\''.format(id = i)
        tic = time.perf_counter()
        cur.execute(read_cmd)
        res = cur.fetchall()
        toc = time.perf_counter()
        conn.commit()
        time_elapsed_for_one = toc - tic
        read_times.append(time_elapsed_for_one)

    max_val = max(read_times)
    min_val = min(read_times)
    avg_val = avg(read_times)
    print("max is", max_val, " min is ", min_val, " avg_val ", avg_val)

    return True

#this is the iterative version of it
def experiment():
    #this test is designed call benchmark() and harasssinit()
    samplenum = init()
    harassinit()
    bench(samplenum)
    pass

#TODO we need to implmement a multiprocess verison of this

experiment()