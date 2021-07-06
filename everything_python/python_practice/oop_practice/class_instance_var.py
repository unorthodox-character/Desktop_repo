class CSStudent:
	#defining class variable
	stream = 'cse'
	#constructor
	def __init__(self, roll):
		#instance variable
		self.roll = roll
a = CSStudent(12)
b = CSStudent(15)

print(a.stream)
print(a.roll)
print(CSStudent.stream)

