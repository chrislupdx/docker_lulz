import psycopg2

print("susan")

#connect to the database
def init():
    conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            port='5432',
            host='localhost',
            password='example'
            )
    cur = conn.cursor()
    cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    #populate the table
    for i in range(1000):
        print(i)  

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
