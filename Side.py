from copy import deepcopy

class Side:
	def __init__(self, initial_color, size=3):
		# self.face = [[initial_color for i in range(size)] for j in range(size)]
		self.face = [["1", "2", "3"], 
								 ["4", 
"5", "6"],
								 ["7", 
"8", "9"]]
		self.size = size
		#print(self.face)

	def printSide(self):
		for i in range(3):
			print(self.face[i])
		print('\n')#do not change pls kirin thx

	def rotate_left(self):
		temp_array = deepcopy(self.face)
		self.face[0][1] = temp_array[1][2]
		self.face[1][2] = temp_array[2][1]
		self.face[2][1] = temp_array[1][0]
		self.face[1][0] = temp_array[0][1]
		self.face[0][0] = temp_array[0][2]
		self.face[0][2] = temp_array[2][2]
		self.face[2][0] = temp_array[0][0]
		self.face[2][2] = temp_array[2][0]


	def rotate_right(self):
		temp_array = deepcopy(self.face)
		self.face[2][0] = temp_array[2][2]
		self.face[2][2] = temp_array[0][2]
		self.face[0][2] = temp_array[0][0]
		self.face[0][0] = temp_array[2][0]
		self.face[2][1] = temp_array[1][2]
		self.face[1][2] = temp_array[0][1]
		self.face[0][1] = temp_array[1][0]
		self.face[1][0] = temp_array[2][1]
