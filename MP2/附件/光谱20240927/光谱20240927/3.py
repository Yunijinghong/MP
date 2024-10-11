
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter

# 设置文件夹路径
folder_path = r'C:\Users\hll\Desktop\CO\EX\MP\MP2\附件\光谱20240927\光谱20240927'  # 替换为你的实际路径
os.chdir(folder_path)

# 获取文件夹中所有txt文件
files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

# 设置忽略的峰值高度阈值
peak_height_threshold = 100 # 你可以根据实际数据调整这个值

# 遍历每个txt文件
for file in files:
    # 读取文件数据
    file_path = os.path.join(folder_path, file)
    data = np.loadtxt(file_path)
    
    # 第一列是频率，第二列是强度
    frequency = data[:, 0]
    intensity = data[:, 1]
    
    # 对数据进行滤波 (Savgol filter, window size=11, poly order=3)
    smoothed_intensity = savgol_filter(intensity, window_length=11, polyorder=3)
    
    # 寻找滤波后数据的峰值，忽略较矮的峰
    peaks, properties = find_peaks(smoothed_intensity, height=peak_height_threshold)
    
    # 创建图像
    plt.figure(figsize=(10, 6))
    
    # 绘制原始数据
    plt.plot(frequency, intensity, label='Original Spectrum', linestyle='--', color='gray')
    
    # 绘制滤波后的数据
    plt.plot(frequency, smoothed_intensity, label='Smoothed Spectrum', color='blue')
    
    # 标记峰值
    plt.plot(frequency[peaks], smoothed_intensity[peaks], 'rx', label='Peaks')
    
    # 在峰值位置标记具体的数值
    for peak in peaks:
        plt.text(frequency[peak], smoothed_intensity[peak], f'{frequency[peak]:.2f}', 
                 horizontalalignment='center', verticalalignment='bottom', color='red')
    
    # 图像设置
   
    plt.xlabel('Frequency')
    plt.ylabel('Intensity')
    plt.legend()
    plt.grid(True)
    
    # 保存图像，使用文件名
    plt.savefig(os.path.join(folder_path, f"{file}_spectrum_filtered.png"))
    plt.close()  # 关闭当前图像，避免显示过多图像
