from quadrado import Quadrado

def calculos_quadrado():

    print("Cálculo interativo de área e perímetro de quadrado")

    medida = float(input("Digite a medida de um dos lados do quadrado:\n"))

    quadrado = Quadrado(medida)
    area = quadrado.area()
    perimetro = quadrado.perimetro()

    print(f"A área do quadrado é igual a {area:.2f}, enquanto o perímetro é {perimetro:.2f}.")


calculos_quadrado()