
class History:
	def __init__(self, dept, type, time, user, message):
		self.dept = dept
		self.type = type
		self.time = time
		self.user = user
		self.message = message
	def prettyPrint(self, level):
		indent = "".join(["\t"]*level)
		print(indent + "{")
		print(indent + "\tDEPT: " + self.dept)
		print(indent + "\tTYPE: " + self.type)
		print(indent + "\tTIME: " + str(self.time))
		print(indent + "\tUSER: " + self.user)
		print(indent + "\tMESSAGE: " + self.message )
		print(indent + "}")
