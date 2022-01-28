from mastermind_functions import get_random, get_input, check_juiste, check_foute

kleurenLijst = ['R', 'G', 'B', 'O', 'P', 'W']
antwoordLijst = get_random(kleurenLijst)
while True:
    gokLijst = get_input(antwoordLijst)
    if gokLijst == 'stop': break
    aantal_juiste = check_juiste(antwoordLijst, gokLijst)
    if aantal_juiste == 'alles geraden': break
    check_foute(aantal_juiste)
