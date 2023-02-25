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

# ## 6. 데이터 선택(기본)

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# ## Column 선택(label)

df['이름']

df['키']

df[['이름','키']]

# ## Column 선택(정수 index)

df.columns

df.columns[0]

df.columns[2]

df[df.columns[0]]

df.columns[-1]

df[df.columns[-1]]

# ## 슬라이싱

df['영어'][0:5] # 0~4 까지 영어점수 데이터를 가져옴

df[['이름','키']][:3] # 처음 3명의 이름, 키 정보를 가져옴

df[3:]
