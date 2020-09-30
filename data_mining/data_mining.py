"""
    Cross-industry standard process for data mining

1) Entendimento do negócio 
esta etapa consiste em definir os objetivos do projeto de Data Mining com um olhar para os problemas de negócio. 
É importante salientar que o ciclo de desenvolvimento do projeto só tem efeito se for orientado para resolver um problema de negócio

2) Entendimento dos Dados 
esta etapa consiste desde a captura dos dados até a identificação de problemas relacionados à qualidade.
Nesta fase é também onde se formam hipóteses em cima do que se aprendeu com os dados.

3) Preparação dos Dados 

Preparação dos dados: cobre todas as atividades para construir o conjunto de dados final – dados que alimentarão as ferramentas –, a partir dos dados iniciais brutos. Tarefas de preparação podem ser repetidas várias vezes, sem ordem predeterminada. Incluem seleção de tabelas,  de  registros  e  de  atributos,  bem  como  transformações  e  limpeza  dos  dados  para  as  ferramentas de mineração. A  preparação  dos  dados  é  uma  fase  importante  dentro  do  processo,  que  consome  grande  parte  do  tempo  e,  em  muitos  projetos,  não  recebe  a  devida  atenção.  O  desafio  é  preparar  os  dados  de  forma  que  a  informação  contida  neles  seja  exposta  da  melhor  maneira  para   as   ferramentas   de   mineração   (PYLE,   1999),   momento   em   que   as   atividades   de   compreensão do domínio fazem diferença


3.1. Seleção dos dados.

    Foi realizada uma busca por bases de dados adequadas para o projeto em questão. Inicialmente a preferência seria por dados reais, por isso analizou-se opções disponíveis nos sites de séries estatatísticas do IBGE [https://seriesestatisticas.ibge.gov.br/series.aspx?no=10&op=0&vcodigo=CD90&t=populacao-presente-residente] e no acervo de downloads da mesma instituição [https://www.ibge.gov.br/estatisticas/downloads-estatisticas.html].
    Todavia, a descrição dos dados apresentados era muito pobre e o formato de disponibilização dos mesmos também. A maior parte deles podia ser acessada através planilhas nos formatos .xlsx e .ods , contendo várias abas em cada planilha e com a presença de cédulas acopladas. Além disso, o volume de dados contido em cada planilha normalmente era pequeno, o que não seria de acordo com o propósito do projeto, que é de trabalhar com grandes quantidades de dados. As planilhas do IBGE nas referências analisadas, em geral apresentavam apenas resumos e classificações dos dados, e não a definição bruta dos mesmos.
    A busca por dados adequados para o projeto continuou e foi notada a disponibilização de bases relevantes pelo professor na atividade de análise exploratória presente no Moodle [https://moodle.ufsc.br/mod/assign/view.php?id=2341649]. Desta forma, foram analisados os DataSets disponibilizadas pela UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/datasets.php] e escolhido o conjunto Adult. Ele foi considerado adequado para o projeto pois possui uma quantidade relevante de registros (48842), tem um número significativo de colunas(14) e ilustra um conjunto real de informações presentes em um censo realizado.
    
    A implementação do programa que extrai as informações desejadas foi feito utilizando Python 3.6.9. 


3.2. Integrar dados: combinar múltiplas tabelas ou outras fontes ( essa etapa acontece nesse ponto pois o formato dos dados é identico nas duas fontes de dados utilizadas, ou seja, nao precisa ser adequado antes da integração)
3.3. Limpar os dados (dados nulos, ausentes, zerados, inválidos, etc..)
3.4. Construir dados (criar novos atributos a partir de outros)
3.5. Formatar dados: modificações sintáticas nos dados, sem alterar o seu significado

"""
from data_mining.vars import download, adult_data, adult_test, adult_data_test
from data_mining import crawler
from data_mining.utils import (
    append_files,
    create_continent_column,
    delete_lines,
    replace_characters
)

def get_data():
    print('Extracting data from website...')
    crawler.extract_data()
    print('Data has been extracted.')

def integrate_data():
    print(f'Appending {adult_data_test}...')
    append_files(
        output_file=adult_data_test,
        input_filenames=[adult_data, adult_test],
        basepath=download
    )
    print(f'Data from {adult_data} and {adult_test} has been appended to {adult_data_test}.')

def clean_data():
    print('Deleting invalid lines...')
    delete_lines(bad_word="?", basepath=download, filename=adult_data_test)
    delete_lines(bad_word="|1x3", basepath=download, filename=adult_data_test)
    delete_lines(bad_word="South", basepath=download, filename=adult_data_test)
    # |1x3: Linhas inválidas do arquivo adult.test
    # ? : Linhas com valores nulos
    # South : Linhas com valor inválido para a coluna "country"
    print('Invalid lines deleted.')

def build_data():
    print('Building data...')
    # Mudança para valores mais facilmente interpretáveis
    replace_characters('<=50K.', '1')
    replace_characters('>50K.', '2')
    replace_characters('<=50K', '1')
    replace_characters('>50K', '2')
    # Ordem específica do replace da palara "Female" anteriormente à palavra "Male"
    replace_characters('Female', 'F')
    replace_characters('Male', 'M')
    # Criação da coluna "continent" baseando-se na coluna "country"
    create_continent_column(basepath=download, filename=adult_data_test)
    print('Data has been builded.')

def format_data():
    print('Formatting data...')
    # Escritos de maneira incorreta
    replace_characters('Columbia', 'Colombia')
    replace_characters('Hong', 'Hong Kong')
    replace_characters('Trinadad&Tobago', 'Trinidad and Tobago')
    # Remoção do caracter "-" 
    replace_characters('United-States', 'United States')
    replace_characters('Puerto-Rico', 'Puerto Rico')
    replace_characters('Dominican-Republic', 'Dominican Republic')
    replace_characters('El-Salvador', 'El Salvador')
    replace_characters('Holand-Netherlands', 'Netherlands')
    print('Data has been formatted.')
