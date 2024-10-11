import matplotlib.pyplot as plt
import pandas as pd

# 创建原始数据框
data = {
    'Pressure (Pa)': [100, 100, 100, 90, 90, 90, 80, 80, 80, 70, 70, 70, 60, 60, 60, 50, 50, 50, 
                40, 40, 40, 30, 30, 30, 20, 20, 20, 18, 18, 18, 16, 16, 16, 14, 14, 14, 12, 
                12, 12, 10, 10, 10, 8, 8, 8, 6, 6, 6, 4, 4, 4],
    'Breakdown Voltage (V)': [795, 796, 801, 774, 772, 775, 741, 743, 738, 706, 711, 711, 669, 660, 676, 636, 
                   627, 637, 580, 573, 567, 540, 536, 529, 474, 477, 481, 476, 474, 456, 475, 
                   467, 456, 459, 450, 437, 474, 472, 478, 500, 498, 476, 554, 532, 532, 650, 
                   642, 656, 964, 843, 875]
}

# 创建 DataFrame
df = pd.DataFrame(data)

# 聚合数据，分别获取三个击穿电压及其平均值
df_grouped = df.groupby('Pressure (Pa)')['Breakdown Voltage (V)'].apply(list).reset_index()
df_grouped['Breakdown Voltage 1 (V)'] = df_grouped['Breakdown Voltage (V)'].apply(lambda x: x[0])
df_grouped['Breakdown Voltage 2 (V)'] = df_grouped['Breakdown Voltage (V)'].apply(lambda x: x[1])
df_grouped['Breakdown Voltage 3 (V)'] = df_grouped['Breakdown Voltage (V)'].apply(lambda x: x[2])
df_grouped['Average Breakdown Voltage (V)'] = df_grouped['Breakdown Voltage (V)'].apply(lambda x: sum(x) / len(x))

# 获取气压和击穿电压平均值的数据
pressure = df_grouped['Pressure (Pa)']
average_voltage = df_grouped['Average Breakdown Voltage (V)']

# 绘制图像，使用英文
plt.figure(figsize=(8, 6))
plt.plot(pressure, average_voltage, marker='o', linestyle='-', color='darkblue', label='Average Breakdown Voltage')

plt.xlabel('Pressure (Pa)')
plt.ylabel('Average Breakdown Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
