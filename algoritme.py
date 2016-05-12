def hillclimb (init_value_grid, move, max_repetitions):
	best = value_init_grid
	
	repetitions = 1

	while repetitions < max_repetitions:
		#search for next grid
		roep new grid functie aan. 
		calculater(new_grid) (deze returned value_new_grid
		for next in move(best):
			if repetitions >= max_repetitions:
				break

		value_new_grid = calculater(new_grid)
		repetitions +=1
		# Is this grid better?
		if value_new grid > value_init_grid
			best = value_new_grid
			move_made = True
			break 

		if not move_made:
			break
			print "couldn't find a better move"	

def new_grid (init_grid):
	## pak een random huisje en verzet het in een random richting. (misschien met een kleine range)
	# def move_house(current_state, move):
	    """
        Return a random position inside the room.
        returns: a Position object.
        """
        random_house = pick random house and change its position random.
        
        # get random numbers to generate a random position in room
        # constraints in de functie waar hij aangeroepen wordt
        # minus 18 because every house extands 18 tiles to the right and down (16m + 2m free space)
        # used to be 23, dont know why
        ran_x = random.randint(0, width - 28) 
        ran_y = random.randint(0, depth - 28)
        ran_pos = Position(ran_x, ran_y)
        return ran_pos

        set in init_grid
        return new_grid

 # 	pos.x, pos.y = current_state

 # 	if move == 'up':
 # 		pos.x += 1
 # 	elif move == 'down':
 # 		pos.x -= 1
 # 	elif move == "right"
 # 		pos.y += 1
 # 	else:
 # 		pos.y -= 1
 # 	next_state = pos.x, pos.y	

 	return new_grid

def calculater (new_grid): 
	extra_space_Small_house = 0
	extra_space_bungalow = 0
	extra_space_maison = 0
	for every rand van 4'en in de grid:
		extra_space_Small_house++;
	for every rand van 5'en in de grid:
		extra_space_bungalow++;
	for every rand van 6'en in de grid:
		extra_space_maison++	

	value_new_grid = 3435000 + (8550 * extra_space_Small_house) + (15960 * extra_space_bungalow) + (366000 * extra_space_maison);
	return value_new_grid;	
	
def anneal(solution):
	old_value_grid = value_grid(solution)
	# of T = 1 definitely switch, 0.0 stay put, if you know the acceptance prob. the it is compared to a radom
	# generated number between 0 and 1. if the appect. prob. is larger than the random number then you are switching 
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


def new_grid (init_grid, move);
	def move_house(current_state, move):
 	pos.x, pos.y = current_state

 	if move == 'up':
 		pos.x += 1
 	elif move == 'down':
 		pos.x -= 1
 	elif move == "right"
 		pos.y += 1
 	else:
 		pos.y -= 1
 	next_state = pos.x, pos.y	

 	return next_state			
