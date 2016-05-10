# pseudocode;
# begin met een kleine grid
# kan je de huisjes erkennen & waarde berekenen?
# kan je de huisjes van positie laten veranderen die legitime is en waarde berekenen
# dan algoritme toepassen, kijken of er nog een kans is dat dit algoritme aangenomen kan worden
# exp^(current - neighboor solution)/ (value) --- hoe kleiner het verschil& hoe hoger de waarde, des te waarschijnlijker aangenomen te worden.

# values initialiseren van soorten huisjes en de waarde erbij

Small_house = 285000
obligatory_space = 0
extra_space_Small_house = 8550 #voor iedere nieuwe ring extra ruimte

bungalow = 399000
extra_space_bungalow = 15960

maison = 610000
extra_space_maison = 366000

water = 0 #verplciht

#erkennen van huisjes en vrije ruimte
def analyze(self):
	
def anneal(solution):
	old_value_grid = value_grid(solution)
	# of T = 1 definitely switch, 0.0 stay put, if you know the acceptance prob. the it is compared to a radom
	# generated number between 0 and 1. if the appect. prob. is larger than the random number then you are switching 

	T = 1.0
	T_min = 0.00000001
	alpha = 0.9
	while T < T_min:
		i = 1
		while i <= 100:
			new_value_grid = neighboor(solution)
			new_value_ genereted = value(new_solution)
			ap = acceptance_probability(old_value_grid, new_value_grid, T)
			if ap > random():
				solution = new_solution
				old_value_grid = new_value_grid
			i+=1
		T = T * alpha
	return solution, old_value_grid	

	return math.exp( -abs(new_value_grid - old_value_grid)/ value?)		


set a  random move

calculate the value of the grid.
value_grid = ((28500 * Small_house) + (8550 * extra_space_Small_house)) + ((399000 * bungalow) + (15960 * extra_space_bungalow)) + ((610000 * maison) + (366000 * extra_space_maison)) 

set a new random neighboor solution

calculate the cost of the new solution

compare them



# small house = 285000 (zien als 1 unit) (8 * 8 = 64)(voor iedere 64 blokken aan elkaar gerensend met een 1 waarde, value toevoegen )
# extra_space_Small_house = 3% van 285000 (voor  iedere ring van 3en op het veld) 

# (eerste ring voor 3% waarde vermeerdering = 43 2tjes, bij 94 6% waarde vermeerdering )
# ( voor iedere  ruimte = lengte +(2*extra_space_Small_house) * breedte + (2*extra_space_Small_house) - (lengte*breedte))


# bungalow = 399000 (10 * 7.5 = 75 blokken aaneensluitend met waarde 4, value toevoegen)
# extra_space_bungalow = 4% van 399000
# maison = 610000
# extra_space_maison = 6% van 610000

# som_waarde = Small_house * 285000 + (for every 3 in Field add )

