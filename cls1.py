class calc(object):
	def __init__(self):
		self.var1 = 0
		self.var2 = 0
	def setVar1(self, val):
		self.var1 = val
	def getVar1(self):
		return self.var1
	def setVar2(self, val):
		self.var2 = val
	def getVar2(self):
		return self.var2
	def add(self):
		return self.var1 + self.var2