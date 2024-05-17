escolha = int(input("Escolha a opção:\n"))

match escolha:
    case 1:
        Num = input("Digite um numero: ")
        print("o numero informado foi:", Num)
    case 2:
        vl_hora = float(input("Digite salario: "))
        horas = float(input("Digite horas: "))
        print("Você ganha: ", vl_hora*horas)
    case 3:
        In_num = int(input("Digite um numero inteiro: "))
        In_num2 = int(input("DIgite o outro numeo inteiro: "))
        real = float(input("Digite um numero real: "))

        print("1º: ", (In_num*2)*(In_num2/2), "\n2º: ", (3*In_num)+real, "\n3º: ", real**2)
    case 4:
        altura = float(input("Altura: "))
        print("seu peso ideal é: ", (72.7*altura)-58)
    case 5:
        altura = float(input("Altura: "))
        print("seu peso ideal é: \ncaso Mulher:", (62.1*altura)-44.7, "\ncaso Homem: ", (72.7*altura)-58)
    case 6:
        valor = float(input("Quanto você ganha: "))
        horas = float(input("Horas trabalhadas: "))
        sálario = (valor*horas)
        imposto = (11/100)*sálario
        inss = sálario*(8/100)
        sindicato = sálario*(5/100)

        print("Você ganha: \na)sálario bruto: ", sálario, "\nb)INSS: ", sálario-inss, "\nc)sindicato", sálario-inss-sindicato, "\nd)líquido: ", sálario-inss-sindicato-imposto)
        
    case 7:
        valor = float(input("Digite valor: R$"))
        desconto = valor*0.15
        print(f"O valor do produto é R${valor+desconto:,.2f}")
    
    case 8:
        valor = 1030
        v_original = valor/(1+0.15)
        print(v_original)

    case 9:
        sJoao = 1200
        c1, c2 = 200, 120
        mc1, mc2 = c1+(c1*0.02), c2+(c2*0.02)
        pJoao = sJoao - (mc1+mc2)
        print(f"João terá apenas R${pJoao:,.2f} disponivel")

    case 10:
        broas, paes = 1.50, 0.12
        qbroas, qpaes = int(input("Quantas broas foram vendidas: ")), int(input("Quantos pães foram vendidos: "))
        valor = (qbroas*broas)+(qpaes*paes)
        poupanca = valor+(valor*0.1)
        print(f"Foi ganho R${valor:,.2f} com as vendas, e deve ser guardado R${poupanca:,.2f} na poupança")
    case 11:
        A, B, C = float(input("Digite a primeira nota: "))*2, float(input("Digite a segunda nota: "))*3, float(input("Digite a terceira nota: "))*5
        media = (A+B+C)/10
        print(f"A média do aulo é: {media:,.1f}")
    case 12:
        distancia, gasto = float(input("Digite qual foi a distancia em Km: ")),  float(input("Digite o gasto em Litros: "))
        consumo = distancia/gasto
        print(f"O consumo médio é de {consumo:,.1f}Km/l")
    case 13:
        tempo = float(input("Qual a tempo?: "))
        velocidade = float(input("Qual a velocidade do carro em Km/h: "))
        distancia = velocidade*tempo
        gasto = distancia/12

        print(f"A distancia é de {distancia:,.3f}km e será gasto {gasto:,.3f} litros")
    case 14:
        A, B = float(input("Digite o valor A: ")), float(input("Digite o valor B: "))
        operador = str(input("Qual o operador? (-, +, x, /)"))
        resultado = 0
        if operador=="-":
            resultado = A-B
        elif operador=="+":
            resultado = A+B
        elif operador=="x":
            resultado = A*B
        elif operador=="/":
            resultado = A/B
        else:
            print("Erro")
        print(f"O valor é: {resultado}")

    case 15:
        valor = float(input("Digite qual valor: "))
        if 0<= valor <=25:
            print("está no intervalo de [0, 25]")
        elif 25< valor <=50:
            print("está no intervalo de [26, 50]")
        elif 50< valor <= 75:
            print("está no intervalo de [51, 75]")
        elif 75< valor <= 100:
            print("está no intervalo de [76, 100]")
        else:
            print("Valor errado")

    case 16:
        nota1 = float(input("Digite a nota 1: "))
        nota2 = float(input("Digite a nota 2: "))
        valor = (nota1+nota2)/2

        if 0<= valor <=4:
            print("E")
        elif 4< valor <=6:
            print("D")
        elif 6< valor <= 7.5:
            print("C")
        elif 7.5< valor <= 9:
            print("B")
        elif 9< valor <= 10:
            print("A")
        else:
            print("Valor errado")
    case 17:
        a, b, c = int(input("da: ")), int(input("da: ")), int(input("da: "))
        if a>=(b+c):
            print("N tri")
        elif a**2 == (b**2 + c**2):
            print("Retangulo")
        elif a**2>(b**2+c**2):
            print("Obtusangulo")
        elif a**2<(b**2+c**2):
            print("Actuangulo")
        elif a==b==c:
            print("Equilatero")
        elif a==b!=c or a==c!=b or c==b!=a:
            print("Isoceles")
    case 18:
        import math
        a, b, c = int(input("da: ")), int(input("da: ")), int(input("da: "))
        if b>0 and a!=0:
            delta = math.sqrt(b**2 - (4*a*c))
            x1 = ((b*-1) + delta)/2*a
            x2 = ((b*-1) - delta)/2*a
            print("as raizes são: ", x1, x2)
        else:
            print("n tem raiz")
    case 19:
        x=-1
        if x <=0:
            for x in range(0, 101):
                print(x)
                x+=1
                if x>=100:
                    for x in range(0, 101):
                        x-=1
                        print(x)
    case 20:
        x=0
        for x in range(0, 25, +3):
            print(x)
    case 21:
        x = 0
        lis = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        for x in range(0, 5):
            if lis[x]%2==0:
                print(lis[x], "eh par")
            else:
                print(lis[x], "eh impar")
    case 22:
        x1 = 0
        for x in range(0, 6):
            x1 += x
            print(x1)
    case 23:
        x1 = 0
        lis = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        for i in range(0, 5):
            x1 += lis[i]
        print(x1)
    case 24:
        lis = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        par = 0
        impar = 1
        x = 0
        for x in range(0, 5):
            if lis[x]%2==0:
                par += lis[x]
            else:
                impar *= lis[x]
        print(f"a soma dos pares é: {par} e o produto dos impáres é: {impar}")
    case 25:
        lis = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        positivo = 0
        negativo = 0
        x = 0
        for x in range(0, 5):
            if lis[x]>=0:
                positivo += 1
                print(f"são {positivo} numeros positovos")
            elif lis[x]<0:
                negativo += 1
                print(f"são {negativo} numeros negativos")
            else:
                print("Erro")
    case 26:
        x = 1
        for x in range(0, 1000, 7):
            print(x)
    case 27:
        lis_idade = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        lis_tamanho = [float(input("tamanho: ")), float(input("tamanho: ")), float(input("tamanho: ")), float(input("tamanho: ")), float(input("tamanho: "))]
        a, b = 0, 0
        idade, tamanho = 0, 0
        for x in range(0, 5):
            if lis_tamanho[x]< 1.70:
                a +=1
                idade+= lis_idade[x]
            elif lis_idade[x]> 20:
                b+= 1
                tamanho += lis_tamanho[x]
        print(f"Idade média é {idade//a} e tamanho médio é {tamanho//b}")
    case 28:
        num = int(input("numero: "))
        for x in range(1000):
            if x%num==2:
                print(x)
    case 29:
        lis = [int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: ")), int(input("numero: "))]
        a, num = 0, 0
        for x in range(6):
            if lis[x]%3==0:
                print(lis[x])
                num += lis[x]
                a +=1
        print(f"a média é: {num/a:,.1f}")
    case 30:
        import math
        num = int(input("Numero: "))
        a, quadrado = 0, 0
        for x in range(0, num):
            if x%2==0:
                quadrado = x**2
                print(quadrado)
    case 31:
        valor = int(input("valor: "))
        while valor!=1:
            if valor%2==0:
                valor/=2
            else:
                valor= (valor*3)+1
            print(valor)
    case 32:
        ze, chico, ano = 1.30, 1.50, 1
        while chico>ze:
            ze+=0.03
            chico+=0.02
            ano+=1
        print(ano)
    case 33:
        var = str(input("Digite seu nome: "))
        print(len(var))
    case 34:
        var = str(input("Digite um nome: "))
        cont = str(input("Digite um caracter: "))
        if cont in var:
            print("Caracter no nome")
        else:
            print("djiasdj")
    case 35:
        var = str(input("Digite: "))
        a = var.count('a' or 'e' or 'i' or 'o' or 'u')
        print(a)
    case 36:
        rept = int(input("Digite quantas vezes gostária de dividir H: "))
        h, n, = 1, 1
        while n <= rept:
            h += 1/n
            n+=1
        print(n)
    case 37:
        n, m = 1, 1
        s = 0
        repr = int(input("Digite o valor N: "))
        while n <= repr:
            s += n/m
            n+=1
            m+=2
        print(s)
    case 38:
        esco = -1
        joao, maria, josé, branco, nulo = 0, 0, 0, 0, 0
        while esco !=0:
            esco = int(input("Escolha: "))
            if esco == 1:
                joao += 1
            elif esco == 2:
                maria += 1
            elif esco == 3:
                josé += 1
            elif esco == 4:
                branco += 1
            elif esco == 5:
                nulo += 1
            else:
                print("Erro")
        print(f"João: {joao}, Maria: {maria}, José: {josé}, Branco: {branco}, Nulo: {nulo}")
    case 39:
        m, n = int(input("Digite valor: ")), int(input("Digite valor: "))
        y = 0
        if m > n:
            x = m
            m = n
            n = x
        while (m or n)>= 0 and m<=n:
            print(m)
            y += m
            m += 1
        print(y)
    case 40:
        esc = int(input("Escola `1` para A e `2` para B: "))
        if esc == 1:
            a = '0'
            for x in range(0, 6):
                print(a)
                a += '0'
        if esc == 2:
            b = ''
            for x in range(1, 6):
                b += str(x)
                print(b)