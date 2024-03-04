
eda = int(input('¿Cual es tu edad?\n'))
if eda <= 0:
	print('Como que menos de 0 años, estas loco? o k')
elif eda >= 1 and eda <= 18:
	print('Puedes siquiera escribir we?')
elif eda > 18 and eda <= 45:
	print('Vale, te la compro ijo')
elif eda > 45 and eda <= 100:
	print('Ya estas ruco ijo, consiguete la pension')
elif eda > 100 and eda <= 300:
	print('Sientete feliz, superaste a la reina Isabelle')
else:
	print('Anota algo que valga la pena revisar ijo xd')
