'''
Составить генератор (yield), который переведет символы строки из верхнего
регистра в нижний.
'''
from string import ascii_lowercase

def translet(num):
    num_1 = list(num)
    yield [i for i in num if i in ascii_lowercase]
num = 'Я хочу пойти домой и хорошенько выспаться, а потом почитать книгу.'
num_2 = translet(num)
print(num_2) #крч, пока так оставлю. мозги не работают.
