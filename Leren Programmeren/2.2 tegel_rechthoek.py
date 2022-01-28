# input #############################################################################

lengte = float(input("Lengte van de kamer? "))
breedte = float(input("Breedte van de kamer? "))
tegel_len =  float(input("Wat is de lengte van een tegel? "))
tegel_br =  float(input("Wat is de breedte van een tegel? "))


# bereken en print #########################################################################
import math

tegels_leninlen = math.ceil(lengte / tegel_len)
tegels_brinbr = math.ceil(breedte / tegel_br)
totaal_tegels_lenlen = tegels_brinbr * tegels_leninlen

tegels_leninbr = math.ceil(lengte / tegel_br)
tegels_brinelen = math.ceil(breedte / tegel_len)
totaal_tegels_lenbr = tegels_leninbr * tegels_brinelen


print(' ')
print('Als je de tegels met de langste zijde in de lengterichting plaatst: ')
print('Dan moet je %d tegels van %.2f x %.2f meter kopen voor een kamer van %d op %d meter' % (totaal_tegels_lenlen, tegel_len, tegel_br, lengte, breedte))
print(' ')
print('Als je de tegels met de langste zijde in de breedterichting plaatst: ')
print('Dan moet je %d tegels van %.2f x %.2f meter kopen voor een kamer van %d op %d meter' % (totaal_tegels_lenbr, tegel_len, tegel_br, lengte, breedte))