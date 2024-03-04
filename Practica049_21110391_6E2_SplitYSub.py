
import re #Libreria RegEx

palabrota = "avrsisimepuedesencontrarvamosaprobarelpoderdeestacosaavrsisimuyvrgaspuedecontodoyconmitareaymisproblemasemocionalesxd"
busk = re.split('poder', palabrota) #borrara todos los "poder"? xd, avr k pasa
print(busk)

palabrota = "avrsisimepuedesencontrarvamosaprobarelpoderdeestacosaavrsisimuyvrgaspuedecontodoyconmitareaymisproblemasemocionalesxd"
busk = re.split('si', palabrota, 2) #Split pero solo dos veces xd
print(busk)

palabrota = "avrsisimepuedesencontrarvamosaprobarelpoderdeestacosaavrsisimuyvrgaspuedecontodoyconmitareaymisproblemasemocionalesxd"
busk = re.sub('si', 'no', palabrota) #Cambia los 'si' por 'no'
print(busk)

palabrota = "avrsisimepuedesencontrarvamosaprobarelpoderdeestacosaavrsisimuyvrgaspuedecontodoyconmitareaymisproblemasemocionalesxd"
busk = re.sub('si', 'no', palabrota, 2) #Solo cambia 2 'si' por 'no'
print(busk)

#no ps si k puede profe xd, me sorprendio la vdd
