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

# ## 9.데이터 선택(조건)
# 조건에 해당하는 데이터 선택

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df['키'] >= 185 # 학생들의 키가 185이상인지 여부를 True/False

filt = (df['키'] >= 185)
df[filt] # 키가 185 이상인 학생들의 데이터

df[~filt] #filt 를 역으로 적용

df[df['키'] >= 185]

df.loc[df['키'] >= 185, '수학'] #키가 185 이상의 학생들의 수학 데이터

df.loc[df['키'] >= 185, ['이름','수학','과학']]

# ## 다양한 조건
# ### & : and 

df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')]

# ### | : or

df.loc[(df['키'] < 170)|(df['키'] > 200)]

# ### str 함수

filt = df['이름'].str.startswith('송') # '송' 씨 성을 가진 사름
df[filt]

filt = df['이름'].str.contains('태')
df[filt]

df[~filt]

langs = ['Python', 'Java']
filt = df['SW특기'].isin(langs) # 특기가 Python 이나 Java 인 사람
df[filt]

df

langs = ['python', 'java']
filt = df['SW특기'].str.lower().isin(langs) # 소문자로 바꿔서 비교
df[filt]

df['SW특기'].str.lower().isin(langs)

df['SW특기'].str.contains('Java', na=True) # NaN 데이터에 대해서 True로 설정

filt = df['SW특기'].str.contains('Java', na=False)
df[filt]
