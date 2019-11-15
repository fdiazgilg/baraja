class Baraja:

    def __init__(self):
        self.palo = ('o','c','e','b')
        self.numero = ('A','2','3','4','5','6','7','S','C','R')
    
    def crearBaraja(self):
        barajaNew = []
        for palo in self.palo:
            for num in self.numero:
                barajaNew.append(num+palo)
        
        return barajaNew

    def mezclar(self):
        import random
        mezclada = self.crearBaraja()
        for i in range(len(mezclada)):
            cartaOut = random.choice(mezclada)
            indiceOut = mezclada.index(cartaOut)
            cartaIn = mezclada.pop(indiceOut)
            mezclada.insert(i,cartaIn)

        return mezclada
    
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
        
        return baraja
