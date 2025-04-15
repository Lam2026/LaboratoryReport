# Created by leonacui
import pandas as pd
import os


with open('20210610.klt1.ublox.f9p.pos.txt') as f:
    f = f.readlines()
    ff = []
    for i in range(len(f)):
        l_i = f[i].split('\n')[0].split(' ')
        l_i_clean = []
        for j in range(len(l_i)):
            if l_i[j] is not '':
                l_i_clean.append(l_i[j])
        ff.append(l_i_clean)



df = pd.DataFrame(ff)
df_want = df.iloc[:,:5]
df_want.to_csv('20210610.klt1.ublox.f9p.pos.csv', index=False, header=False)
