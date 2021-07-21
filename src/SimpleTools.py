#Simpletools 0.0.2

def ping():
	print("ping")
	return True

# Create file
def file_create(file):
	try:
		f = open(file, "r")
		f.close()
	except:
		f = open(file, "w")
		f.close()

# works with data in one line from the file
class OneLine:
	def __init__(self, file="", separation="", file_create=None):
		# create default variables
		self.file = file
		self.separation = separation
		if file_create == True:	# test if file_create is set
			try:
				tempfile = open(self.file, "r")
				self.data = tempfile.readline().split(self.separation)
				tempfile.close()
			except:
				tempfile = open(self.file, "a+")
				tempfile.close()
				self.data = []
		else:
				tempfile = open(self.file, "r")
				self.data = tempfile.readline().split(self.separation)
				tempfile.close()
		#print(self.data)

		#adds the element to the file and data
	def addElement(self, element):
		self.data.append(element)
		tempcontent = ""
		for content in self.data:
			tempcontent += (content + self.separation)
		tempfile = open(self.file, "w")
		tempfile.write(tempcontent[:-len(self.separation)])
		tempfile.close()
		#print(self.data)

		#removes the element to the file and data
	def removeElement(self, element):
		self.data.remove(element)
		tempcontent = ""
		for content in self.data:
			tempcontent += (content + self.separation)
		tempfile = open(self.file, "w")
		tempfile.write(tempcontent[:-len(self.separation)])
		tempfile.close()
		#print(self.data)

		#gives all information about the data
	def info(self):
		#print(
		#	f"file: {self.file},",
		#	f"seperation: {self.separation},",
		#	f"data: {self.data}"
		#	)
		return (
			f"file: {self.file}",
			f"seperation: {self.separation}",
			f"data: {self.data}"
			)

