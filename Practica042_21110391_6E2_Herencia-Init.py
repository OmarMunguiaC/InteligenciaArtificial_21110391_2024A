
class Morro: #
    def __init__(tu, n, a): #jajaja dice tuna xd
        tu.n = n #
        tu.a = a #
    def simp(tu): #
        print('Tu nombre:', tu.n, '\nTus apellidos:', tu.a) #

class MorroPremium(Morro): #No manche profe, la misma cosa pero con esto otro de pormedio
    def __init__(tu, n, a, s): #jajaja dice tunas xd
        tu.n = n #como que ahi que procede profe
        tu.a = a #si sigue esto asi
        tu.s = s #su IA me va a detectar que estoy copiandome a mi mismo xd
    def simpP(tu):
        print('Tu nombre:', tu.n, '\nTus apellidos:', tu.a, '\nAprro, tu eres un', tu.s)

u1 = MorroPremium('Omar', 'Munguia Camacho','Sazonador xD') #No quiero morir por eso profe
u2 = Morro('Cesar', 'Carillo Alcaraz') #Tenga piedad de este sucio mortal
u2.n = 'Erland' #HURAAAII

u1.simpP() #Y si profe, la S es de sazonador xd
u2.simp() #Jaja, mi compa xd
