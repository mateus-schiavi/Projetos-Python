# ANÁLISE DE VENDAS - CÓDIGO COM ERROS PARA CORREÇÃO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ========== SEÇÃO 1: DATASET DE VENDAS COM ERROS ==========
def criar_dataset_vendas()
    dados = {
        'venda_id': range(1, 16),
        'produto': np.random.choice(['Notebook', 'Smartphone', 'Tablet', 'Monitor'], 15),
        'categoria': np.random.choice(['Eletrônicos', 'Informática', 'Acessórios'] 15),
        'quantidade': np.random.randint(1, 5, 15),
        'preco_unitario': np.random.randint(500, 2000, 15),
        'data_venda': pd.date_range(start='2024-01-01', end='2024-01-15', periods=15),
        'vendedor': np.random.choice(['Ana', 'Carlos', 'Maria', 'João'], 15)
    }
    
    df = pd.DataFrame(dados)
    df['valor_total'] = df['quantidade'] * df['preco_unitario']
    return df

df_vendas = criar_dataset_vendas()
print("Dataset de vendas:")
print(df_vendas.head(3)

# ========== SEÇÃO 2: ANÁLISE COM ERROS ==========
def analisar_vendas(df):
    print("\n=== ANÁLISE DE VENDAS ===")
    print(f"Total de vendas: {len(df)}")
    print(f"Valor total vendido: R$ {df['valor_total'].sum()}")
    print(f"Venda mais alta: R$ {df['valor_total'].max()}")
    
    # Análise por produto (ERRO)
    vendas_produto = df.groupby('produto')['valor_total'].sum
    print("\nVendas por produto:")
    print(vendas_produto)

# ========== SEÇÃO 3: CÁLCULOS COM ERROS ==========
def calcular_metricas(df):
    # Média móvel (ERRO)
    df['media_movel'] = df['valor_total'].rolling(window=3).mean
    
    # Top 3 produtos (ERRO)
    top_produtos = df['produto'].value_counts().head(3)
    print(f"\nTop 3 produtos mais vendidos: {top_produtos}")
    
    return df

# ========== SEÇÃO 4: VISUALIZAÇÃO COM ERROS ==========
def criar_graficos_vendas(df):
    plt.figure(figsize=(15, 5))
    
    # Gráfico 1: Vendas por dia (ERRO)
    plt.subplot(1, 3, 1)
    df.groupby('data_venda')['valor_total'].sum().plot.line()
    plt.title('Vendas por Dia')
    plt.xticks(rotation=45)
    
    # Gráfico 2: Vendas por produto (ERRO)
    plt.subplot(1, 3, 2)
    df['produto'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title('Distribuição por Produto')
    
    # Gráfico 3: Vendas por vendedor (ERRO)
    plt.subplot(1, 3, 3)
    df.groupby('vendedor')['valor_total'].sum().plot.barh()
    plt.title('Vendas por Vendedor')
    plt.xlabel('Valor Total (R$)')
    
    plt.tight_layout()
    plt.show()

# ========== SEÇÃO 5: SISTEMA COM ERROS ==========
class SistemaVendas:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)
    
    def adicionar_venda(self, produto, quantidade, preco, vendedor):
        novo_id = self.df['venda_id'].max + 1
        nova_venda = {
            'venda_id': novo_id,
            'produto': produto,
            'quantidade': quantidade,
            'preco_unitario': preco,
            'vendedor': vendedor,
            'data_venda': datetime.now(),
            'valor_total': quantidade * preco
        }
        
        self.df = self.df.append(nova_venda, ignore_index=True)
        print(f"Venda de {produto} adicionada com sucesso!")
    
    def filtrar_vendas(self, vendedor=None, produto=None, valor_minimo=None):
        resultado = self.df.copy()
        
        if vendedor:
            resultado = resultado[resultado['vendedor'] = vendedor]
        if produto:
            resultado = resultado[resultado['produto'] == produto]
        if valor_minimo:
            resultado = resultado[resultado['valor_total'] > valor_minimo]
        
        return resultado
    
    def relatorio_vendedor(self, vendedor):
        vendas_vendedor = self.df[self.df['vendedor'] == vendedor]
        
        if vendas_vendedor.empty():
            print(f"Vendedor {vendedor} não encontrado.")
            return
        
        total_vendas = vendas_vendedor['valor_total'].sum()
        media_venda = vendas_vendedor['valor_total'].mean()
        
        print(f"\n=== RELATÓRIO DO VENDEDOR {vendedor.upper()} ===")
        print(f"Total de vendas: R$ {total_vendas:.2f}")
        print(f"Média por venda: R$ {media_venda:.2f}")
        print(f"Quantidade de vendas: {len(vendas_vendedor)}")

# ========== EXECUÇÃO COM ERROS ==========
print("="*60)
analisar_vendas(df_vendas)

print("="*60)
df_vendas = calcular_metricas(df_vendas)
print("Dataset com métricas calculadas:")
print(df_vendas[['venda_id', 'valor_total', 'media_movel']].head())

print("="*60)
sistema_vendas = SistemaVendas(df_vendas)
sistema_vendas.adicionar_venda('Smartphone', 2, 1500, 'Ana')

vendas_ana = sistema_vendas.filtrar_vendas(vendedor='Ana')
print(f"\nVendas da Ana: {len(vendas_ana)}")

sistema_vendas.relatorio_vendedor('Ana')

criar_graficos_vendas(df_vendas)