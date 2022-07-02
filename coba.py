import pandas as pd

df = pd.read_csv('contacts.csv')

kontak = df.to_dict('list')

print(kontak)
