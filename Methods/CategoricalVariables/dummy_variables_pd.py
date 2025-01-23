import pandas as pd

df_fidelidade = pd.read_csv('Raw_Datasets\dados_fidelidade.csv')

print(df_fidelidade)

df_fidelidade_dummies = pd.get_dummies(df_fidelidade,
                                       columns=['atendimento',
                                                'sortimento',
                                                'acessibilidade',
                                                'preço',
                                                'sexo'],
                                       dtype=int,
                                       drop_first=True)
print(df_fidelidade.columns)
print(df_fidelidade_dummies.columns)
print(df_fidelidade_dummies)