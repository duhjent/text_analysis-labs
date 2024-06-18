import pandas as pd
import torch

data = torch.load('./data/translated-bbc.pt')

print(data[:3])

# with open('./data/bbc.csv', 'r') as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#         idx = lines[i].find(';')
#         lines[i] = lines[i].replace('\t', '')
#         lines[i] = lines[i].replace('\n', '')
#         lines[i] = lines[i][:idx+1] + '"' + lines[i][idx+1:]
#         lines[i] = lines[i] + '"' + '\n'

# with open('./data/bbc-new.csv', 'w') as fw:
#     fw.writelines(lines)
    

# df = pd.read_csv('./data/bbc-new.csv', delimiter=';', names = ['category','content'])
# print(df)
