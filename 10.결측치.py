# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # 10. 결측치
# 비어 있는 데이터

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# ## 데이터 채우기 fillna

df.fillna('') # NaN 데이트를 빈 칸으로 채움

df.fillna('없음')

import numpy as np
df['학교'] = np.nan # 학교 데이터 전체를 NaN으로 채움
df

df.fillna('모름') # 전체 데이터에 적용

df.fillna('모름', inplace=True)
df

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df['SW특기'].fillna('확인 중', inplace=True) # SW특기 데이터 중에서  NaN 에 대해서 채움
df

# ## 데이터 제외하기 dropna

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.dropna() #전체 데이터 중에서 NaN을 포함하는 데이터 삭제

df

df.dropna(inplace=True)
df

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# ### axis : index / columns
# ### how : any / all

df.dropna(axis='index', how='any') # NaN 가 하나라도 있는 row 삭제

df.dropna(axis='columns') #  NaN 이 하나도 있는 colum 삭제

df['학교'] = np.nan
df

df.dropna(axis='columns', how='all') # 데이터 전체가 NaN인 경우에만 Column 삭제




