# This is my personel project for Password Generator.
# It is based on my lessons from Python.

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Sam Criador de Senhas! (Welcome to the Sam Password Generator!)\n"
      "\n")
nr_letters = int(input("Qual a quantidade de lestras que você quer na sua senha?"
                       "(na sua senha? How many letters would you like in your password?)\n"
                       "\n"))
nr_symbols = int(input(f"Quantos simbolos você quer na sua senha? (How many symbols would you like?)\n"
                       f"\n"))
nr_numbers = int(input(f"Quantos números você quer na sua senha? (How many numbers would you like?)\n"
                       f"\n"))

if nr_symbols > len(symbols) or nr_numbers > len(numbers) or nr_letters > len(letters):
    print("Essa quantidade não é valida! (Your option is not valid, try again!)")
    exit()
elif nr_symbols > 5 or nr_numbers > 5 or nr_letters > 25:
    print("Tente novamente! Suas opções não são validas! (Your option is not valid, try again!)")
    exit()



# Creating the letters selection
letters_pool = []

for x in range(1, nr_letters + 1):
    l = random.randint(0, len(letters) -1)
    letters_pool.append(letters[l])
    letters.pop(l)

# creating the symbols selections
symbols_pool = []

for y in range(1, nr_symbols + 1):
    m = random.randint(0, len(symbols) -1)
    symbols_pool.append(symbols[m])
    symbols.pop(m)

# creating the numbers selections
numbers_pool = []

for w in range(1, nr_numbers + 1):
    p = random.randint(0, len(numbers) -1)
    numbers_pool.append(numbers[p])
    numbers.pop(p)

all_together = letters_pool + symbols_pool + numbers_pool
random.shuffle(all_together)

print(f'Aqui esta sua senha (Here is your password): {"".join(all_together)}')


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P