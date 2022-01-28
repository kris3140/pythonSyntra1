# berekening kapitaal en rente

kapitaal = float(input("Wat is het kapitaal? "))
interestvoet = float(input("Wat is de intrest in procenten? "))
looptijd = int(input("Wat is de looptijd? "))
limiet_jn = str(input("Is er een limiet (j/n)? "))
limiet = int(input("Wat is de limiet? "))

print(' Jaar', ' '*4, 'Kapitaal', ' '*4,' Rente' )


for i in range(looptijd):
    jaar = i + 1
    rente = kapitaal * interestvoet / 100
    #formateer rente en kapitaal met 2 decimalen
    rente, kapitaal = format(rente, ".2f" ), format(kapitaal, ".2f" )
    #bereken de lengte van rente, kapitaal en jaar
    rlen, klen, jlen = len(str(rente)), len(str(kapitaal)), len(str(jaar))
    #print
    print(' '*(4-jlen), jaar, ' '*(12-klen), kapitaal, ' '*(10-rlen), rente)
    #bereken het kapitaal van het volgende jaar
    kapitaal = float(kapitaal) + float(rente)
    if kapitaal > limiet and limiet_jn == 'j':
        print('De limiet zal in jaar %d overschreden worden' % (jaar + 1))
        break





