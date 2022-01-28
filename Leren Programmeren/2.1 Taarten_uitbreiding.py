# input #############################################################################

aantal_taarten = int(input("hoeveel taarten heb je? "))
aantal_deelnemers = int(input("hoeveel deelnemers zijn er? "))

# berekening ########################################################################

grote_stukken = aantal_deelnemers // aantal_taarten
kleine_stukken = grote_stukken + 1

getal = grote_stukken * aantal_taarten
taarten_in_ks = aantal_deelnemers - getal
taarten_in_gs = aantal_taarten - taarten_in_ks


print('je hebt %d taarten voor %d deelnemers' % (aantal_taarten, aantal_deelnemers))
print('je moet %d taarten in %d stukken snijden.' % (taarten_in_gs, grote_stukken))
if taarten_in_ks > 0:
    print('en %d taarten in %d stukken.  ' % (taarten_in_ks, kleine_stukken) )


# controle ###########################################################################
print(' ')
print(' ')
controle = (taarten_in_gs * grote_stukken) + (taarten_in_ks * kleine_stukken)
if taarten_in_ks > 0:
    print('controle : (%d taarten x %d stukken) + (%d taarten x %d stukken) = %d deelnemers ' % (taarten_in_gs, grote_stukken, taarten_in_ks, kleine_stukken, controle))
else:
    print('controle : (%d taarten x %d stukken) = %d deelnemers ' % (taarten_in_gs, grote_stukken, controle))
