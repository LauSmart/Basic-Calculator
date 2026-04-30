import math

HISTORICO = []
ULTIMO_RESULTADO = None

def mostrar_menu():
    print("\n" + "=" * 35)
    print("      CALCULADORA AVANÇADA")
    print("=" * 35)
    print("  1. Soma (+)")
    print("  2. Subtração (-)")
    print("  3. Multiplicação (*)")
    print("  4. Divisão (/)")
    print("  5. Potência (**)")
    print("  6. Raiz Quadrada (√)")
    print("  7. Módulo / Resto (%)")
    print("  8. Divisão Inteira (//)")
    print("  9. Fatorial (!)")
    print(" 10. Logaritmo Natural (ln)")
    print(" 11. Seno (sin)")
    print(" 12. Cosseno (cos)")
    print(" 13. Ver Histórico")
    print(" 14. Limpar Histórico")
    print("  0. Sair")
    print("=" * 35)

def obter_numero(prompt, permitir_ultimo=False):
    global ULTIMO_RESULTADO
    while True:
        entrada = input(prompt).strip().lower()
        if permitir_ultimo and entrada in ('r', 'ultimo', 'último') and ULTIMO_RESULTADO is not None:
            print(f"Usando último resultado: {ULTIMO_RESULTADO}")
            return ULTIMO_RESULTADO
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def obter_inteiro_positivo(prompt):
    while True:
        try:
            valor = int(input(prompt))
            if valor < 0:
                print("O valor deve ser não negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")

def adicionar_historico(operacao, resultado):
    HISTORICO.append(f"{operacao} = {resultado}")
    if len(HISTORICO) > 20:
        HISTORICO.pop(0)

def mostrar_historico():
    print("\n--- HISTÓRICO ---")
    if not HISTORICO:
        print("Nenhuma operação no histórico.")
    else:
        for item in HISTORICO:
            print(f"  {item}")
    print("-----------------\n")

def calcular():
    global ULTIMO_RESULTADO

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '0':
            print("Encerrando calculadora. Até logo!")
            break

        elif escolha == '13':
            mostrar_historico()
            continue

        elif escolha == '14':
            HISTORICO.clear()
            print("Histórico limpo com sucesso!")
            continue

        # Operações que precisam de dois números
        if escolha in ('1', '2', '3', '4', '5', '7', '8'):
            extra = " (digite 'r' para usar último resultado)" if ULTIMO_RESULTADO is not None else ""
            num1 = obter_numero(f"Digite o primeiro número{extra}: ", permitir_ultimo=True)
            num2 = obter_numero(f"Digite o segundo número{extra}: ", permitir_ultimo=True)

            if escolha == '1':
                resultado = num1 + num2
                operacao = f"{num1} + {num2}"
            elif escolha == '2':
                resultado = num1 - num2
                operacao = f"{num1} - {num2}"
            elif escolha == '3':
                resultado = num1 * num2
                operacao = f"{num1} * {num2}"
            elif escolha == '4':
                if num2 == 0:
                    print("Erro: Divisão por zero não permitida!")
                    continue
                resultado = num1 / num2
                operacao = f"{num1} / {num2}"
            elif escolha == '5':
                resultado = num1 ** num2
                operacao = f"{num1} ** {num2}"
            elif escolha == '7':
                resultado = num1 % num2
                operacao = f"{num1} % {num2}"
            elif escolha == '8':
                if num2 == 0:
                    print("Erro: Divisão inteira por zero não permitida!")
                    continue
                resultado = num1 // num2
                operacao = f"{num1} // {num2}"

            print(f"\n>>> Resultado: {operacao} = {resultado}")
            adicionar_historico(operacao, resultado)
            ULTIMO_RESULTADO = resultado

        # Operações com um único número
        elif escolha in ('6', '9', '10', '11', '12'):
            extra = " (digite 'r' para usar último resultado)" if ULTIMO_RESULTADO is not None else ""
            num = obter_numero(f"Digite o número{extra}: ", permitir_ultimo=True)

            if escolha == '6':
                if num < 0:
                    print("Erro: Não é possível calcular raiz quadrada de número negativo.")
                    continue
                resultado = math.sqrt(num)
                operacao = f"√{num}"
            elif escolha == '9':
                if not num.is_integer() or num < 0:
                    print("Erro: Fatorial só é definido para inteiros não negativos.")
                    continue
                resultado = math.factorial(int(num))
                operacao = f"{int(num)}!"
            elif escolha == '10':
                if num <= 0:
                    print("Erro: Logaritmo natural só é definido para números positivos.")
                    continue
                resultado = math.log(num)
                operacao = f"ln({num})"
            elif escolha == '11':
                resultado = math.sin(math.radians(num))
                operacao = f"sin({num}°)"
            elif escolha == '12':
                resultado = math.cos(math.radians(num))
                operacao = f"cos({num}°)"

            print(f"\n>>> Resultado: {operacao} = {resultado}")
            adicionar_historico(operacao, resultado)
            ULTIMO_RESULTADO = resultado

        else:
            print("Opção inválida! Por favor, escolha uma opção do menu.")

if __name__ == "__main__":
    calcular()

