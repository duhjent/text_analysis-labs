import torch
import pandas as pd

bbc = pd.read_csv('./data/bbc-new.csv', delimiter=';', names = ['category','content'])
imdb = pd.read_csv('./data/df-shuffled.csv').drop(columns=['Unnamed: 0'])


translated_bbc = torch.load('./data/translated-bbc.pt')
translated_imdb = torch.load('./data/translated-data.pt')


bbc['content_uk'] = pd.Series([x[0]['translation_text'] for x in translated_bbc])
bbc.to_csv('./data/bbc-translated.csv', index=False)

imdb['review_uk'] = pd.Series([x[0]['translation_text'] for x in translated_imdb])
imdb.to_csv('./data/imdb-translated.csv', index=False)
