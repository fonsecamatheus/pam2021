'''

import pandas as pd
import pprint
import shutil 

caminho_origem839 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\tabela839\tabela839.csv'
caminho_destino839 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\chamando\tabela839.csv'

caminho_origem1000 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\tabela1000\tabela1000.csv'
caminho_destino1000 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\chamando\tabela1000.csv'

caminho_origem1001 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\tabela1001\tabela1001.csv'
caminho_destino1001 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\chamando\tabela1001.csv'

caminho_origem1002 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\tabela1002\tabela1002.csv'
caminho_destino1002 = r'C:\Users\fonsecamatheus\Desktop\PAM 2021\chamando\tabela1002.csv'


shutil.copyfile(caminho_origem839, caminho_destino839)
shutil.copyfile(caminho_origem1000, caminho_destino1000)
#shutil.copyfile(caminho_origem1001, caminho_destino1001)
#shutil.copyfile(caminho_origem1002, caminho_destino1002)

tabela839 = pd.read_csv(caminho_destino839)
tabela1000 = pd.read_csv(caminho_destino1000)

tabelas_concatenadas = pd.concat([tabela839, tabela1000])
tabelas_concatenadas.to_csv('tabelasconcatenadas.csv', index=False)

'''