# Importing libs
import json
import csv

# CREATING FUNCTION
# Extracting data functions
def reading_json(path_json):
    with open(path_json, "r") as f:
        dados_json = json.load(f)
    return dados_json

def reading_csv(path_csv):
    dados_csv = []  
    with open(path_csv, "r") as f:
        spamreader = csv.DictReader(f, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
        return dados_csv

def reading_data(path, type_file):
    if type_file == "json":
        return reading_json(path)
    elif type_file == "csv":
        return reading_csv(path)
    else:
        raise ValueError("Invalid file type. Please use 'json' or 'csv'.")

#Treating data functions
def get_cols(data):
    columns = list(data[-1].keys())
    return columns

def treating_data(data, key_mapping):
    new_data = []
    for dicts in data:
        dict_temp = {}
        for old_key, value in dicts.items():
            dict_temp[key_mapping[old_key]] = value
        new_data.append(dict_temp)
    return new_data

def combining_and_saving_data(final_path,data1, data2): # Does a more complex analysis of the dataset, checking if any champ is missing
    combined_data = data1 + data2
    cols = get_cols(combined_data)

    final_dataset = [cols] # Start with the header row
    for row in combined_data:
        line = []
        for col in cols:
            line.append(row.get(col, "Not available"))
        final_dataset.append(line)

    # Saving the final dataset to a CSV file
    with open(final_path, "w") as f:
        writer = csv.writer(f)
        writer.writerows(final_dataset)


# Defining the paths to the initial files
path_json = "data_raw/dados_empresaA.json"
path_csv = "data_raw/dados_empresaB.csv"
final_path = "data_processed/dados_combinados.csv"

# Reading the data
data_json = reading_data(path_json, "json")
data_csv = reading_data(path_csv, "csv")

# Treating the data
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
key_mapping

# Combining the data into a single list of dictionaries
new_data_csv = treating_data(data_csv, key_mapping)

combining_and_saving_data(final_path,data_json, new_data_csv)