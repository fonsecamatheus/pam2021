'''

import pandas as pd
import requests
import json
import pprint 

api109 = ''

def chamando_api(api):
    dados = requests.get(api)
    dados_api = dados.json()
    
    return dados_api

def coletando_dados(dados_api):
    dados_brutos = dados_api[0]['resultados'][0]['series']
    municipios_dados = []
    for i in dados_brutos:
        nome = i['localidade']['nome']
        dados = i['serie']
        municipio = {'cidade': nome, 'dados': dados}
        municipios_dados.append(municipio)
    
    return municipios_dados

def tratando_dados(municipios_dados):
    for municipio in municipios_dados:
        municipio['cidade'] = municipio['cidade'].replace(' (MT)', '')       
        dados =  municipio['dados']
        for chave, valor in dados.items():
            if valor == '...' or valor == '-':
                dados[chave] = '0'

    return municipios_dados

def tratando_dados2(municipios_dados):
    dados_lista = []
    for i in municipios_dados:
        cidade = i['cidade']
        dados = i['dados']
        
        df = pd.DataFrame(dados.items(), columns=['ano', 'área plantada (hectares)'])
        df['data'] = pd.to_datetime(df['ano'], format='%Y').dt.strftime('%d/%m/%Y')
        df['produto'] = 'Milho'
        df['safra'] = 1 
 
        municipio = {
            'cidade' : cidade,
            'dados' : df.drop('ano', axis=1).to_dict(orient='records')
        }
        dados_lista.append(municipio)
    
    return dados_lista

def printando_dados(dados_lista):
    pprint.pprint(dados_lista)

def gravando_dados(dados_lista):
    with open('variavel109safra1.json','w') as arquivo_tratando:
        json.dump(dados_lista, arquivo_tratando)


api = chamando_api(api109)
dados_coletados =  coletando_dados(api)
dados_tratados = tratando_dados(dados_coletados)
dados_lista = tratando_dados2(dados_tratados)
printando_dados(dados_lista)
gravando_dados(dados_lista)

'''