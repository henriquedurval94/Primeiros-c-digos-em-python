"""
📌 Projeto: Calculadora de Ângulos
📖 Descrição: Programa que calcula seno, cosseno e tangente de um ângulo informado pelo usuário.
👨‍💻 Autor: Henrique Durval
"""

import math


def calcular_trigonometria(angulo_graus: float) -> dict:
    """
    Converte o ângulo para radianos e calcula seno, cosseno e tangente.

    :param angulo_graus: Ângulo em graus
    :return: Dicionário com seno, cosseno e tangente
    """
    radianos = math.radians(angulo_graus)

    return {
        "seno": math.sin(radianos),
        "cosseno": math.cos(radianos),
        "tangente": math.tan(radianos),
    }


def exibir_resultados(angulo: float, resultados: dict) -> None:
    """
    Exibe os resultados formatados no terminal.

    :param angulo: Ângulo informado
    :param resultados: Dicionário com valores trigonométricos
    """
    print(f"\n📐 Resultados para o ângulo {angulo}°:\n")
    print(f"Seno: {resultados['seno']:.2f}")
    print(f"Cosseno: {resultados['cosseno']:.2f}")
    print(f"Tangente: {resultados['tangente']:.2f}")


def main():
    """
    Função principal do programa.
    """
    try:
        angulo = float(input("Digite o ângulo em graus: "))
        resultados = calcular_trigonometria(angulo)
        exibir_resultados(angulo, resultados)
    except ValueError:
        print("❌ Erro: Por favor, digite um número válido.")


if __name__ == "__main__":
    main()

