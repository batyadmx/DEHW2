import pandas as pd
import json
import pickle
import msgpack

def addNumericColumns():
    for col in numericColumns:
        results[f"MAX {col}"] = int(df[col].max())
        results[f"MIN {col}"] = int(df[col].min())
        results[f"MEAN {col}"] = int(df[col].mean())

    return results

def addFreqDicts():
    for col in freqColumns:
        results[f"{col} FREQ DICT"] = getFreqDictOfArray(df[col])

def getFreqDictOfArray(array):
    dict = {}
    for el in array:
        el = str(el).upper()
        if el not in dict:
            dict[el] = 0
        dict[el] += 1
    return sorted(dict.items(), key= lambda x: x[1], reverse=True)

def addTimeDistribution():
    timeDistr = dict([(i, 0) for i in range(0, 24)])
    for time in df['CRASH TIME']:
        hour = int(time.split(':')[0])
        timeDistr[hour] += 1
    results['CRASH TIME DISTRIBUTION'] = timeDistr


df = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes.csv", low_memory=False)

df = df[['NUMBER OF PERSONS INJURED',
          'NUMBER OF PERSONS KILLED',
          'NUMBER OF PEDESTRIANS INJURED',
          'NUMBER OF PEDESTRIANS KILLED',
          'BOROUGH',
          'VEHICLE TYPE CODE 1',
          'CRASH TIME']]

numericColumns = ['NUMBER OF PERSONS INJURED',
                  'NUMBER OF PERSONS KILLED',
                  'NUMBER OF PEDESTRIANS INJURED',
                  'NUMBER OF PEDESTRIANS KILLED',]

freqColumns = ['BOROUGH', 'VEHICLE TYPE CODE 1']

results = {}
addNumericColumns()
addFreqDicts()
addTimeDistribution()

with open("result.json", "w") as file:
    file.write(json.dumps(results))

with open("result.msgpack", "wb") as file:
    file.write(msgpack.dumps(results))

with open("result.pkl", "wb") as file:
    file.write(pickle.dumps(results))