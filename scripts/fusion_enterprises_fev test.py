# Importing libs
import json
import csv

from data_processing import Data

# Defining the paths to the initial files
path_json = "data_raw/dados_empresaA.json"
path_csv = "data_raw/dados_empresaB.csv"
final_path = "data_processed/dados_combinados_test.csv"

# Extract
data_entA = Data(path_json, "json")
data_entB = Data(path_csv, "csv")

# Transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

data_entB.treating_data(key_mapping)

# Combining the data into a single list of lists and saving it to a CSV file
Data.combining_and_saving_data(data_entA.data, data_entB.data, final_path)