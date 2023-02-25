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

# # 7. 데이터 선택(loc)
# 이름을 이용해 원하는 row에서 원하는 col를 선택

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.loc['1번'] # index 1번에 해당하는 전체 데이터

df.loc['5번']

df.loc['1번','국어'] # index 1번에 해당하는 국어 데이터

df.loc[['1번','2번'],'영어'] # index 1번, 2번에 해당한느 영어 데이터

df.loc[['1번','2번'],['영어','수학']]

df.loc['1번':'5번','국어':'사회'] # index 1번~5번, 국어~사회(마지막 포함)
