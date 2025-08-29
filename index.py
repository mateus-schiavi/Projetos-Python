# Importações necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# Criando nosso dataset de funcionários
def criar_dataset():
    dados = {
        'id': range(1, 21),
        'nome': ['Ana Silva', 'Carlos Oliveira', 'Maria Santos', 'João Pereira', 'Pedro Costa', 
                'Laura Mendes', 'Paulo Rodrigues', 'Juliana Almeida', 'Fernando Lima', 'Camila Souza',
                'Ricardo Barbosa', 'Amanda Carvalho', 'Bruno Martins', 'Patrícia Rocha', 'Marcos Ferreira',
                'Luciana Dias', 'Eduardo Cardoso', 'Isabela Batista', 'Roberto Nunes', 'Tânia Moreira'],
        'departamento': np.random.choice(['Vendas', 'TI', 'RH', 'Marketing', 'Financeiro'], 20),
        'salario': np.random.randint(3000, 10000, 20),
        'idade': np.random.randint(22, 55, 20),
        'data_admissao': pd.date_range(start='2015-01-01', end='2023-12-31', periods=20),
        'avaliacao': np.random.uniform(3.0, 5.0, 20).round(1)
    }
    
    df = pd.DataFrame(dados)
    df['anos_empresa'] = ((datetime.now() - df['data_admissao']).dt.days / 365).round(1)
    return df

# Criar e visualizar o dataset
df_funcionarios = criar_dataset()
print("Primeiras 5 linhas do dataset:")
print(df_funcionarios.head())
print("\nInformações do dataset:")
print(df_funcionarios.info())

# Funções de análise
def analise_estatisticas(df):
    print("=== ESTATÍSTICAS GERAIS ===")
    print(f"Total de funcionários: {len(df)}")
    print(f"Média salarial: R$ {df['salario'].mean():.2f}")
    print(f"Salário máximo: R$ {df['salario'].max():.2f}")
    print(f"Salário mínimo: R$ {df['salario'].min():.2f}")
    print(f"Idade média: {df['idade'].mean():.1f} anos")
    print(f"Média de avaliação: {df['avaliacao'].mean():.1f}/5.0")
    
    print("\n=== DISTRIBUIÇÃO POR DEPARTAMENTO ===")
    dist_depto = df['departamento'].value_counts()
    for depto, count in dist_depto.items():
        print(f"{depto}: {count} funcionários ({count/len(df)*100:.1f}%)")

def analise_departamento(df, departamento):
    print(f"\n=== ANÁLISE DO DEPARTAMENTO {departamento.upper()} ===")
    depto_df = df[df['departamento'] == departamento]
    
    if depto_df.empty:
        print("Departamento não encontrado.")
        return
    
    print(f"Quantidade: {len(depto_df)} funcionários")
    print(f"Média salarial: R$ {depto_df['salario'].mean():.2f}")
    print(f"Funcionários:")
    for _, row in depto_df.iterrows():
        print(f"  - {row['nome']} (R$ {row['salario']:.2f}, {row['avaliacao']}/5.0)")

# Executando as análises
analise_estatisticas(df_funcionarios)
analise_departamento(df_funcionarios, 'TI')
analise_departamento(df_funcionarios, 'Vendas')

# Criando visualizações
def criar_visualizacoes(df):
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
    
    # Gráfico 1: Distribuição de salários
    ax1.hist(df['salario'], bins=10, edgecolor='black', alpha=0.7)
    ax1.set_title('Distribuição de Salários')
    ax1.set_xlabel('Salário (R$)')
    ax1.set_ylabel('Frequência')
    ax1.axvline(df['salario'].mean(), color='red', linestyle='dashed', linewidth=1, label=f'Média: R$ {df["salario"].mean():.2f}')
    ax1.legend()
    
    # Gráfico 2: Salário por departamento
    salario_por_depto = df.groupby('departamento')['salario'].mean().sort_values()
    ax2.barh(salario_por_depto.index, salario_por_depto.values)
    ax2.set_title('Média Salarial por Departamento')
    ax2.set_xlabel('Salário Médio (R$)')
    
    # Gráfico 3: Distribuição por departamento
    dist_depto = df['departamento'].value_counts()
    ax3.pie(dist_depto.values, labels=dist_depto.index, autopct='%1.1f%%', startangle=90)
    ax3.set_title('Distribuição de Funcionários por Departamento')
    
    # Gráfico 4: Relação idade vs salário
    ax4.scatter(df['idade'], df['salario'], alpha=0.6)
    ax4.set_title('Relação: Idade vs Salário')
    ax4.set_xlabel('Idade')
    ax4.set_ylabel('Salário (R$)')
    
    # Adicionando linha de tendência
    z = np.polyfit(df['idade'], df['salario'], 1)
    p = np.poly1d(z)
    ax4.plot(df['idade'], p(df['idade']), "r--", alpha=0.8)
    
    plt.tight_layout()
    plt.show()

# Executando as visualizações
criar_visualizacoes(df_funcionarios)

class SistemaGestaoFuncionarios:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)
        self.relatorios = []
    
    def adicionar_funcionario(self, nome, departamento, salario, idade, avaliacao):
        novo_id = self.df['id'].max() + 1
        novo_funcionario = {
            'id': novo_id,
            'nome': nome,
            'departamento': departamento,
            'salario': salario,
            'idade': idade,
            'data_admissao': datetime.now(),
            'avaliacao': avaliacao,
            'anos_empresa': 0
        }
        
        self.df = pd.concat([self.df, pd.DataFrame([novo_funcionario])], ignore_index=True)
        print(f"Funcionário {nome} adicionado com sucesso!")
    
    def aumentar_salario(self, departamento, percentual):
        mask = self.df['departamento'] == departamento
        self.df.loc[mask, 'salario'] = self.df.loc[mask, 'salario'] * (1 + percentual/100)
        print(f"Salários do departamento {departamento} aumentados em {percentual}%")
    
    def buscar_funcionario(self, nome=None, departamento=None, salario_min=None):
        resultado = self.df.copy()
        
        if nome:
            resultado = resultado[resultado['nome'].str.contains(nome, case=False)]
        if departamento:
            resultado = resultado[resultado['departamento'] == departamento]
        if salario_min:
            resultado = resultado[resultado['salario'] >= salario_min]
        
        return resultado
    
    def gerar_relatorio(self, tipo):
        if tipo == 'estatisticas':
            relatorio = {
                'total_funcionarios': len(self.df),
                'media_salarial': self.df['salario'].mean(),
                'media_idade': self.df['idade'].mean(),
                'media_avaliacao': self.df['avaliacao'].mean(),
                'departamentos': self.df['departamento'].value_counts().to_dict()
            }
        elif tipo == 'departamento':
            relatorio = {}
            for depto in self.df['departamento'].unique():
                depto_df = self.df[self.df['departamento'] == depto]
                relatorio[depto] = {
                    'quantidade': len(depto_df),
                    'media_salarial': depto_df['salario'].mean(),
                    'media_avaliacao': depto_df['avaliacao'].mean()
                }
        
        self.relatorios.append({'tipo': tipo, 'data': datetime.now(), 'dados': relatorio})
        return relatorio

# Usando o sistema
sistema = SistemaGestaoFuncionarios(df_funcionarios.to_dict('records'))

# Adicionando novo funcionário
sistema.adicionar_funcionario('Carlos Magno', 'TI', 8500, 32, 4.5)

# Aumentando salários
sistema.aumentar_salario('TI', 10)

# Buscando funcionários
funcionarios_ti = sistema.buscar_funcionario(departamento='TI')
print("\nFuncionários de TI:")
print(funcionarios_ti[['nome', 'salario', 'avaliacao']])

# Gerando relatório
relatorio = sistema.gerar_relatorio('estatisticas')
print("\nRelatório Estatístico:")
for chave, valor in relatorio.items():
    if chave != 'departamentos':
        print(f"{chave}: {valor}")