import pandas as pd
import numpy as np
from enum import Enum
from datetime import datetime, timedelta

Total_salary = 63000
Fixed_expenses = 10000
CTBC = 15000
Total_investment = Total_salary - Fixed_expenses - CTBC
Stock_invest_ratio = 0.25
Crypto_invest_ratio = 0.65
Bank_saving_ratio = 1 - Stock_invest_ratio - Crypto_invest_ratio
Year = 20
Stock_monthly_investment = Total_investment * Stock_invest_ratio
Crypto_monthly_investment = Total_investment * Crypto_invest_ratio
Bank_monthly_saving = Total_investment * Bank_saving_ratio
Crypto_annual_roi = 0.06
Stock_annual_roi = 0.06
Bank_annual_roi = 0.0083
class ROI(Enum):
    AnnualROI = 0
    MonthROI = 1
    DayROI = 2

def ROI_calculate(input_type: ROI, output_type: ROI, roi: float) -> float:
    if input_type == ROI.AnnualROI:
        annual_roi = roi
    elif input_type == ROI.MonthROI:
        annual_roi = (1 + roi) ** 12 - 1
    elif input_type == ROI.DayROI:
        annual_roi = (1 + roi) ** 365 - 1
    else:
        raise ValueError("Invalid input type")

    # Convert from annual ROI to desired output type
    if output_type == ROI.AnnualROI:
        result =  annual_roi
    elif output_type == ROI.MonthROI:
        result =  (1 + annual_roi) ** (1/12) - 1
    elif output_type == ROI.DayROI:
        result =  (1 + annual_roi) ** (1/365) - 1
    else:
        raise ValueError("Invalid output type")

    return f"{result:.{6}f}"


start_date = datetime.now().replace(day=1)
date_range = [start_date + timedelta(days=30*i) for i in range(Year*12)]
Crypto_assets = []
Crypto_monthly_roi = float(ROI_calculate(ROI.AnnualROI,ROI.MonthROI,Crypto_annual_roi))
print("month_roi=",Crypto_monthly_roi)
temp = 0
for i in range(Year*12):
    temp = temp*(1+Crypto_monthly_roi) + Crypto_monthly_investment
    Crypto_assets.append(f"{temp:.{2}f}")

df = pd.DataFrame({
    'Date':date_range,
    'Crypto':Crypto_assets
})
# 將 'Date' 列轉換為只包含年份和月份
df['Date'] = df['Date'].dt.to_period('M')

# 設置 'Date' 列為索引
df.set_index('Date', inplace=True)
# 顯示前幾行和後幾行
print(df.head())
print("\n...\n")
print(df.tail())

# 基本統計信息
print("\nBasic Statistics:")
print(df.describe())
df['Crypto'] = df['Crypto'].astype(float)
'''
# 繪製資金增長圖表
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.figure(figsize=(12, 6))
# 將索引轉換為 datetime 對象
df.index = df.index.to_timestamp()
plt.plot(df.index,  df['Crypto'])
plt.title('Crypto Growth Over 2 Year')
plt.xlabel('Year')
plt.ylabel('Crypto Amount')
plt.grid(True)

# 設置 x 軸刻度為每5年一個
years = mdates.YearLocator(1)  # 每5年一個刻度
years_fmt = mdates.DateFormatter('%Y')
plt.gca().xaxis.set_major_locator(years)
plt.gca().xaxis.set_major_formatter(years_fmt)

# 旋轉並對齊 x 軸標籤
plt.gcf().autofmt_xdate()
# 设置 y 轴的刻度
y_min = 0
print(df['Crypto'].max())
y_max = df['Crypto'].max() * 1.1  # 给最大值留一些空间
y_interval = 10000000  # 设置固定间隔
y_ticks = np.arange(y_min, y_max, y_interval)
plt.yticks(y_ticks, [f'${y:,.0f}' for y in y_ticks])
plt.tight_layout()
plt.show()
'''
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# 確保日期格式正確
df.index = df.index.to_timestamp()

# 創建圖表
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 添加 Crypto 曲線
fig.add_trace(
    go.Scatter(x=df.index, y=df['Crypto'], name="Crypto Value"),
    secondary_y=False,
)

# 設置 x 軸
fig.update_xaxes(
    title_text="Year",
    tickformat="%Y",
    dtick="M12"  # 每5年顯示一次刻度
)

# 設置 y 軸
fig.update_yaxes(
    title_text="Crypto Amount ($)",
    secondary_y=False,
    tickformat="$,.0f",
    hoverformat="$,.2f"
)

# 更新布局
fig.update_layout(
    title_text="Crypto Growth Over %d Years"%Year,
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# 顯示圖表
fig.show()