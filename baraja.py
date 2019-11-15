class Baraja:

    def __init__(self):
        self.palo = ('o','c','e','b')
        self.numero = ('A','2','3','4','5','6','7','S','C','R')
    
    def crearBaraja(self):
        baraja = []
        for key in self.palo:
            for item in self.numero:
                baraja.append(item+key)
        
        return baraja

    def mezclar(self):
        import random
        baraja = self.crearBaraja()
        for i in range(len(baraja)):
            cartaOut = random.choice(baraja)
            indiceOut = baraja.index(cartaOut)
            cartaIn = baraja.pop(indiceOut)
            baraja.insert(i,cartaIn)

        return baraja
    
    def repartir(self,mano,jugadores):
        baraja = self.mezclar()
        partida = []
        try:
            for i in range(jugadores):
                partida.append([])
                for j in range(mano):
                    carta = baraja.pop(0)                
                    partida[i].append(carta)                
                print("Las cartas del jugador {} son {}.".format(i+1,partida[i]))
        
        except:
            print("\nLo siento, pero no tenemos cartas para todos los jugadores.")
