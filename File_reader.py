f = "og_data.csv"

f.partition(".")
print(f)

filename, seperator, extension = f.partition(".")
print("The full-file name is: " + f)
print("The extension of this file is: " + extension)
 

with open("og_data.csv", "r") as f:
	pass

	size_to_read = 250

	f_contents = f.read(size_to_read)	
	print("This is the header data: ")		# HEADER TEXT
	print(f_contents, end="")


	# f.seek(0)									# LOOP BACK TO BEGINNING

	# f_contents = f.read(size_to_read)
	# print(f_contents, end="")

	# print(f.tell())							# GETS POSITION



	# while len(f_contents) > 0:
	# 	print(f_contents, end="")
	# 	f_contents =f.read(size_to_read)			
	

	# for line in f:
	# 	print(line, end="")				# READS ALL 1 BY 1 #

	# f_contents = f.readlines()
	# print(f_contents, end="")

	# f_contents = f.readline()
	# print(f_contents, end ="")