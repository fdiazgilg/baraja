
import baraja

barajaNueva = baraja.Baraja()
print("Hemos creado una baraja de cartas española:\n",barajaNueva.crearBaraja())
print("\nHemos mezclado una baraja de cartas española:\n",barajaNueva.mezclar(),"\n")
barajaNueva.repartir(7,6)
