from pandas import read_csv, isnull, DataFrame
from numpy import nan

def getDictAllData(filename='message_info.csv'):
    df = read_csv(filename)
    return df.to_dict('list')

def addData(key, data):
    dictData = getDictAllData()
    # Cek apakah ada nilai null pada baris terakhir
    isLastNull = False
    if dictData['idx'] != []:
        for col in dictData.keys():
            if isnull(dictData[col][-1]):
                isLastNull = True
                break
    
    # Jika ada nilai null
    if isLastNull:
        dictData[key][-1] = data

    # Jika tidak ada nilai null
    else:
        for col in dictData.keys():
            if col == key:
                dictData[col].append(data)
            else:
                dictData[col].append(nan)
        
    DataFrame(dictData).to_csv('message_info.csv', index=False)