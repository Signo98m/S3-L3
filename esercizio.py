def perimetro():
	print ("Il seguente programma  esegue il calcolo dei vari perimetri")
	print  ("""
	- Quadrato 1
	- Rettangolo 2
	- Circonferenza 3
	""")

	print ("Inserisci la selta")
	scelta = int(input("1 Quadrato 2 Rettangolo 3 Circonferenza"))
	if scelta == 1:
	   print ("Hai selezionato il perimetro del Quadrato")
	   lato = float(input("Inserisci il valore del lato"))
	   print ("Il permetro del Quadrato", lato, " è:", lato*4)
	elif scelta == 2:
	   print ("Hai selezionato il perimetro del Rettangolo")
	   base = float(input("Inserisci il valore della base "))
	   altezza = float(input("Inserisci il valore dell altezza"))
	   print ("Il perimetro del Rettangolo che ha per base", base, "e altezza", altezza, "è", base*2 + altezza*2)
	elif scelta == 3:
	   print ("Hai scelto la Circonferenza")
	   r = float(input("Inserisci il valore del raggio"))
	   print ("Il perimetro del cerchio",r, "è",2* r* 3.14)
	else:
	   print ("Inserire una scleta valida")

perimetro();
