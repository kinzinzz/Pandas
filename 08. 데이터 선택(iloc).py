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

# ## 8.데이터 선택(iloc)
# 위치를 이용해서 원하는 row에서 원하는 col을 선택

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.iloc[0] # 0번째 위치의 데이터

df.iloc[4]

df.iloc[0:5] # 0~4번째 위치의 데이터

df.iloc[0, 1] # 0번째 위치의 1번째(index 제외) 데이터

df.iloc[4, 2] # 4번째 위치의 2번째 데이터

df.iloc[[0,1],2]

df.iloc[[0,1],[3,4]]

df.iloc[0:5,3:8]
