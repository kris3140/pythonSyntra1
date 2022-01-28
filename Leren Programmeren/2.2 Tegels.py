# input #############################################################################

lengte = int(input("Lengte van de kamer? "))
breedte = int(input("Breedte van de kamer? "))
vierkante_tegel =  int(input("Vierkante tegel. Wat is de lengte van een zijde? "))

# bereken en print #########################################################################
import math

aantal_tegels_len = math.ceil(lengte / vierkante_tegel)
aantal_tegels_br = math.ceil(breedte / vierkante_tegel)
totaal_tegels = aantal_tegels_br * aantal_tegels_len


print('Je moet %d tegels van %.2f x %.2f meter kopen voor een kamer van %d op %d meter' % (totaal_tegels, vierkante_tegel, vierkante_tegel, lengte, breedte))