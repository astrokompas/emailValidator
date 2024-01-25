import pandas as pd

def read(file_path):
    read = pd.read_excel(file_path, sheet_name=None, header=None)
    
    if not read:
        print("Error: No sheets found in the Excel file.")
        return []
    
    first_sheet = list(read.keys())[0]
    all_data_column = pd.concat([read[first_sheet][col].astype(str) for col in read[first_sheet]], ignore_index=True)
    
    all_data_column = all_data_column.fillna('')
    
    # first_column = read[first_sheet].iloc[:, 0]
    new_df = pd.DataFrame({first_sheet: all_data_column})
    for col in read[first_sheet].columns[1:]:
        new_df[col] = read[first_sheet][col]
    
    no_duplicates = new_df[first_sheet].drop_duplicates(keep='first')
    
    result = no_duplicates.tolist()
    
    return result