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

# # 5. 데이터 확인

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# ## DataFrame 확인
# 계산 가능한 데이터에 대해 Column 별로 데이터의 갯수, 평균, 표준편차, 최소/최댓값 등의 정보를 보여줌

df.describe()

df.info()

df.head() # 처음 5개의 row를 가져옴

df.head(7)

df.tail() # 마지막 5개 row를 자겨옴

df.tail(3)

df.values

df.index

df.columns

df.shape # row, column(index 제외)

df

# ## Series 확인

df['키'].describe()

df['키'].min()

df['키'].max()

df['키'].nlargest(3) # '키' 큰 사람 순서대로 3명

df['키'].mean()

df['키'].sum()

df['SW특기'].count()

df['학교'].unique()

df['학교'].nunique()
