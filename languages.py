import openpyxl

data = openpyxl.open('binar.xlsx', read_only = True) #задаємо бінарні відношення множин через матрицю
sheet = data.active

p_r = set()
r_l = set()

for cell in range(1,5):
	for raw in range(2,6):
		cort = sheet[raw][cell].value
		cort = int(cort)
		if cort == 1:
			a = sheet[1][cell].value
			b = sheet[raw][0].value
			p_r.add(tuple([b, a]))					#створюємо множину людей та сфер

			
for cell in range(1,5):
	for raw in range(8,13):
		cort = sheet[raw][cell].value
		cort = int(cort)
		if cort == 1:
			a = sheet[7][cell].value
			b = sheet[raw][0].value
			r_l.add(tuple([a, b]))					#створюємо множину сфер та мов


s = set()
ios = set()
apps = set()
games = set()
web = set()

for i in list(p_r):					#створюємо нову множину за допомогою композиції двох інших
	a = list(i)
	for j in list(r_l):
		b = list(j)
		if a[1] == b[0]:
			s.add(tuple([a[0], a[1], b[1]]))


for i in list(s):					#сортуємо множину за властивостями єлементів
	l = list(i)
	if 'IOS' in l:
		ios.add(tuple(l))
	elif 'web' in l:
		web.add(tuple(l))
	elif "apps" in l:
		apps.add(tuple(l))
	elif 'games' in l:
		games.add(tuple(l))


print(f'games: ')
for i in list(games):
	print(i)
print()

print(f'ios: ')
for i in list(ios):
	print(i)    
print()

print(f'apps: ')
for i in list(apps):
	print(i)
print()

print(f'web: ')
for i in list(web):
	print(i)
print()
