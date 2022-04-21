import sys

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

import datetime

df= pd.read_csv('name.basics.tsv', sep='\t')
df.head(20)
df.dtypes

#Convert this back to pandas  from tuple
df = pd.DataFrame(df)


#perfom the couny
df = pd.DataFrame(df)
TotalRowCount, InitiaColumnCount = df.shape
print('TotalRowCount',TotalRowCount)

# Convert the values the column  to lowercasedf['deathYear'] = df['deathYear'].map(str.lower)
df = df.apply(lambda x: x.str.lower() if(x.dtype == 'object') else x)
df = df.replace('\n','', regex=True)

df.shape

# Replace the  \n  character with empty string "" usin the regula expression
df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["",""], regex=True, inplace=True)

#Filter the deathYear when it empty as this isthe criteria for being ALIVE
df = df[df["deathYear"] == '']

df = df.fillna("")

#puthe the first column in a seperate colulmn in the dataFrame, to aid filtring
df['primaryProfession_VAL'] = df['primaryProfession'].apply(lambda x: x.split(',')[0])


df.dtypes

#count the nummber of proffesions sepretaed by a comma and put in a seperate column primaryProfession_COUNT
df['primaryProfession_COUNT'] = df['primaryProfession'].apply(lambda x: len(x.split(',')))

# Filter for for actors having 3 professions
df = df[df["primaryProfession_COUNT"] == 3 ]

# Filter for for actors having first profession to be equal to producer
df = df[df["primaryProfession_VAL"] == 'producer']

#perfom the couny
df = pd.DataFrame(df)
RowCount, ColumnCount = df.shape
print('************************************')
print('RowCount',RowCount)

print('************************************')

sys.exit(-1)