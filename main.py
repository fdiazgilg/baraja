class Baraja:

    def __init__(self):
        self.palo = ('o','c','e','b')
        self.numero = ('A','2','3','4','5','6','7','S','C','R')
        self.baraja = self.crearBaraja()
        self.sinCartas = False
    
    def crearBaraja(self):
        barajaNueva = []
        for palo in self.palo:
            for num in self.numero:
                barajaNueva.append(num+palo)
        
        return barajaNueva

    def mezclar(self):
        import random
        mezclada = self.baraja
        for i in range(len(mezclada)):
            cartaOut = random.choice(mezclada)
            indiceOut = mezclada.index(cartaOut)
            cartaIn = mezclada.pop(indiceOut)
            mezclada.insert(i,cartaIn)

        return mezclada
    
    def repartir(self,mano,jugadores):
        reparto = self.baraja
        partida = []
        try:
            for i in range(jugadores):
                partida.append([])
                for j in range(mano):
                    carta = reparto.pop(0)                
                    partida[i].append(carta)                
                print("Las cartas del jugador {} son {}.".format(i+1,partida[i]))
       
        except:
            juego.sinCartas = True
        
        return reparto


if __name__ == '__main__':
    juego = Baraja()
    baraja = juego.crearBaraja()
    print("Las cartas ordenadas de la baraja española:\n",format(baraja))
    barajada = juego.mezclar()
    print("\nLas cartas mezcladas de la baraja española:\n",format(barajada),"\n")
    restoBaraja = juego.repartir(5,5)
    if not juego.sinCartas:
        print("\nLas cartas sobrantes después de iniciar la partida:\n",format(restoBaraja))
        restoMezc = juego.mezclar()
        print("\nVolvemos a mezclar las cartas que han sobrado tras iniciar la partida:\n",format(restoMezc))
    else:
        print("\nLo siento, pero no tenemos cartas para todos los jugadores.")
