# ETL com Python

## Problema a ser resolvido:
A matriz principal na LoveraStream manda os relatórios dos assinantes, cada dia recebemos um. Todos os dias temos arquivos novos, sem padrão nenhum. Cada país tem seus próprios relatórios e precisamos transformar em apenas um arquivo. Os relatórios contêm as informações das pessoas que estão assinando como data de venda do plano, nome da pessoa, tipo de plano, o valor que ela pagou, link de UTM.

## O que será necessário para realizar o projeto:
- Python
- Pip - Gerenciador de pacotes
  - Pandas: biblioteca de Python focada em tratar dados
  - Openpyxl: Ler e escrever em arquivos de excel
  - Xlsxwriter: Escrever em arquivos de excel

## Conceitos
- Crie sempre um ambiente virtual (VENV)
- Criar uma pasta SRC para armazenamento dos arquivos de códigos e dados
- Dentro da pasta SRC, criar uma pasta de Data e dentro dela duas pastas, RAW e READY.
  - RAW: dados na forma crua, antes de qualquer processamento
  - READY: dados que foram passados pelo meu processo de refinamento
  - DataRaw →→→→ Data Ready
- Criar um arquivo onde estará o meu código dentro da pasta SRC

## Tratamentos dos dados: Dicas e Regras para a organização dos dados
- Prezar pela confiabilidade e rastreabilidade
- ETL: Processo em 3 etapas
  1) Extrair: Neste projeto os dados já foram extraídos e armazenados em diversos arquivos de formato excel.
  2) Transformar: Tratamento e transformação dos dados (arquivos excel)
  3) Carregar: Um arquivo tratado e preparado para ser entregue ao cliente (fictício)
