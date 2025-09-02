import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import pandas as pd

user = "postgres"
password = "capoeira"
host = "localhost"
port = 5432
database = "funcionarios"

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@localhost:{port}/{database}')

def criar_graficos(df):
    plt.figure(figsize=(14, 10))

    plt.subplot(2,3,1)
    df.sort_values('idade').groupby('idade')['salario'].mean().plot()
    plt.title("Salário Médio por Idade")

    plt.subplot(2,3,2)
    plt.hist(df['idade'], bins=10, edgecolor='black')
    plt.title("Distribuição das Idades")

    plt.subplot(2,3,3)
    plt.boxplot(df['salario'])
    plt.title("Boxplot dos Salários")

    plt.subplot(2,3,4)
    idade_salario = df.groupby('idade')['salario'].mean()
    plt.fill_between(idade_salario.index, idade_salario.values, alpha=0.3)
    plt.plot(idade_salario.index, idade_salario.values, marker='o')
    plt.title("Área - Salário Médio por Idade")

    plt.subplot(2,3,5)
    df['departamento'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Proporção por Departamento")
    plt.ylabel("")

    plt.subplot(2,3,6)
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Calor das Correlações")
    plt.show()


# 3. Carrega a tabela em DataFrame
df = pd.read_sql_query("SELECT * FROM funcionarios;", engine)

criar_graficos(df)

