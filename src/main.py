import pandas as pd # apelido da biblioteca
import os # biblioteca para usar recursos do sistema operacional
import glob # serve para ler arquivos em massa

folder_path = 'src\\data\\raw' # definição do caminho para ler os arquivos

# lista todos os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compatível encontrado.") # caso não tenha arquivos, o tratamento não ocorre
else:
    # dataframe = tabela na memoria para guardar os conteúdos dos arquivos
    dfs = []

    for excel_file in excel_files:

        try:
            #dataframe temporário
            df_temp = pd.read_excel(excel_file) #função do panda para ler um arquivo 

            file_name = os.path.basename(excel_file) # leutura do caminho do arquivo

            df_temp['filename'] = file_name # inclusão do nome do arquivo de origem

            # tratamento 1: criação da rastreabilidade dos dados com a coluna location
            if 'brasil' in file_name.lower():
                df_temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_temp['location'] = 'it'

            # tratamento 2: criação da rastreabilidade dos dados com a coluna campanha
            df_temp['campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')

            dfs.append(df_temp)# guardar os dados tratados

        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")# se ocorrer um erro, irá aparecer mensagem


if dfs: 

    result = pd.concat(dfs, ignore_index=True) # pegar várias tabelas que estão no dfs e concatenar em uma só

    output_file = os.path.join('src','data','ready', 'clean.xlsx') # caminho de saída

    #configuração do motor para escrever arquivo no Excel
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    #leva os dados do resultados a serem escritos no motor configurado na linha acima
    result.to_excel(writer, index=False)

    #salva o arquivo de excel
    writer._save()
else:
    print("Nenhum dado para ser salvo.")