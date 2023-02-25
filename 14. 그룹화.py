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

# ## 14. 그룹화
# 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

df.groupby('학교').get_group('북산고')

df.groupby('학교').get_group('능남고')

df.groupby('학교').mean() # 계산 가능한 데이터들의 평균값

df.groupby('학교').size() # 각 그룹의 데이터수

df.groupby('학교').size()['능남고']

df.groupby('학교')['키'].mean()

df.groupby('학교')[['국어','영어','수학']].mean()

df['학년'] = [3,3,2,1,1,3,2,2]
df

df.groupby(['학교','학년']).mean()

df.groupby('학년').mean()

df.groupby('학년').mean().sort_values('키')

df.groupby('학년').mean().sort_values('키', ascending=False)

df.groupby(['학교','학년']).sum()

df.groupby('학교')[['이름','SW특기']].count()

school = df.groupby('학교')
school['학년'].value_counts() # 학교로 그룹화 한 뒤에 학년별 학생수를 가져옴

school['학년'].value_counts().loc['북산고']

school['학년'].value_counts(normalize=True).loc['북산고'] # 학생들의 수 데이터를 퍼센트로 비교하여 가져옴
