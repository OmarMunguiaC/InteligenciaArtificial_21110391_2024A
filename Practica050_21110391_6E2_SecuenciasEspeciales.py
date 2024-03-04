
import re #Odugen Taiga Song - Saidash (besto para programar xdxdxd)

frase1 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind1 = re.findall("[a-c]", frase1) #de una letra a otra del abecedario
print(faind1)

frase2 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind2 = re.findall("[lo{2}]", frase2) #palabra con multiples letras
if faind2:
    print('Valido')
else:
    print('No valido')

frase3 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind3 = re.findall("caldo|coctel", frase3) #un resultado u otro
if faind3:
    print('Si hay')
else:
    print('No hay')

frase4 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind4 = re.findall("tu...er", frase4) # '.' reemplaza cualquier valor dentro de un string
if faind4:
    print('Si existen coincidencias')
else:
    print('No existen coincidencias')

frase5 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind5 = re.findall('lu*', frase5) #El final del string
if faind5:
    print('Pozole')
else:
    print('Tostadas')


frase6 = 'Wena mecha ina sama, tu ma jart bit saund, wi fel in loo, as de lifs tur braun, an wi ca bi tugeder beibi, as de skais ar blu'
faind6 = re.findall('^Wena', frase6) #El inicio del string
if faind6:
    print('Gansito')
else:
    print('Coca')
