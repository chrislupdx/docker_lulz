import psycopg2
import sys
import subprocess
import timeit

print("susan")

#connect to the database
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
    print("starting bench")
    #measures the performance of the db in terms of reads and writes

    #first connect to the db/do this for each database
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
        # cur.execute(add)
        # res = cur.fetchall()
        # print(res)

        val = 'cur.execute(' + add + ')'
        res = timeit.timeit(stmt=val, number=1)

        # res = cur.fetchall()
        print(res)

        # cmd = 'cur.execute(' + add + ' res= cur.fetchall())'
        # cmd = 'cur.execute(\'' + add + ';\')' #this is going to be a string how do we break #1719: putting quotes between the string didn't satisfy the syntax rules
        # cmd = 'cur.execute(\'' + add + ';\')'
        # print(cmd)
        # timeit.timeit(cmd)
        #this is the interpolated version we feed into timeit
        # cmd = 'curr.execute({sqladd})'.format(sqladd = add)
        # print('cmd is: ', cmd)        
        # one_read_time = timeit.timeit(cmd)
        # read_times.append(one_read_time)   

        #mean, max, min
        #get the mean of read_times
        #get the min of read_times
        #get the max of read_times

    #BENCH 2: re-write every value from database 
    #get an average and distribution of these metrics across 150 runs
    #get a distribution
    pass

sample_num = init()
#we might want more mechanical flexibility here
bench(sample_num)