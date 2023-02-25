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

# # 13. 함수 적용

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df = pd.read_excel('score.xlsx', index_col='지원번호')
df


# ## 데이터에 함수 적용(apply)

# +
def add_cm(height):
    return str(height) + 'cm'

df['키'] = df['키'].apply(add_cm)
df


# +
def capitalize(lang):
    if pd.notnull(lang): # NaN 이 아닌지
        return lang.capitalize() # 첫 글자는 대문자로, 나머지는 소문자로
    return lang

df['SW특기'] = df['SW특기'].apply(capitalize)
df
# -

df['SW특기'].str.capitalize()
