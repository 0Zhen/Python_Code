import pandas as pd
import re
# 讀取Excel檔案
dff = pd.read_excel("D:\ChrisLee\personal\Chris\Personal Git\Code\python_personal\EC.xlsx")



df = pd.read_excel("EC.xlsx",sheet_name="Assistive Part")
result = {}
for error_code in df['Error Code'].unique():
    # 取得該error code的所有資料
    error_data = df[df['Error Code'] == error_code]

    # 創建新的資料結構
    result[error_code] = {
        'pedal': error_data[error_data['Assistive Part'] == 'pedal']['Status'].iloc[0],
        'motion': error_data[error_data['Assistive Part'] == 'motion']['Status'].iloc[0],
        'throttle': error_data[error_data['Assistive Part'] == 'throttle']['Status'].iloc[0]
    }

# 轉換成DataFrame
new_df = pd.DataFrame.from_dict(result, orient='index')
new_df.index.name = 'Error_Code'
new_df.reset_index(inplace=True)


merged_df = pd.merge(dff, new_df, on='Error_Code', how='left')

# 顯示結果
print(merged_df)

columns_to_replace = ['pedal', 'motion', 'throttle']
merged_df[columns_to_replace] = merged_df[columns_to_replace].replace('off','\\off')
merged_df[columns_to_replace] = merged_df[columns_to_replace].replace('on','\\on')
merged_df[columns_to_replace] = merged_df[columns_to_replace].replace('not_affected','\\NA')


print(merged_df.columns)
merged_df.to_excel('export.xlsx',index = False)
print('ok')

def clean_text(text):
    if isinstance(text, str):
        # 移除 x000D_ 和其他特殊字元
        cleaned = text.replace('_x000D_', '').replace('\r', '').replace('\n', '').replace('_',' ')
        # 只保留英文、數字、空格和基本標點符號
        cleaned = re.sub(r'[^a-zA-Z0-9\s\.,_\\]', '', cleaned)
        # 移除多餘的空格
        cleaned = ' '.join(cleaned.split())
        return cleaned
    return text

# 清理DataFrame中的所有文字
for column in merged_df.columns:
    merged_df[column] = merged_df[column].apply(clean_text)

def to_latex_format(row):
    return (
        "\\etable{\n"
        f"    name={{{row['Error Type'].title()}}},\n"
        f"    code={{{row['Error_Code']}}},\n"
        f"    type={{\\error}},\n"
        f"    pedal={{{row['pedal']}}},\n"
        f"    motion={{{row['motion']}}},\n"
        f"    throttle={{{row['throttle']}}},\n"
        f"    category={{{row['Category']}}},\n"
        f"    hradangerlevel={{{row['HRA Danger Level']}}},\n"
        f"    description={{{row['Error Description']}}},\n"
        f"    triggerconditioncode={{{row['Condition']}}}\n"
        "}\n"
        "\n"
    )

first_row = merged_df.iloc[0]
print(to_latex_format(first_row))

# 將每一行轉換成LaTeX格式並儲存到檔案
with open('error_table.txt', 'w', encoding='utf-8') as f:
    for index, row in merged_df.iterrows():
        latex_text = to_latex_format(row)
        f.write(latex_text)
        f.write('\n')  # 在每個項目之間加入空行

print("已儲存成LaTeX格式！")