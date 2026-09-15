import json
import csv

class Data:
    
    def __init__(self, path, data_type):  # Constructor method
        self.path = path
        self.file_type = data_type
        self.data = self.__reading_data()
        self.columns = self.__get_cols(self.data)

    # CREATING FUNCTION
    # Extracting data functions
    def __reading_json(self):
        with open(self.path, "r") as f:
            dados_json = json.load(f)
        return dados_json

    def __reading_csv(self):
        dados_csv = []  
        with open(self.path, "r") as f:
            spamreader = csv.DictReader(f, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
            return dados_csv

    def __reading_data(self):
        if self.file_type == "json":
            return self.__reading_json()
        elif self.file_type == "csv":
            return self.__reading_csv()
        else:
            raise ValueError("Invalid file type. Please use 'json' or 'csv'.")

    #Treating data functions
    @staticmethod
    def __get_cols(data):
        return list(data[-1].keys())

    def treating_data(self, key_mapping):
        new_data = []                 
        for dicts in self.data:
            dict_temp = {}
            for old_key, value in dicts.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)
        self.data = new_data

    @staticmethod
    def combining_and_saving_data(data1, data2, final_path):
        combined_data = data1 + data2
        cols = Data.__get_cols(combined_data)

        final_dataset = [cols]
        for row in combined_data:
            line = [row.get(col, "Not available") for col in cols]
            final_dataset.append(line)

        with open(final_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows(final_dataset)
