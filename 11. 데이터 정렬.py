# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 11. 데이터 정렬

# %%
import pandas as pd
df = pd.read_excel('score.xlsx', index_col='지원번호')
df

# %%
df.sort_values('키') # 키 기준으로 오름차순 정렬

# %%
df.sort_values('키', ascending=False)

# %%
df.sort_values(['수학','영어'], ascending=False) # 수학, 영어 점수 기준으로 내림차순

# %%
df.sort_values(['수학','영어'], ascending=[True, False]) # 수학 점수는 오름차순, 영어 점수는 내림차순

# %%
df['키'].sort_values()

# %%
df['키'].sort_values(ascending=False)

# %%
df.sort_index()

# %%
df.sort_index(ascending=False)
