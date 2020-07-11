from random import shuffle


class Card(object):
    def __init__(self,renk,val):
        self.renk = renk
        self.value = val

    def show(self): 
        if self.value == '1':
            val = "As"
        elif self.value == '11':
            val = "Vale"
        elif self.value == '12':
            val = "Kız"
        elif self.value == '13':
            val = "Papaz"
        else:
            val = self.value   
        return "{} {}".format(self.renk,val)
    
    def __str__(self):
        return self.show    

        


class Deck():
    def __init__(self):
        self.cards = []
        self.CreateDeck()
        

    def CreateDeck(self):
        self.cards = []
        for i in ['Kupa' , 'Sinek' , 'Karo' , 'Maça'] :
            for j in ['1','13','12','11','10','9','8','7','6','5','4','3','2']:
                self.cards.append(Card(i,j))

    def Shuffle(self):
        shuffle(self.cards)


    def deal(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            print(card.show())   






class Oyuncu(object):
    def __init__(self,name):
        self.name = name
        self.hand = []

    def Çek(self,deck,range):
        while range > 0:
            
            card = deck.deal()
            self.hand.append(card)
            range = range-1

    def show(self):
        for card in self.hand:
            print(card.show())

    def say(self):
        toplam = 0
        ascounter = 0
        for card in self.hand:
            if card.value == '1':
                ascounter+=1
            elif card.value == '12':
                toplam += 10
            elif card.value == '13':
                toplam += 10
            elif card.value == '11':
                toplam += 10                        
            else:
                toplam += int(card.value)
        if ascounter == 1 and toplam <= 10:
            toplam+=11        
        elif ascounter ==1 and toplam > 10:
            toplam+=1
        return toplam
    
    def showCount(self,num):
        for card in self.hand:
            print(card.show())
            if num == 0:
                break
            num-=1 
                  
            

kurpiyer = Oyuncu("dealer")
akif = Oyuncu("akif")
dek = Deck()
dek.Shuffle()
kurpiyer.Çek(dek,1)
dek.Shuffle()
akif.Çek(dek,1)  
dek.Shuffle()
akif.Çek(dek,1)
dek.Shuffle()
kurpiyer.Çek(dek,1)


game = "Play"

while (game!="exit"):
    print("Kurpiyer :")
    kurpiyer.showCount(0)
    
    print("Player :")
    akif.show()
    
    if akif.say() == 21:
        print("BlackJack!!!")
        print("player Hand:")
        akif.show()
        break
    elif akif.say() > 21:
        print("BATTIN!")
        print("player Hand:")
        akif.show()
        break
    
    elif kurpiyer.say()>21:
        print("KURPIYER BATTI!")
        print("Dealer Hand:")
        kurpiyer.show()
        break    

    
    game = input("Hit(h) or Stay(s)\n")
    if game == 'h':
        akif.Çek(dek,1)
        print("player hand:")
        akif.show()
    elif kurpiyer.say()<=16:
        kurpiyer.Çek(dek,1)    
    elif akif.say() > kurpiyer.say():
        print("PLAYER KAZANDI!")
        print("player Hand:")
        akif.show()
        print("Dealer Hand:")
        kurpiyer.show()   
        break
    elif akif.say() == kurpiyer.say():
        print("BERABERE! ")
        print("player Hand:")
        akif.show()
        print("Dealer Hand:")
        kurpiyer.show()
        break
    else:
        print("KURPİYER KAZANDI")
        print("player Hand:")
        akif.show()
        print("Dealer Hand:")
        kurpiyer.show()
        break
    
    
       

