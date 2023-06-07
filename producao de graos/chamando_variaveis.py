'''

import pandas as pd
import json
import pprint

from variavel109safra1 import dados_lista as v109s1
from variavel109safra2 import dados_lista as v109s2
from variavel216safra1 import dados_lista as v216s1
from variavel216safra2 import dados_lista as v216s2
from variavel214safra1 import dados_lista as v214s1
from variavel214safra2 import dados_lista as v214s2

with open('variavel109safra1.json') as file:
    dados109safra1 = json.load(file)

with open('variavel109safra2.json') as file:
    dados109safra2 = json.load(file)
    
with open('variavel214safra1.json') as file:
    dados214safra1 = json.load(file)

with open('variavel214safra2.json') as file:
    dados214safra2 = json.load(file)

with open('variavel216safra1.json') as file:
    dados216safra1 = json.load(file)

with open('variavel216safra2.json') as file:
    dados216safra2 = json.load(file)


df109safra1 = pd.DataFrame([(municipio['cidade'], d['data'], d['área plantada (hectares)'], d['safra'], d['produto'])
                      for municipio in dados109safra1 for d in municipio['dados']],
                     columns=['cidade', 'data', 'área plantada (hectares)', 'safra', 'produto'])
df109safra2 = pd.DataFrame([(municipio['cidade'], d['data'], d['área plantada (hectares)'], d['safra'], d['produto'])
                      for municipio in dados109safra2 for d in municipio['dados']],
                     columns=['cidade', 'data', 'área plantada (hectares)', 'safra', 'produto'])

df214safra1 = pd.DataFrame([(municipio['cidade'], d['data'], d['quantidade produzida (toneladas)'], d['safra'], d['produto'])
                      for municipio in dados214safra1 for d in municipio['dados']],
                     columns=['cidade', 'data', 'quantidade produzida (toneladas)', 'safra', 'produto'])
df214safra2 = pd.DataFrame([(municipio['cidade'], d['data'], d['quantidade produzida (toneladas)'], d['safra'], d['produto'])
                      for municipio in dados214safra2 for d in municipio['dados']],
                     columns=['cidade', 'data', 'quantidade produzida (toneladas)', 'safra', 'produto'])

df216safra1 = pd.DataFrame([(municipio['cidade'], d['data'], d['área colhida (hectares)'], d['safra'], d['produto'])
                      for municipio in dados216safra1 for d in municipio['dados']],
                     columns=['cidade', 'data', 'área colhida (hectares)', 'safra', 'produto'])
df216safra2 = pd.DataFrame([(municipio['cidade'], d['data'], d['área colhida (hectares)'], d['safra'], d['produto'])
                      for municipio in dados216safra2 for d in municipio['dados']],
                     columns=['cidade', 'data', 'área colhida (hectares)', 'safra', 'produto'])


merged_df1 = pd.merge(df109safra1, df214safra1, on=['cidade', 'data', 'safra', 'produto'])
merged_df1 = pd.merge(merged_df1, df216safra1, on=['cidade', 'data', 'safra', 'produto'])

merged_df2 = pd.merge(df109safra2, df214safra2, on=['cidade', 'data', 'safra', 'produto'])
merged_df2 = pd.merge(merged_df2, df216safra2, on=['cidade', 'data', 'safra', 'produto'])

df_union = pd.concat([merged_df1, merged_df2], ignore_index=True)

df_union.to_csv('tabela839.csv', index=False)
pprint.pprint(df_union)

'''