

def StudentToTable(dict):
    print('<h1>Student</h1>')
    print('<table>')
    for veldnaam, veldinhoud in student.items():
        veldnaam = veldnaam[0].upper() + veldnaam[1:]
        veldinhoud = str(veldinhoud)
        print('<tr><td>'+veldnaam+'</td><td>'+veldinhoud+'</td></tr>')
    print('</table>')



student =	{
"voornaam": "Jan",
"naam": "Janssens",
"straat": "Oude baan",
"huisnr": "22",
"postcode": 2800,
"gemeente": "Mechelen",
"geboortedatum": "14/05/1991",
"telefoon": "015 24 24 26",
"e-mail": "jan.janssens@gmail.com"
}



StudentToTable(student)
