import openpyxl
import math

variant = openpyxl.open('table_task_3.xlsx', read_only = True)
sheet = variant.worksheets[0]

variant = list()             			#lists for containing data         
variants_list = list()
answers = list()						#list with answers for teacher
t = True
n = 3

def make_variant(n):					#function for reading the data for each variant
	variant.clear()
	for cell in range(0, 7):
		personal_variant = sheet[n][cell].value
		variant.append(personal_variant)

		'''[0, 2011, 1, 2017, 2, 512, 65536, ]
		    ^	 ^   ^    ^   ^   ^     ^
		    V    Y1  M1   Y2  M2  V1    V2
		'''

def calculate_and_write_variant(variant):
	v = variant[0]
	y1 = variant[1]
	m1 = variant[2]
	y2 = variant[3]
	m2 = variant[4]
	v1 = variant[5]
	v2 = variant[6]
	
	t_ = (y2 - y1) * 12 + m2 - m1
	a = v2 / v1 #how many times increased
	T = 2 * t_ / a
	T = round(T, 2) #round to 2 numbers after points
	answers.append(T)

while t:
	make_variant(n)
	calculate_and_write_variant(variant)
	#space to function, which make txt file with task
	#space to function, which generate the answer and make txt file
	n = n + 1
	if n == 35:
		t = False

print(answers)

