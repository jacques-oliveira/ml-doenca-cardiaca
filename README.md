# Deep Learning RNA - Presença de Doença Cardíaca em paciente
## Classificação de doença cardíaca usando RNA
<div>
  <img src = https://www.heart.org/-/media/Images/News/2021/June-2021/0623SilentHeartAttack_SC.jpg?sc_lang=en width="380">
</div>
Fazer a classificação de um banco de dados com 13 atributos e um target. Em particular, o banco dedados de 
Cleveland, que é o único usado pelos pesquisadores de ML até hoje. O campo "objetivo" refere-se á presença de 
doença cardíaca no paciente.

## Apresentar como resultado a acurácia, precisão, recall, f1_score e matriz de confusão do classificador
- Utilizar Batch Size = 10
- Percentual para %teste = n * 20, aqui adotado n = 0.95, %teste = 19
## Responder as Seguintes perguntas:
- 1 Quantos atributos essa base tem ?
- 2 Quantas classes essa base tem ?
- 3 Qual foi o percentual da base usada para testes ?
- 4 Quantas amostras foram usadas no treinamento dessa RNA ?
- 5 No comando que criou a primeira camada da rede, qual seria o valor do parâmetro "input_dim" ?
- 6 No comando que criou aútlima camada dessa rede, qual seria o valor do parâmetro "units" ?
- 7 Escreva o comando que compila essa rede com as definições que você usaria nos parâmetros
- 8 Quantos conjuntos de pesos foram salvos em cada época ?
- 9 Quantas atualizações de peso (interações) foram antes que um valor seja salvo ?