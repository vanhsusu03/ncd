import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/2.2,2.3_train_5k.csv')

res = []
# deleted_rules = [
#     'daughter-husband',
#     'son-wife',
#     'husband-grandson',
#     'wife-granddaughter',
#     'husband-father',
#     'husband-mother',
#     'wife-father',
#     'wife-mother',
#     'husband-granddaughter',
#     'wife-grandson',
# ]
deleted_rules = [
    'grandson-brother',
    'granddaughter-sister',
    'grandson-sister',
    'granddaughter-brother',
    'son-son',
    'daughter-daughter',
    'son-daughter',
    'daughter-son',
    'daughter-husband',
    'son-wife',
    'husband-grandson',
    'wife-granddaughter',
    'husband-father',
    'husband-mother',
    'wife-father',
    'wife-mother',
    'husband-granddaughter',
    'wife-grandson',
    'brother-daughter',
    'sister-son',
    'brother-son',
    'sister-daughter',
    'mother-mother',
    'father-father',
    'mother-father',
    'father-mother',
]
for index, row in df.iterrows():
    if row['f_comb'] in deleted_rules:
        res.append(row)

print(len(res))
res = pd.DataFrame(res)
res.to_csv('./data/2.2,2.3_train_cannot_answer_85.csv', index = False)
