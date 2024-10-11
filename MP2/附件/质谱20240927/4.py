import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# 文件夹路径
folder_path = r'C:\Users\hll\Desktop\CO\EX\MP\MP2\附件\质谱20240927\质谱20240927'

# 设置峰的高度阈值，调整为适合数据的范围
peak_height = 2*1e-12  # 根据你的数据，将阈值设置得更小

# 创建一个保存图像的文件夹
output_folder = os.path.join(folder_path, 'output_images')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历文件夹中的所有 .xlsx 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        
        # 读取 .xls 文件，从第7行开始读取
        df = pd.read_excel(file_path, header=6)
        
        # 获取质量和amp数据
        mass = df.iloc[:, 0].dropna()
        amp = df.iloc[:, 1].dropna()
        
        # 绘制质谱图
        plt.figure(figsize=(10, 6))
        plt.plot(mass, amp, label='Mass Spectrum')

        # 绘制高度阈值线，帮助可视化
        plt.axhline(y=peak_height, color='r', linestyle='--', label='Height threshold')

        # 寻峰，调整高度参数
        peaks, _ = find_peaks(amp, height=peak_height)

        if len(peaks) > 0:
            # 标出峰的位置
            plt.plot(mass[peaks], amp[peaks], "rx", label='Peaks', markersize=8)
            for peak in peaks:
                plt.text(mass[peak], amp[peak] + 0.05 * max(amp), f'{mass[peak]:.2f}', 
                         ha='center', fontsize=10, color='blue')
        else:
            print(f"No peaks found in {file_name}")

        # 添加标题和标签
        plt.title(f'Mass Spectrum of {file_name}')
        plt.xlabel('Mass')
        plt.ylabel('Amplitude')
        plt.legend()

        # 保存图片为png，命名为对应文件名
        output_file = os.path.join(output_folder, f'{os.path.splitext(file_name)[0]}.png')
        plt.savefig(output_file)  # 保存图片为PNG格式
        
        # 清空当前图像，防止下一次循环时重叠
        plt.close()

        print(f"Saved: {output_file}")
