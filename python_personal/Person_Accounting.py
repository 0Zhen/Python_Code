import pandas as pd
from datetime import datetime

# 创建一个空的DataFrame来存储交易记录，现在包括Tags列
df = pd.DataFrame(columns=['Date', 'Amount', 'Category', 'Description', 'Tags'])

def add_transaction(amount, category, description="", tags=None):
    global df
    if tags is None:
        tags = []
    new_transaction = pd.DataFrame({
        'Date': [datetime.now()],
        'Amount': [amount],
        'Category': [category],
        'Description': [description],
        'Tags': [tags]
    })
    df = pd.concat([df, new_transaction], ignore_index=True)

def get_balance():
    return df['Amount'].sum()

def get_expenses_by_category():
    expenses = df[df['Amount'] < 0].groupby('Category')['Amount'].sum().abs()
    return expenses

def get_expenses_by_tag():
    # 展开标签列表，为每个标签创建一行
    expenses = df[df['Amount'] < 0].explode('Tags')
    # 按标签分组并计算总支出
    return expenses.groupby('Tags')['Amount'].sum().abs()

def add_tag_to_transaction(index, new_tag):
    if index in df.index:
        current_tags = df.at[index, 'Tags']
        if new_tag not in current_tags:
            df.at[index, 'Tags'] = current_tags + [new_tag]
    else:
        print("Transaction not found.")

# 示例使用
add_transaction(63000,"薪水")
add_transaction(-690, "固定支出", "TrainerRoad", ["Sport"])
add_transaction(-690, "固定支出", "Claude", ["Work"])
add_transaction(-299, "固定支出", "電話費", ["Necessities"])
add_transaction(-799,"固定支出", "網路費", ["Necessities"])
add_transaction(-45, "固定支出", "YoutubeMusic", ["Entertainment"])
add_transaction(-1088, "固定支出", "健身工廠", ["Sport"])
add_transaction(-3240, "固定支出", "國泰壽險", ["Necessities"])
add_transaction(-790, "固定支出", "PressPlay", ["Work"])
add_transaction(-125, "固定支出", "Strava", ["Sport"])
add_transaction(-30, "固定支出", "Apple Cloud", ["Necessities"])
add_transaction(-400, "固定支出", "燃料稅", ["Car","Tax"])
add_transaction(-594, "固定支出", "牌照稅", ["Car","Tax"])
add_transaction(-2558, "固定支出", "車寶貝分期", ["Car"])
add_transaction(-3923, "固定支出", "綜所稅", ["Tax"])




# 为已存在的交易添加新标签
#add_tag_to_transaction(0, "快餐")

print("所有交易:")
print(df)

print(f"\n当前余额: {get_balance()}")

print("\n各类别支出:")
print(get_expenses_by_category())

print("\n各标签支出:")
print(get_expenses_by_tag())

# 数据分析示例
print("\n包含'Sport'标签的交易:")
print(df[df['Tags'].apply(lambda x: 'Sport' in x)])

print("\n每个标签的平均支出:")
tag_expenses = df[df['Amount'] < 0].explode('Tags')
print(tag_expenses.groupby('Tags')['Amount'].mean().abs())