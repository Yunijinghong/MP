import matplotlib.pyplot as plt

# 数据
time = [26, 36, 46, 56, 66, 76, 85, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 
        360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720,
        740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980, 1000, 1020, 1040, 1060, 1080, 
        1100, 1120, 1140, 1160, 1180, 1200, 1220, 1240, 1260, 1280, 1300, 1320, 1340, 1360, 1380, 1400, 
        1420, 1440, 1460, 1480, 1500, 1520, 1540, 1560, 1580, 1600, 1620, 1640, 1660, 1680, 1700, 1720, 
        1740, 1760, 1780, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960]

pressure = [8.10E+01, 2.00E+01, 1.40E+01, 1.10E+01, 9.80E+00, 8.80E+00, 7.80E+00, 6.90E+00, 6.00E+00,
            5.30E+00, 4.80E+00, 4.40E+00, 4.00E+00, 3.70E+00, 3.50E+00, 3.30E+00, 3.10E+00, 2.90E+00, 
            2.80E+00, 2.60E+00, 2.50E+00, 2.40E+00, 7.20E-01, 2.00E-01, 6.90E-02, 3.80E-02, 3.30E-02,
            2.60E-02, 2.10E-02, 1.60E-02, 1.20E-02, 9.80E-03, 8.20E-03, 6.90E-03, 6.10E-03, 4.90E-03, 
            4.70E-03, 4.40E-03, 4.40E-03, 4.20E-03, 4.10E-03, 3.90E-03, 3.80E-03, 3.70E-03, 3.50E-03, 
            3.40E-03, 3.30E-03, 3.20E-03, 3.10E-03, 3.10E-03, 3.00E-03, 2.90E-03, 2.80E-03, 2.70E-03, 
            2.60E-03, 2.60E-03, 2.50E-03, 2.30E-03, 2.30E-03, 2.20E-03, 2.20E-03, 2.20E-03, 2.20E-03, 
            2.20E-03, 2.20E-03, 2.10E-03, 2.10E-03, 2.10E-03, 2.10E-03, 2.20E-03, 2.20E-03, 2.30E-03, 
            2.40E-03, 2.50E-03, 2.80E-03, 3.20E-03, 3.70E-03, 4.60E-03, 7.00E-03, 1.90E-02, 3.20E-02, 
            4.10E-02, 5.00E-02, 1.00E-01, 1.70E-01, 2.40E+00, 2.60E+00, 2.80E+00, 3.10E+00, 3.30E+00,
            3.50E+00, 3.70E+00, 3.80E+00, 4.00E+00, 4.20E+00, 4.40E+00, 4.60E+00, 4.80E+00, 5.00E+00,
            5.20E+00, 5.40E+00]

# 绘制图像
plt.figure(figsize=(10, 6))
plt.plot(time, pressure, marker='o', linestyle='-', color='b')

plt.xlabel('Time (S)')
plt.ylabel('Pressure(pa)')
plt.grid(True)

# 显示图像
plt.show()


