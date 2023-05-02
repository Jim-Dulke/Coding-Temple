#Square 1 questions - add input values
ri = int(input('What is the property rental income?'))
li = int(input('What is the property laundry income?'))
si = int(input('What is the property storage income?'))
misc_i = int(input('What is the total amount of other income?'))

sq_1= ri + li + si + misc_i

print(f'Square 1: ${sq_1}')


#Square 2 questions - add list values
i = 0

sq_2 = 0

expenses = ['taxes', 'insurance', 'water/sewer', 'garbage', 'electric',  'gas', 'HOA', 'Lawn/Snow', 'Vacancy', 'Repairs', 'CapEx', 'Property Management', 'Mortgage']

while i < len(expenses):

       i+= 1

       ask = int(input(f'How much is being paid for in {expenses[i-1]}?'))

       sq_2 += ask



print(f'Square 2: ${sq_2}')


#Square 3: Calculate annual cash flow by subtracting square 1 and square 2, then multiply by 12
sq_3 = (sq_1 - sq_2) * 12

print(f'Square 3: ${sq_3}')


#Square 4: Solve by storing in variables and using those variables as dictionary values
d = int(input('What is the down payment?'))

cc = int(input('How much are closing costs?'))

rehab = int(input('What is the rehab budget?'))

misc = int(input('List amount in USD of other income.'))



ti = {'Down payment': d, 'Closing costs': cc, 'Rehab costs' : rehab, 'Misc': misc}

total_inv = 0

for x in ti.values():
    total_inv += x

sq_4 = (sq_3 / total_inv) * 100
print (f'Square 4: {sq_4}%')