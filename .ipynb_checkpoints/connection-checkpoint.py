import pandas as pd
from sqlalchemy import create_engine
from IPython.display import display_html

user = "postgres"
password = "capoeira"
host = "localhost"
port = 5432
database = "analise_de_dados"


engine = create_engine(f'postgresql+psycopg2://{user}:{password}@localhost:{port}/{database}')

df_projetos = pd.read_sql("SELECT * FROM Projetos;", engine)
df_tarefas = pd.read_sql("SELECT * FROM Tarefas;", engine)
df_empregados = pd.read_sql("SELECT * FROM Empregados;", engine)
df_logs = pd.read_sql("SELECT * FROM Logs;", engine)
df_custos = pd.read_sql("SELECT * FROM Custos;", engine)
df_recursos = pd.read_sql("SELECT * FROM Recursos;", engine)
df_recursos_projetos = pd.read_sql("SELECT * FROM Recursos_projetos;", engine)

dfs = [df_projetos, df_tarefas, df_empregados, df_logs, df_custos, df_recursos, df_recursos_projetos]

display_html(pd.concat(dfs, axis=1).to_html(), raw=True)