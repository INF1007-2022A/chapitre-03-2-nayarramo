#!/usr/bin/env python


from ast import Num


def dissipated_power(voltage, resistance):
	# Calculer la puissance dissipée par la résistance.
	result = voltage*voltage/resistance
	return result

def orthogonal(v1, v2):
	# Retourner vrai si les vecteurs sont orthogonaux, faux sinon.

	if v1[0] * v2[0] + v1[1] * v2[1] == 0:
		return True
	else:
		return False


def average(values):
	# Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	list = []
	for v in values:
		if v >= 0:
			list.append(v)

	result = sum(list)/len(list)
	return result

def bills(value):
	# Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, ones = 0, 0, 0, 0
	
	while value != 0:
		if value >= 20:
			twenties = value // 20
			value = value%20
		elif value >= 10:
			tens = value // 10
			value = value%10
		elif value >= 5:
			fives = value // 5
			value = value%5
		elif value >= 1:
			ones = value
			value = 0
	return (twenties, tens, fives, ones)

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
