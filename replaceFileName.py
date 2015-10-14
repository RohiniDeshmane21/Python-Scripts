import os
  
  
file  = os.listdir('.')
i=1

for filename in file:
	extension = os.path.splitext(filename)[1]
	if not extension == '.py':  
		p=i
		newfilename = filename.replace(os.path.splitext(filename)[0],'Trial'+str(p))
		'''If you want to replace space by _ then pass 1st variable as " " and 2nd as "_"
			or vice versa
			here replace file name by fix name and increase counter E.g java1, java2, java3, java4 etc
		'''
		i=i+1;
		print('Renaming file: '+ filename+' to filename: '+ newfilename)
		os.rename(filename,newfilename);

