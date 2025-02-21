import pandas as pd
import numpy as np
from enum import Enum
from datetime import datetime, timedelta
import plotly.graph_objs as go
from plotly.subplots import make_subplots

Total_salary = 63000
Fixed_expenses = 10000
CTBC = 15000
Stock_invest_ratio = 0.25
Crypto_invest_ratio = 0.65
Year = 2

Crypto_annual_roi = 0.1
Stock_annual_roi = 0.06
Bank_annual_roi = 0.0083
yaxis_uint = 10000000

Total_investment = Total_salary - Fixed_expenses - CTBC
Bank_saving_ratio = 1 - Stock_invest_ratio - Crypto_invest_ratio
Stock_monthly_investment = Total_investment * Stock_invest_ratio
Crypto_monthly_investment = Total_investment * Crypto_invest_ratio
Bank_monthly_saving = Total_investment * Bank_saving_ratio
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
Stock_assests = []
Bank_assests = []
Total_assests = []
Crypto_monthly_roi = float(ROI_calculate(ROI.AnnualROI,ROI.MonthROI,Crypto_annual_roi))
Stock_monthly_roi = float(ROI_calculate(ROI.AnnualROI, ROI.MonthROI,Stock_annual_roi))
Bank_monthly_roi = float(ROI_calculate(ROI.AnnualROI,ROI.MonthROI,Bank_annual_roi))
Crytpo_temp = 0
Stock_temp = 0
Bank_temp = 0
Total_assests_temp = 0

for i in range(Year*12):
    Crytpo_temp = Crytpo_temp*(1+Crypto_monthly_roi) + Crypto_monthly_investment
    Crypto_assets.append(f"{Crytpo_temp:.{0}f}")

    Stock_temp = Stock_temp*(1+Stock_monthly_roi) + Stock_monthly_investment
    Stock_assests.append(f"{Stock_temp:.{0}f}")

    Bank_temp = Bank_temp *(1 + Bank_monthly_roi) + Bank_monthly_saving
    Bank_assests.append(f"{Bank_temp:.{0}f}")

    Total_temp = Crytpo_temp+Stock_temp+Bank_temp
    Total_assests.append(f"{Total_temp:.{0}f}")

df = pd.DataFrame({
    'Date':date_range,
    'Crypto':Crypto_assets,
    'Stock':Stock_assests,
    'Bank':Bank_assests,
    'Total_assests':Total_assests
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
df['Stock'] = df['Stock'].astype(float)
df['Bank'] = df['Bank'].astype(float)
df['Total_assests'] = df['Total_assests'].astype(float)




# 確保日期格式正確
df.index = df.index.to_timestamp()

# 創建圖表
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 添加 Crypto 曲線
fig.add_trace(
    go.Scatter(x=df.index, y=df['Crypto'], name=f"Crypto Value, Annual ROI={Crypto_annual_roi:.2%}"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df.index, y=df['Stock'], name=f"Stock Value, Annual ROI={Stock_annual_roi:.2%}"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df.index, y=df['Bank'], name=f"Bank Value, Annual ROI={Bank_annual_roi:.2%}"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df.index, y=df['Total_assests'], name="Total Value"),
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
    title_text="Assets Amount ($)",
    secondary_y=False,
    dtick=yaxis_uint,
    tickformat="$d",#"$,.0f",
    hoverformat="$d"#"$,.2f"
)

# 更新布局
fig.update_layout(
    title_text="Assets Growth Over %d Years"%Year,
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# 顯示圖表
fig.show()