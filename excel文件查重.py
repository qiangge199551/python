import os
import pandas as pd

def main(dirname):
	for root, dirs, files in os.walk(dirname):
		# print(root)
		# print(dirs)
		# print(files)
		# for dir in dirs:
		#     print(os.path.join(root, dir))
		for file in files:
			print(os.path.join(root, file))
			data = pd.read_excel(file)
			data.loc['']
			print('-------------------------------------------')
 
 
if __name__ == '__main__':
	main(r'./')