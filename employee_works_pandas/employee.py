import pandas as pd

data = pd.read_csv("C:/Users/chipp/OneDrive/Desktop/EDA/employee_works_pandas/sample.csv")
# read the data from csv file
df = pd.DataFrame(data)
# convert into data structure
print(df)

"""
          Id first_name last_name  age                         job location
0    4000001   Kristina     Chung   55                       Pilot    india
1    4000002      Paige      Chen   74                     Teacher       uk
2    4000003     Sherri    Melton   34                 Firefighter       us
3    4000004   Gretchen      Hill   66  Computer hardware engineer    china
4    4000005      Karen   Puckett   74                      Lawyer   africa
..       ...        ...       ...  ...                         ...      ...
458  4000459   Gretchen   Francis   60                  Politician  ireland
459  4000460     Cheryl      Horn   40                Veterinarian  ireland
460  4000461     Audrey   Forrest   50                   Architect  ireland
461  4000462       Alan     Levin   43                Statistician  ireland
462  4000463      Wayne    Weiner   70                       Actor  ireland

[463 rows x 6 columns]

"""

print(df.describe())

"""
                 Id         age
count  4.630000e+02  463.000000
mean   4.000232e+06   49.673866
std    1.338008e+02   15.606897
min    4.000001e+06   21.000000
25%    4.000116e+06   36.000000
50%    4.000232e+06   51.000000
75%    4.000348e+06   64.000000
max    4.000463e+06   75.000000

"""