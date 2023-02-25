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

# # 2.DataFrame
# 2차원 데이터 (Series 들의 모음)

# ## Data 준비
# 사전(dict) 자료구조를 통해 생성
#
# ex) 슬램덩크 주요 인물 8명에 대한 데이터

data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
data

data['이름']

data['키']

# ## DataFrame 객체 생성

import pandas as pd
df = pd.DataFrame(data)

df

# ## 데이터 접근

df['이름']

df['키']

df[['이름','키']]

# ## DataFrame 객체 생성(index 지정)

df= pd.DataFrame(data,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df

# ## DataFrame 객체 생성(Column 지정)
# data 중에서 원하는 column 만 생성하거나, 순서 변경 가능

df = pd.DataFrame(data,columns=['이름','학교','키'])
df

df = pd.DataFrame(data,columns=['이름','키','학교'])
df
