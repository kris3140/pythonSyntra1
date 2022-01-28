
tekst = \
    "Ruim 50.000 kandidaten hengelen in Vlaanderen naar uw stem en hopen straks " \
    "gemeenteraadslid te worden. Het is maar de vraag of ze zo blij gaan zijn als die " \
    "droom in vervulling gaat. De inzet van de lokale verkiezingen, op 14 oktober, is " \
    "heel precies in cijfers vastgelegd: er moeten 7.398 nieuwe gemeenteraadsleden " \
    "verkozen worden, verspreid over de 308 Vlaamse gemeenten, plus 175 nieuwe " \
    "provincieraadsleden."


def split_paragraph(text, endofline):
    text_einde = (len(text))
    lijn_begin, spatie = 0, 0
    lijn_einde = endofline    # lijn einde verandert, endofline blijft vast
    splittext = '\n'          # we beginnen onze string met een blanco lijn
    for index in range(text_einde):
        if text[index] == ' ':
            spatie = index             #onthoud waar de laatste spatie stond
        if index == lijn_einde:
            splittext += (text[lijn_begin:spatie])      # voeg de tekst toe aan de tekst string
            splittext += '\n'                           # voeg nieuwe nieuwe lijn toe aan de tekst string
            lijn_begin = spatie + 1                     # reset lijn begin
            lijn_einde = lijn_begin + endofline         # reset lijn einde
        index += 1
        if index == text_einde:                        # op het einde plak je het laatste stuk tekst er nog bij
            splittext += (text[lijn_begin:text_einde])
    return splittext


gesplitte_tekst = split_paragraph(text=tekst, endofline=30)
print(gesplitte_tekst)
print('')
gesplitte_tekst = split_paragraph(text=tekst, endofline=50)
print(gesplitte_tekst)

