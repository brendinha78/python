#exerc09
n1 =float(input("digite o primeiro numero"))
n2 =float(input("digite o segundo numero"))
op (input("digite a operação desejada( "soma(+) , divisao(/) , subtraçao(-) , multiplicaçao(*)"))
if op == "+":
    r = n1 + n2
elif op == "*":
    r = n1 * n2
elif op == "/":
    r = n1 / n2
 elif op == "-":
    r = n1 - n2
else:
    print("operador invalido")
print(" o resultado da operaçao",op,"e :",r)    