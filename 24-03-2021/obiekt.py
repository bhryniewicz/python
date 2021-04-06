employee = {
 'imie':'Julia',
 'nazwisko':'Nowak',
 'miasto':'Poznań',
 'imionaDzieci':['Anna', 'Paweł', 'Dariusz']
}

print(employee)

print(type(employee))

print(employee['imionaDzieci'][1])

employee['number'] = '56632123'
employee['wiek'] = '45'

print(employee)

del employee['imionaDzieci']

print(dict.keys(employee))