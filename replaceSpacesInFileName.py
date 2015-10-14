import os  
file  = os.listdir('.')
for filename in file:
	extension = os.path.splitext(filename)[1]
	if not extension == '.py': 
		newfilename = filename.replace('_',' ')
		print('Renaming file: '+ filename+' to filename: '+ newfilename)
		os.rename(filename,newfilename); 
