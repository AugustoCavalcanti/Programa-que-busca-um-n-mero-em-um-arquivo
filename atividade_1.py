import datetime
start_time = datetime.datetime.now()

arq=open('dataset-1-c.csv','r')
conteudo=arq.read()
arq.close()
dados = conteudo.split('\n')

n = dados[0]
t = int(dados[1]) - 1
D = dados[2:-1]

posicao = 0
palavra = 'False'

while posicao < int(t) and palavra == 'False':
    if int(D[posicao]) == int(n):
        palavra = 'True'
    posicao += 1

if palavra == 'False':
    posicao = -1

arq2=open('resposta-dataset-1-c.txt','w')
arq2.write(palavra+'\n')
arq2.write(str(posicao)+'\n')

end_time = datetime.datetime.now()
time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000

arq2.write(str(execution_time)+'\n')
arq2.close()
