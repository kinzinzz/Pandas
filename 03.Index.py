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

# # 3.Index
# 데이터에 접근할 수 있는 주소값

# +
import pandas as pd
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

df = pd.DataFrame(data ,index=['1번','2번','3번','4번','5번','6번','7번','8번'])
df
# -

df.index

# ## Index 이름 설정

df.index.name = '지원번호'
df

# ## Index 초기화

df.reset_index()

df.reset_index(drop=True) # 원래 쓰던 '지원번호' index 삭제

df

df.reset_index(drop=True, inplace=True) # 실제 데이터에 반영

df

# ## Index 설정
# 지정한 column으로 index를 설정

df.set_index('이름')

df

df.set_index('이름', inplace=True)

df

# ## Index 정렬
# Index를 기준으로 오름차순, 내림차순 정렬

df.sort_index()

df.sort_index(ascending=False)
