# ANÁLISE DE DADOS - CÓDIGO COM ERROS PARA CORREÇÃO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========== SEÇÃO 1: DATASET COM ERROS ==========
def criar_dataset():
    dados = {
        'id': range(1, 11),
        'nome': ['Ana Silva', 'Carlos Oliveira', 'Maria Santos', 'João Pereira', 'Pedro Costa'],
        'departamento': np.random.choice(['Vendas', 'TI', 'RH'], 10),
        'salario': np.random.randint(3000, 8000, 10),
        'idade': np.random.randint(25, 50, 10)
    }
    
    df = pd.DataFrame(dados)
    return df

df = criar_dataset()
print("Primeiras linhas:")
print(df.head()

# ========== SEÇÃO 2: ANÁLISE COM ERROS ==========
def analisar_dados(df):
    print("\n=== ANÁLISE ===")
    print(f"Total de funcionários: {len(df)}")
    print(f"Média salarial: R$ {df['salario'].mean()}")
    print(f"Maior salário: R$ {df['salario'].max()}")
    
    # Contagem por departamento (ERRO)
    contagem = df.groupby('departamento').count()
    print("\nFuncionários por departamento:")
    print(contagem['nome'])

analisar_dados(df)

# ========== SEÇÃO 3: VISUALIZAÇÃO COM ERROS ==========
def criar_graficos(df):
    plt.figure(figsize=(12, 4))
    
    # Gráfico de barras (ERRO)
    plt.subplot(1, 2, 1)
    df['departamento'].value_counts().plot.bar()
    plt.title('Funcionários por Departamento')
    
    # Gráfico de dispersão (ERRO)
    plt.subplot(1, 2, 2)
    plt.scatter(df['idade'], df['salario'])
    plt.xlabel('Idade')
    plt.ylabel('Salário')
    plt.title('Idade vs Salário')
    
    plt.tight_layout()
    plt.show()

criar_graficos(df)

# ========== SEÇÃO 4: SISTEMA COM ERROS ==========
class SistemaFuncionarios:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)
    
    def aumentar_salarios(self, departamento, percentual):
        # ERRO: Filtro incorreto
        mask = self.df['departamento'] = departamento
        self.df.loc[mask, 'salario'] *= (1 + percentual / 100)
        print(f"Salários de {departamento} aumentados em {percentual}%")
    
    def buscar_por_idade(self, idade_min, idade_max):
        # ERRO: Condição lógica incorreta
        resultado = self.df[(self.df['idade'] > idade_min) and (self.df['idade'] < idade_max)]
        return resultado

# Testando o sistema (ERROS)
sistema = SistemaFuncionarios(df)
sistema.aumentar_salarios('TI', 10)

funcionarios_jovens = sistema.buscar_por_idade(25, 35)
print("\nFuncionários entre 25-35 anos:")
print(funcionarios_jovens[['nome', 'idade']])