import os
file  = os.listdir('.')
i=1
for filename in file:
	extension = os.path.splitext(filename)[1]
	if extension == '.pdf':
		p=i
		newfilename = filename.replace('_',' ')
		print(newfilename)
		with open("result.txt", "a") as myfile:
			myfile.write("\n"+ str(p) + ") "+os.path.splitext(newfilename)[0])
			i= i+1;
