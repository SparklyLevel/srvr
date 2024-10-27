from Models import Car, Boat, Transport

if __name__ == '__main__':
    print('PyCharm')

tyronk = Car( 20, 'русы', 'ivi','кргу')
print(tyronk)
emmyynm = Boat(21, 'edf', 'фуксия' , 'кдврт')
spisok = [tyronk, emmyynm]
print(spisok)
for e in spisok:
    print(e)
