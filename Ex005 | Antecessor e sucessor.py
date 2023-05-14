# Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e seu sucessor

numero_1 = int(input('Digite um valor: '))
sucessor = numero_1 + 1
antecessor = numero_1 - 1
print('O número {} tem como seu sucessor o número: {} e o seu antecessor como o número: {}'.format(numero_1, sucessor, antecessor))
