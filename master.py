# ANÁLISE DE DADOS - CÓDIGO CORRIGIDO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========== SEÇÃO 1: DATASET CORRIGIDO ==========
def criar_dataset():
    dados = {
        'id': range(1, 11),
        'nome': ['Ana Silva', 'Carlos Oliveira', 'Maria Santos', 'João Pereira', 'Pedro Costa',
                'Laura Mendes', 'Paulo Rodrigues', 'Juliana Almeida', 'Fernando Lima', 'Camila Souza'],
        'departamento': np.random.choice(['Vendas', 'TI', 'RH'], 10),
        'salario': np.random.randint(3000, 8000, 10),
        'idade': np.random.randint(25, 50, 10)
    }
    
    df = pd.DataFrame(dados)
    return df

df = criar_dataset()
print("Primeiras linhas:")
print(df.head())

# ========== SEÇÃO 2: ANÁLISE CORRIGIDA ==========
def analisar_dados(df):
    print("\n=== ANÁLISE ===")
    print(f"Total de funcionários: {len(df)}")
    print(f"Média salarial: R$ {df['salario'].mean():.2f}")
    print(f"Maior salário: R$ {df['salario'].max()}")
    
    # Contagem por departamento (CORRIGIDO)
    contagem = df.groupby('departamento')['nome'].count()
    print("\nFuncionários por departamento:")
    print(contagem)

analisar_dados(df)

# ========== SEÇÃO 3: VISUALIZAÇÃO CORRIGIDA ==========
def criar_graficos(df):
    plt.figure(figsize=(12, 4))
    
    # Gráfico de barras (CORRIGIDO)
    plt.subplot(1, 2, 1)
    df['departamento'].value_counts().plot.bar()
    plt.title('Funcionários por Departamento')
    plt.ylabel('Quantidade')
    
    # Gráfico de dispersão (CORRIGIDO)
    plt.subplot(1, 2, 2)
    plt.scatter(df['idade'], df['salario'])
    plt.xlabel('Idade')
    plt.ylabel('Salário')
    plt.title('Idade vs Salário')
    
    plt.tight_layout()
    plt.show()

criar_graficos(df)

# ========== SEÇÃO 4: SISTEMA CORRIGIDO ==========
class SistemaFuncionarios:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)
    
    def aumentar_salarios(self, departamento, percentual):
        # CORRIGIDO: Filtro correto
        mask = self.df['departamento'] == departamento
        self.df.loc[mask, 'salario'] = self.df.loc[mask, 'salario'] * (1 + percentual / 100)
        print(f"Salários de {departamento} aumentados em {percentual}%")
        print(f"Novos salários: {self.df.loc[mask, ['nome', 'salario']].to_string(index=False)}")
    
    def buscar_por_idade(self, idade_min, idade_max):
        # CORRIGIDO: Condição lógica correta
        resultado = self.df[(self.df['idade'] >= idade_min) & (self.df['idade'] <= idade_max)]
        return resultado

# Testando o sistema (CORRIGIDO)
print("\n" + "="*50)
sistema = SistemaFuncionarios(df)
sistema.aumentar_salarios('TI', 10)

print("\n" + "="*50)
funcionarios_jovens = sistema.buscar_por_idade(25, 35)
print("Funcionários entre 25-35 anos:")
if not funcionarios_jovens.empty:
    print(funcionarios_jovens[['nome', 'idade', 'departamento']].to_string(index=False))
else:
    print("Nenhum funcionário encontrado nessa faixa etária.")

# ========== BÔNUS: ANÁLISE ADICIONAL ==========
print("\n" + "="*50)
print("ANÁLISE COMPLETA:")
print(f"Média de idade por departamento:")
idade_por_depto = df.groupby('departamento')['idade'].mean()
print(idade_por_depto.round(1))

print(f"\nMédia salarial por departamento:")
salario_por_depto = df.groupby('departamento')['salario'].mean()
print(salario_por_depto.round(2))