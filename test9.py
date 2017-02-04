import  pandas as pd

import  numpy as np

df = pd.read_csv("D:/TISintern/training_data.csv")


df['term'] = [(36 if col == ' 36 months' else 60) for col in list(df['term'])]
df['grade'] = [(1 if col == 'A' else 2 if col == 'B' else 3 if col =='C' else 4 if col =='D' else 5 if col =='E' else 6 if col=='F' else 7 ) for col in list(df['grade'])]
del df['emp_title']
df['emp_length'] = [(0.5 if col == '< 1 year' else 1 if col =='1 year' else 2 if col == "2 years" else 3 if col == "3 years" else 4 if col == "4 years" else 5 if col == "5 years" else 6 if col == "6 years" else 7 if col == "7 years" else 8 if col == "8 years" else 9 if col == "9 years" else 10 if col == "10+ years" else 0) for col in list(df['emp_length'])]
del df['pymnt_plan']
del df['zip_code']



df['sub_grade'] = [(1 if col == 'A1'else 1 if col ==  'B1' else 1 if col == 'C1' else 1 if col == 'D1' else 1 if col == 'E1' else 1 if col == 'F1' else 1 if col =='G1'
    else 2 if col == 'A2' else 2 if col == 'B2' else 2 if col == 'C2' else 2 if col == 'D2' else 2 if col == 'E2' else 2 if col == 'F2' else 2 if col =='G2'
    else 3 if col == 'A3' else 3 if col == 'B3' else 3 if col == 'C3' else 3 if col == 'D3' else 3 if col == 'E3' else 3 if col == 'F3' else 3 if col =='G3'
    else 4 if col == 'A4' else 4 if col == 'B4' else 4 if col == 'C4' else 4 if col == 'D4' else 4 if col == 'E4' else 4 if col == 'F4' else 4 if col =='G4'
    else 5 if col == 'A5' else 5 if col == 'B5' else 5 if col == 'C5' else 5 if col == 'D5' else 5 if col == 'E5' else 5 if col == 'F5' else 5 if col =='G5'
    else 6 if col == 'A6' else 6 if col == 'B6' else 6 if col == 'C6' else 6 if col == 'D6' else 6 if col == 'E6' else 6 if col == 'F6' else 6 if col =='G6'
    else 7 ) for col in list(df['sub_grade'])]

df.to_csv("D:/TISintern/newdata9.csv")