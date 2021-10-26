from cheltuiala import Cheltuiala

'''
c1
*----------> <OBJ de tip Cheltuiala>
'''
def main():
    c1 = Cheltuiala(1, 100, 'exemplu de cheltuiala', '26-10-2021')
    c2 = Cheltuiala(2, 250, 'alt exemplu de cheltuiala', '26-10-2021')

    print(c1)
    c1.set_suma(500)
    print('c1 dupa set_suma:', c1)

    lst = [c1, c2, c2, Cheltuiala(5, 322, 'dsfsd', 'fdsfds')]
    for chelt in lst:
        print(chelt)

    # print(c1._Cheltuiala__suma)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
