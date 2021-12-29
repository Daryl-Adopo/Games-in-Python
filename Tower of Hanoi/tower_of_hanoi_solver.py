'''
	Tower of Hanoi
	
	The Tower of Hanoi is a mathematical puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod:

The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
 	- Only one disk can be moved at a time.
 	- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
 	- No disk may be placed on top of a smaller disk.

	For a general algorithm, we need to divide the stack into two parts - the largest disk (nth disk) is in one part and all other (n-1) disks are in the second part.
Our ultimate goal is to move disk n from source to destination and then put all other (n-1) disks onto it. 
So, we can break up the problem into smaller problems and come up with a general algorithm:

Step 1: Move n-1 disks from source to the middle (Let's call it the bridge).

Step 2: Move nth disk (largest Disk)from source to destination.

Step 3: Move n-1 disks from the bridge to destination (On top of the largest disk)

With 3 disks, the puzzle can be solved in 7 moves. 
The minimal number of moves required to solve a Tower of Hanoi puzzle is 2^n-1, where n is the number of disks.
'''

'''
Solution

Let's Start with a simple case switch solver to understand how to win the game
'''
	
def solver(source, target, bridge, disks):

	# Case 1
	# with one disk, we only need one step
	if disks == 1: 
		
		move(source, target) # Step 2
	
	# Case 2	
	elif disks == 2:
	
		move(source, bridge) # Step 1
		
		move(source, target) # Step 2
		
		move(bridge, target) # Step 3
		
	# With more than 2 disks (n > 2) we need to perform the previous case (case n-1) to move the n-1 disks out of the way. Then, we move the base disk to the destination. Finally the previous case again to move the n-1 disks on top of the largest disk. 
	
	# Case 3	
	elif disks == 3:
		
		# Case 2
		move(source, target) 
		move(source, bridge) # Step 1
		move(target, bridge)
		
		move(source, target) # Step 2
		
		# Case 2
		move(bridge, source)
		move(bridge, target) # Goal of Beta
		move(source, target)
	
	# Case 4
	elif disks == 4:
	
		# Case 3
		move(source, bridge)
		move(source, target)
		move(bridge, target)
		move(source, bridge) # Step 1
		move(target, source)
		move(target, bridge)
		move(source, bridge)
		
		move(source, target) # Step 2
		
		# Case 3
		move(bridge, target)
		move(bridge, source)
		move(target, source)
		move(bridge, target) # Step 3
		move(source, bridge)
		move(source, target)
		move(bridge, target)
		
	## And so on...

'''
Now let's use this knowledge and recursion to create a scalable Tower of Hanoi solver Algorithm
'''
			
def real_solver(source, target, bridge, disks):
	if disks == 1:
		move(source, target)
		
	else:
		# Case n-1
		real_solver(source, bridge, target, disks-1) # Step 1
		
		move(source, target) # Step 2
		
		# Case n-1
		real_solver(bridge, target, source, disks-1) # Step 3

'''
Finally, we can implement our pseudo code and visualize the game
'''

def update_screen():
	global counter
	
	print('__' * (DISKS + 2), f'Move: {counter}')
	print(left)
	print(mid)
	print(right)
	
def game_over():
	return len(left) == len(mid) == 0

def can_move(disk, target):
	if len(target)==0:
		return True
		
	else:
		return target[-1] > disk
	

def move(source, target):
	global counter
	
	if can_move(source[-1], target):
		target.append(source.pop())
		counter += 1
		update_screen()
				
	else:
		print("Illegal Move")
		
	if game_over():
		print("You Win !!!")
		
# Initial State
DISKS = int(input("Please Enter the initial number of disks: "))

left = [disk for disk in range(DISKS, 0, -1)]
mid = []
right = []

counter = 0

update_screen()
real_solver(left, right, mid, DISKS)

'''
Thank you for making it this far! Don't forget to upvote the code if it was helpful so that more people can be helped. 
'''