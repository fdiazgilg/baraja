
import baraja

barajaNueva = baraja.Baraja()
print("Hemos creado una baraja de cartas española:\n",barajaNueva.crearBaraja())
print("\nHemos mezclado una baraja de cartas española:\n",barajaNueva.mezclar(),"\n")
restoBaraja = barajaNueva.repartir(5,6)
print("\nLas cartas que sobran después de repartir son: ",restoBaraja)
