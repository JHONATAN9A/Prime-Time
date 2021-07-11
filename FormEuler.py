def num_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True
                

def  formula_euler(inicio,final):
    Lista_primos= []
    for numero in range (inicio,final):
        formula = (numero**2) + numero + 41
        if num_primo(formula) == True:
            Lista_primos.append(formula)
    cantidad_primos = len(Lista_primos)
    return cantidad_primos


while True:
    try:
        entrada = input()
        conversion = entrada.split()
        inicio = int(conversion[0])
        final = int(conversion[1]) + 1
        resultado = formula_euler(inicio,final)
        porcentaje = (resultado * 100)/(final-inicio)
        print("{:.2f}".format(porcentaje))

    except:
        break

