import requests
import csv
import pandas as pd

# 1. Definir URL e Parâmetros

url = "https://apicadprev.trabalho.gov.br/DAIR_CARTEIRA"
params = {
    "nr_cnpj_entidade": "29131075000193",
    "sg_uf": "RJ",
    "dt_ano": "2025"
}

# 2. Fazer a chamada GET

response = requests.get(url, params=params)

if response.status_code == 200:
    dados_brutos = response.json()
    print("Requisição bem sucedida!") 
else:
    print("Erro na conexão:", response.status_code)
    exit() 

# 3. Buscando o nó com as informações solicitadas

lista_dados = dados_brutos.get('data',[])

# 4. Criando o DataFrame

df = pd.DataFrame(lista_dados)

# 5. Convertendo a coluna para numérico e formatando

df['vl_total_atual'] = pd.to_numeric(df['vl_total_atual'],errors='coerce')

pd.set_option('display.float_format', '{:,.2f}'.format)

# 6. Agrupando os valores e somando-os

df_mes = df.groupby('dt_mes_bimestre')['vl_total_atual'].sum()

print("Montante por mês")
print(df_mes)

#Salvando o DataFrame

df_mes.to_csv('C:\\Users\\João Pedro\\Desktop\\desafio_p2\\Montante_Mes_Marica_2025.csv')
