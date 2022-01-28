import mysql.connector as mysql

def get_sqldata(requested_data):

    tabel = ""

    if requested_data == '/films':
        dbase = 'sakila'
        query = '''select title, rental_rate, count(rental_id) as aantal
                from film
                left join inventory on film.film_id = inventory.film_id
                left join rental on inventory.inventory_id = rental.inventory_id
                group by title
                order by aantal DESC
                limit 30;'''
        tabel += f'<tr><th>film</th><th>huurprijs</th><th>verhuringen</th></tr>'
    elif requested_data == '/gemeenten':
        dbase = 'covid19'
        query = '''select det_txt_nl as Gemeente, det_txt_fr as Commune, det_cases as Aantal_besmettingen
                from gemeente
                order by Aantal_besmettingen desc
                limit 100;'''
        tabel += f'<tr><th>gemeente</th><th>commune</th><th>aantal gevallen</th></tr>'

    config = {
    'user': 'root',
    'password': 'Gloeilamp+123',
    'host': '127.0.0.1',
    'database': dbase,
    'raise_on_warnings': True
    }   # dit is local host

    cnx = mysql.connect(**config)
    cursor = cnx.cursor()
    cursor.execute(query)

    for row in cursor:
        tabel += f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>'


    cursor.close()
    cnx.close()

    return(tabel)

