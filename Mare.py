# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 18:50:23 2023

@author: thiag
"""
import math
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Coeficientes harmônicos
harmônicos = {
    'MM': {'A': 0.020, 'ω': 345.68},
    'MSF': {'A': 0.017, 'ω': 136.35},
    '2Q1': {'A': 0.041, 'ω': 61.84},
    'Q1': {'A': 0.110, 'ω': 53.11},
    'O1': {'A': 0.009, 'ω': 72.15},
    'M1': {'A': 0.051, 'ω': 131.01},
    'K1': {'A': 0.003, 'ω': 117.95},
    'J1': {'A': 0.002, 'ω': 213.37},
    'OO1': {'A': 0.002, 'ω': 298.25},
    'KQ1': {'A': 0.043, 'ω': 129.61},
    'MNS2': {'A': 0.172, 'ω': 50.46},
    'MU2': {'A': 0.162, 'ω': 57.06},
    'N2': {'A': 0.005, 'ω': 149.76},
    'M2': {'A': 0.004, 'ω': 61.48},
    'L2': {'A': 0.018, 'ω': 338.10},
    'S2': {'A': 0.007, 'ω': 42.95},
    'KJ2': {'A': 0.021, 'ω': 48.73},
    'MO3': {'A': 0.028, 'ω': 3.62},
    'M3': {'A': 0.016, 'ω': 163.55},
    'MK3': {'A': 0.002, 'ω': 19.63},
    'MN4': {'A': 0.002, 'ω': 350.01},
    'M4': {'A': 0.001, 'ω': 24.07},
    'SN4': {'A': 0.007, 'ω': 14.41},
    'MS4': {'A': 0.004, 'ω': 107.24},
    'S4': {'A': 0.004, 'ω': 73.95},
    '2MN6': {'A': 0.020, 'ω': 236.54},
    'M6': {'A': 0.017, 'ω': 176.70},
    '2MS6': {'A': 0.041, 'ω': 148.23},
    '2SM6': {'A': 0.110, 'ω': 88.30},
    'M8': {'A': 0.009, 'ω': 355.97},
}

def calcular_altura_mare(harmônicos, data_hora):
    altura_média = 0.0
    for componente, coeficientes in harmônicos.items():
        A = coeficientes['A']
        ω = coeficientes['ω']

        # Converter a data e hora para minutos do dia (0 a 1440 minutos)
        minutos_do_dia = data_hora.hour * 60 + data_hora.minute

        altura = A * math.cos(math.radians(ω * minutos_do_dia / 60))
        altura_média += altura

    return altura_média

def calcular_mare_no_dia(harmônicos, dia):
    alturas_mare_dia = []
    data_inicial = datetime.strptime(dia, '%Y-%m-%d')
    for minutos in range(24*60):
        tempo_atual = data_inicial + timedelta(minutes=minutos)
        altura = calcular_altura_mare(harmônicos, tempo_atual)
        alturas_mare_dia.append((tempo_atual, altura))
    return alturas_mare_dia

def plot_mare_no_dia(harmônicos, dia):
    alturas_mare_dia = calcular_mare_no_dia(harmônicos, dia)
    tempos, alturas = zip(*alturas_mare_dia)

    plt.plot(tempos, alturas)
    plt.xlabel('Tempo')
    plt.ylabel('Altura da Maré (metros)')
    plt.title(f'Maré no dia {dia}')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

# Dia específico para calcular e plotar a maré (no formato "ano-mês-dia")
dia_especifico = "2023-08-30"
# Chame a função para plotar o gráfico da maré no dia específico
plot_mare_no_dia(harmônicos, dia_especifico)