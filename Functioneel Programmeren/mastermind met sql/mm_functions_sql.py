import mysql.connector as mysql

config = {
'user': 'py_kris',
'password': 'ZVADygZNt5g1',
'host': '185.115.218.166',
'database': 'py_kris',
'raise_on_warnings': True
}

def create_new_SQL_record(antwoord):
    cnx = mysql.connect(**config)
    cursor = cnx.cursor()

    query = f"insert into mastermind set mm_datumtijd = now(), mm_antwoord = '{antwoord}';"
    cursor.execute(query)
    cnx.commit()
    return cursor.lastrowid     # met deze rij vervang je de lijnen hieronder + je loopt niet het gevaar
    # dat er iemand anders ondertussen een rij toevoegt.


    # query ="select mm_id from mastermind order by mm_id desc limit 1;"
    # OF korter : query = "select max(mm_id) from mastermind"
    # cursor.execute(query)
    # for row in cursor:
    #     recordID = row[0]
    # cursor.close()
    # cnx.close()
    # return recordID

def update_SQL_afgebroken(goklijst, recordID):
    cnx = mysql.connect(**config)
    cursor = cnx.cursor()

    query = f"update mastermind set mm_afgebroken = now(), mm_input = '{goklijst}' WHERE mm_id ='{recordID}'"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()

def update_SQL_opgelost(goklijst, recordID):
    cnx = mysql.connect(**config)
    cursor = cnx.cursor()

    query = f"update mastermind set  mm_opgelost = now(), mm_input = '{goklijst}' WHERE mm_id ='{recordID}'"
    cursor.execute(query)
    cnx.commit()
    cursor.close()
    cnx.close()
