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

# # Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리

import pandas as pd

# # 1. Series
# 1차원 데이터(정수, 실구, 문자열 등)

# ## Series 객체 생성
# ex) 1월부터 4월까지 평균 온도 데이터(-20, -10, 10, 20)

temp = pd.Series([-20, -10, 10, 20])
temp

temp[0]

temp[2]

# # Series 객체 생성(index 지정)

temp = pd.Series([-20, -10, 10, 20], index=['Jan','Feb','Mar','Apr'])
temp

temp['Jan']

temp['Apr']

# +
# temp['Jun']
