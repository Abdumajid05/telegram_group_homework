import json
def read_data(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    #open file
    f=open(file_path,mode='r',encoding='utf-8')
    a=f.read()
    return json.loads(a)

#b=json.loads(f)
read_data('result.json')