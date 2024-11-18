# Deep Learning RNA - Presença de Doença Cardíaca em paciente
## Classificação de ataque cardíaco usando RNA
<div>
  <img src = https://www.heart.org/-/media/Images/News/2021/June-2021/0623SilentHeartAttack_SC.jpg?sc_lang=en width="380">
</div>
Fazer a classificação de um banco de dados com 13 atributos e um target. Em particular, o banco dedados de 
Cleveland, que é o único usado pelos pesquisadores de ML até hoje. O campo "objetivo" refere-se á presença de 
doença cardíaca no paciente.

<br>
<br>

- age = idade em anos
- sex(1 = male; 0 = female)
- cp tipo de dor no peito
- trestbps pressão sanguínea em repouso(in mm Hg on admission to the hospital)
- chol colesterol sérico mg/dl
- fbs (açucar no sangue> 120 mg/dl) (1 = true; 0 = false)
- restecg resultados eletrocardiográficos em repouso (0, 1 e 2)
- thalach frequência cardíaca máxima atingida
- exang angina induzida por exercício(1 = yes; 0 = no)
- oldpeak depressão ST induzida pelo exercício em relação ao repouso
- slope a inclinação do segmento ST do pico do exercício
- ca número de vasos principais (0-3) coloridos por fluoroscopia
- thal 3 = normal; 6 = defeito fixo; 7 = defeito reversível de dor no peito
- target 1 or 0 (1 = doente e 0 = saudável)

## Apresentar como resultado a acurácia, Precisão, Recall, F1_score e Matriz de Confusão do classificador
- Utilizar Batch Size = 10
- Percentual para %teste = 19
- Uso de One-Hot-Encoding
- BatchNormalization
- kernel_regularizer

<P>
  <strong>Obs:</strong> Com uso de One-Hot-Encoding o número de entradas muda, preferi usar no <strong>input_dim = entradas.shape[1]</strong>,
  que retorna o número atualizado de entradas
</P>  

## Desenvolvimento
- Python 3.11.10
- keras, sklearn, numpy, pandas, matplotlib, seaborn
- IDE Spyder 6.0.2

## Resultados
- Acurácia: 0.862069
- Precision: 0.794118
- Recall: 0.964286
- F1-Score: 0.870968

<img width="491" alt="Figure 2024-11-13 221446" src="https://github.com/user-attachments/assets/ce697f58-5bce-4a5e-bc9e-476c3a0ae49c">

<div>
  <p><strong>Obs:</strong> Neste treinamento foi priorizado ter o menor possível Falsos Negativos, ou seja, 
    o Recall é importante, já que se prezou por não dizer que o paciente teve infarto, tendo ele na verdade infartado.
  </p>
</div>

