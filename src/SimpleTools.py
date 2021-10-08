#Simpletools 0.0.2
import os
import shutil
import time

def ping():
	print("ping")
	return True

# Create file
def file_create(file):
	try:
		f = open(file, "r", encoding="utf-8")
		f.close()
	except:
		f = open(file, "w", encoding="utf-8")
		f.close()

# works with data in one line from the file
class OneLine:
	def __init__(self, file="", separation="", file_create=None):
		# create default variables
		self.file = file
		self.separation = separation
		if file_create == True:	# test if file_create is set
			try:
				tempfile = open(self.file, "r", encoding="utf-8")
				self.data = tempfile.readline().split(self.separation)
				tempfile.close()
			except:
				tempfile = open(self.file, "a+", encoding="utf-8")
				tempfile.close()
				self.data = []
		else:
				tempfile = open(self.file, "r", encoding="utf-8")
				self.data = tempfile.readline().split(self.separation)
				tempfile.close()
		#print(self.data)

		#adds the element to the file and data
	def addElement(self, element):
		self.data.append(element)
		tempcontent = ""
		for content in self.data:
			tempcontent += (content + self.separation)
		tempfile = open(self.file, "w", encoding="utf-8")
		tempfile.write(tempcontent[:-len(self.separation)])
		tempfile.close()
		#print(self.data)

		#removes the element to the file and data
	def removeElement(self, element):
		self.data.remove(element)
		tempcontent = ""
		for content in self.data:
			tempcontent += (content + self.separation)
		tempfile = open(self.file, "w", encoding="utf-8")
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

# Database
class Database:
    def __init__(self, path):
        self.path = path # save the path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
           
    def get_tables(self):
        return os.listdir(self.path)
        
    def create_table(self, table_name):
        os.mkdir(self.path + "/" + table_name)
        os.mkdir(self.path + "/" + table_name + "/column")
        
    def delete_table(self, table_name):
        #os.rmdir(self.path + "/" + table_name)
        shutil.rmtree(self.path + "/" + table_name)
        
    def get_table_structure(self, table_name):
        return os.listdir(self.path + "/" + table_name + "/column")
        
    def create_column(self, table_name, column_name):
        file = open(self.path + "/" + table_name + "/column/" + column_name, "w", encoding="utf-8")
        file.close()
        
    def delete_column(self, table_name, column_name):
        os.remove(self.path + "/" + table_name + "/column/" + column_name)
        
    def add_data(self, table_name, data):
        format = True
        table_path = self.path + "/" + table_name
        for each in data:
            if not each[0] in os.listdir(table_path + "/column"):
                format = False
        if format == True:
            data_path = table_path + "/" + str(len(os.listdir(table_path)))
            os.mkdir(data_path)
            for each in data:
                file = open(data_path + "/" + each[0], "w", encoding="utf-8")
                file.write(each[1])
                file.close()
        
    def delete_data(self, table_name, data_id):
        shutil.rmtree(self.path + "/" + table_name + "/" + str(data_id))
        data_file_list = os.listdir(self.path + "/" + table_name)
        data_file_list.sort()
        for index, data in enumerate(data_file_list):
            if data != "column" and data != str(index + 1):
                os.rename(self.path + "/" + table_name + "/" + data, self.path + "/" + table_name + "/" + str(index + 1))
                #shutil.move(self.path + "/" + table_name + "/" + data, self.path + "/" + table_name + "/" + str(index + 1))
    
    def get_data_byid(self, table_name, data_id):
        data_path = self.path + "/" + table_name + "/" + str(data_id)
        data = []
        for each in os.listdir(data_path):
            file = open(data_path + "/" + each, "r", encoding="utf-8")
            data.append((each, file.read()))
            file.close()
        return data

    def get_data_bydata(self, table_name, known_data): # known_data = [("column", "data"), ("column", "data")]
        format = True
        for data in known_data: # test if the column all existing
            if not data[0] in os.listdir(self.path + "/" + table_name + "/column"):
                format = False
        if format:
            return_data = []
            for file_path in os.listdir(self.path + "/" + table_name):
                if file_path != "column":
                    # get the data for checking
                    temp_data = []
                    for column_file in os.listdir(self.path + "/" + table_name + "/" + file_path):
                        file = open(self.path + "/" + table_name + "/" + file_path + "/" + column_file, encoding="utf-8")
                        temp_data.append((column_file, file.read()))
                        file.close()
                    # if known data in tempdata ...
                    if all(item in temp_data for item in known_data):
                        temp_data.append(("id", file_path))
                        return_data.append(temp_data)
            return return_data
            
    def get_data_all(self, table_name):
        retrun_data = []
        for data_dir in os.listdir(self.path + "/" + table_name):
            if data_dir != "column":
                data = []
                for data_file in os.listdir(self.path + "/" + table_name + "/" + data_dir):
                    file = open(self.path + "/" + table_name + "/" + data_dir + "/" + data_file, "r", encoding="utf-8")
                    data.append((data_file, file.read()))
                    file.close()
                data.append(("id", data_dir))
                retrun_data.append(data)
        
        return retrun_data
            
    def change_data_byid(self, table_name, data_id, changed_data):
        file = open(self.path + "/" + table_name + "/" + data_id + "/" + changed_data[0], "w", encoding="utf-8")
        file.write(changed_data[1])
        file.close()
            
