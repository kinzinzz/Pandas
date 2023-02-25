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

# # 12. 데이터 수정

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# ## Column 수정

df['학교'].replace({'북산고':'상북고','능남고':'홍익고'})

df

df['학교'].replace({'북산고':'상북고'}, inplace=True)
df

df['SW특기'].str.lower()

df['SW특기'] = df['SW특기'].str.lower()
df

df['SW특기'] = df['SW특기'].str.upper()
df

df['학교'] = df['학교'] + '등학교' # 학교 + 등학교
df

# ## Column 추가

df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df

df['결과'] = 'Fail' # 결과 Column을 추가하고 전체 데이터는 Fail로 초기화
df

df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트
df

# ## Column 삭제

df.drop(columns=['총합']) # 총합 Column 을 삭제
df

df.drop(columns=['총합'])

df.drop(columns=['총합','국어','수학'])

# ## Row 삭제

df.drop(index='4번') # 4번 학생 데이터 row를 삭제

filt = df['수학'] < 80
df[filt]

df[filt].index

df.drop(index=df[filt].index)

# ## Row 추가

df.loc['9번'] = ['이정환','해남고등학교',184,90,90,90,90,90,'Kotlin',450,'Pass'] # 새로운 Row 추가
df

df

# ## Cell 수정

df.loc['4번','SW특기'] = 'Python' # 4번 학생의 SW특기 데이터를 Python으로 변경
df

df.loc['5번',['학교','SW특기']] = ['능남고','C']
df

# ## Column 순서 변경

cols = list(df.columns)
cols

df = df[[cols[-1]] + cols[0:-1]] # 맨 뒤에 있는 결과 Column 을 앞으로 가져오고, 나머지 Column 들과 합쳐서 순서 변경
df

# ## Column 이름 변경

df = df[['결과','이름','학교']]
df

df.columns

df.columns = ['Result','Name','School']
df
