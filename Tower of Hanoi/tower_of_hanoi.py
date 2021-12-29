class Tower_of_Hanoi():
	'''
	Tower of Hanoi
	
	The Tower of Hanoi is a mathematical puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod:

	The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
 	- Only one disk can be moved at a time.
 	- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
 	- No disk may be placed on top of a smaller disk.
	'''
	def __init__(self, DISKS):
	
		'''
		Initialize the game with the number of disks. All disks are placed on the left rod. 
		'''
		# Number of disks
		self.DISKS = DISKS

		# Rods
		self.left = [disk for disk in range(self.DISKS, 0, -1)]
		self.mid = []
		self.right = []

		# Move Counter
		self.counter = 0


	### Methods
	def update_screen(self):
		'''
		update screen to show current game state
		'''
		
		print('__' * (self.DISKS + 2), f'Move: {self.counter}', sep = '\t')
		print(self.left)
		print(self.mid)
		print(self.right)
	
	
	def game_over(self):
		'''
		Win Condition
		'''
		
		return len(self.left) == len(self.mid) == 0

	def can_move(self, disk, rod):
		'''
		No disk may be placed on top of a smaller disk.
		'''
		
		if len(rod)==0:
			return True
		
		else:
			return rod[-1] > disk
	

	def move(self, source, target):
		'''
		Move disk from one rod to another
		'''
	
		if self.can_move(source[-1], target):
			target.append(source.pop())
			self.counter += 1
			self.update_screen()
			
				
		else:
			print("Illegal Move")
		
		if self.game_over():
			print("You Win !!!")
			
	def real_solver(self, source, target, bridge, disks):

		'''
		Tower of Hanoi Solver Algorithm
		'''
		
		if disks == 1:
			self.move(source, target)
		
		else:
			self.real_solver(source, bridge, target, disks-1)
		
			self.move(source, target)
		
			self.real_solver(bridge, target, source, disks-1)

if __name__ == '__main__':

	DISKS = int(input("Enter the initial number of disk: \n"))

	game = Tower_of_Hanoi(DISKS)

	game.update_screen()
	
	# Try to win the game one move at a time
	#game.move(game.left, game.right)

	# If you can't, watch the solution
	game.real_solver(game.left, game.right, game.mid, game.DISKS)

	#help(Tower_of_Hanoi)
