import pandas as pd

def read(file_path):
    read = pd.read_excel(file_path, sheet_name=None, header=None)
    
    first_sheet = list(read.keys())[0]
    first_column = read[first_sheet].iloc[:, 0]
    
    no_duplicates = first_column.drop_duplicates(keep='first')
    result = no_duplicates.tolist()
    
    return result