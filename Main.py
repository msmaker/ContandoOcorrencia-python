def caracter(string,c):
    valor = 0
    for num in string:
      if(num == c):
        valor += 1
    return valor

string = input()
c = input()

valor = caracter(string,c)
if valor == 0:
    print("Caractere nao encontrado.")
else:
    print("O caractere buscado ocorre", valor, "vezes na sequencia.")




