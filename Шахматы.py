k = int(input('Введите номер первого поля(1-8): '))
l = input('Введите букву первого поля(большими буквами A-H): ')

m = int(input('Введите номер второго поля(1-8): '))
n = input('Введите букву второго поля(большими буквами A-H): ')

figura = input('Какая фигура на первом поле(ферзь, ладья, слон или конь)? ')

#1
kletka1 = ''
kletka2 = ''
if k%2 == 0 and (l=='A' or l=='C' or l=='E' or l=='G'):
    kletka1 = 'Клетка черная'
else:
    kletka1 = 'Клетка белая'

if m%2 == 0 and (n=='A' or n=='C' or n=='E' or n=='G'):
    kletka2 = 'Клетка черная'
else:
    kletka2 = 'Клетка белая'

if kletka1 == kletka2:
    print('1. Поля одного цвета')
else:
    print('1. Поля разных цветов')
    
#2-3
LM = ['A','B','C','D','E','F','G','H']
L = LM.index(l)
N = LM.index(n)
if figura == 'ладья':
        if (k==m) or (l==n):
            print('2. Ладья угрожает второму полю, можно попасть одним ходом')
        else:
            print('2. Ладья не угрожает второму полю, нельзя попасть одним ходом')
            while (k!=m) or (l!=n):
                if k > m:
                    k -= 1
                else: 
                    k += 1
                if k == m:
                    break
            print('3.'+l+str(k))
            
if figura == 'слон':
        if abs(k - m) == abs(L - N): 
            print('2. Слон угрожает второму полю, можно попасть одним ходом')
        else:
            print('2. Слон не угрожает второму полю, нельзя попасть одним ходом')
            if kletka1 == kletka2:
                if m > k or k == m:
                    while abs(k - m) != abs(L - N): 
                        k += 1
                        L += 1
                        if abs(k - m) == abs(L - N):
                            break
                elif k > m or l == n:
                    while abs(k - m) != abs(L - N): 
                        k -= 1
                        L -= 1
                        if abs(k - m) == abs(L - N):
                            break
                print('3.'+LM[L]+str(k))
            else:
                print('3. Никак')

if figura == 'ферзь':
        if abs(k - m) == abs(L - N) or (k==m) or (l==n):
            print('2. Ферзь угрожает второму полю, можно попасть одним ходом')
        else:
            print('2. Ферзь не угрожает второму полю, нельзя попасть одним ходом')
            
 
if figura == 'конь':
        if (abs(k - m)==1 and (abs(L) - (abs(N)==2))) or (abs(k - m)==2 and (abs(L) - (abs(N)==1))):
            print('2. Конь угрожает второму полю, можно попасть одним ходом')
        else:
            print('2. Конь не угрожает второму полю, нельзя попасть одним ходом')
        


