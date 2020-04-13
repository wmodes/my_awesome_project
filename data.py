# data.py - whatever this does
# authors: Wes Modes, Frank Piva, Kyle Dilbeck
# Date:
# License:

class Data():
	def __init__(self, name):
		self.name = name

	def return_name(self):
		"""returns a string name"""
		return f"Hello, {self.name}"