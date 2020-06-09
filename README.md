# Percepção da divulgação dos dados no portal da COVID-19 do Ministério da Saúde

#### Eric Araújo (eric@ufla.br)


Para entender a metodologia, acesse [o artigo sobre como foi criado o modelo](https://medium.com/@ericinlinux/como-torturar-os-dados-at%C3%A9-eles-confessarem-o-caso-covid-19-ef5ac378c721).


![Resultados para a exibição das mortes diárias nos dois portais](./figs/mortes_diarias.png?raw=true "Mortes diárias")

![Resultados para a exibição da percepção do total de mortes nos dois portais](./figs/mortes_total.png?raw=true "Mortes diárias")

## Instruções

Instale as bibliotecas do Python no terminal:
```
pip install -r requirements.txt
```

O código em Python deve ser executado para gerar a curva de Poisson por meio do comando: 

```
python create_poisson.py
```

O modelo se encontra no arquivo Simulacoes_COVID.nlogo. Para executar o código, instale a ferramenta [Netlogo](https://ccl.northwestern.edu/netlogo/) em seu computador. Para executar o modelo, clique no botão "setup" e logo após no botão "go".
