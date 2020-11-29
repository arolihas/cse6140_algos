import matplotlib.pyplot as plt

x1 = [15.07,15.87,16.86,17.12,17.16,19.4,20.51,23.13,28.02,28.74]
x2 = [12.41,12.82,13.04,14.04,14.29,14.48,14.54,16.13,18.55,22.61]
x3 = [9.37,10.6,10.85,10.94,11.11,11.93,12.16,12.77,13.16,19.88]
x4 = [7.93,8.83,8.94,9.77,10.18,10.67,11.23,11.33,11.41,19.05]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'r', label='q*=0.2%')
plt.plot(x2, y, 'g', label='q*=0.4%')
plt.plot(x3, y, 'b', label='q*=0.6%')
plt.plot(x4, y, 'y', label='q*=0.8%')
plt.xlabel('run-time [CPU sec]')
plt.ylabel('P(solve)')
plt.title('LS1 power.graph QRTD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

import matplotlib.pyplot as plt

x1 = [415.38,509.38,532.94,539.66,552.91,582.8,583.28,583.89,583.95,598.74]
x2 = [399.92,492.44,520.23,527.57,538.22,567.41,570.23,571.39,573.87,583.21]
x3 = [381.98,476.06,507.59,510.33,521.92,548.04,549.05,553.85,561.08,569.26]
x4 = [365.24,494.42,504.05,522.42,556.8,458.15,496.79,534.17,531.25,548]
x4.sort()
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'r', label='q*=1.85%')
plt.plot(x2, y, 'g', label='q*=2.0%')
plt.plot(x3, y, 'b', label='q*=2.15%')
plt.plot(x4, y, 'y', label='q*=2.30%')
plt.xlabel('run-time [CPU sec]')
plt.ylabel('P(solve)')
plt.title('LS1 star2.graph QRTD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

import matplotlib.pyplot as plt

x1 = [511.02,404.42,351.35,547.54,462.25,437.25,258.18,449.83,445.6,360.42]
x1.sort()
x2 = [303.65,303.63,170.67,349.54,338.49,315.08,330.53,291.88,280.82,358.3]
x2.sort()
x3 = [285.33,244.26,320.13,215.26,245.84,249.58,286.71,282.34,117.83,279.14]
x3.sort()
x4 = [207.43,206.98,90.97,206.19,210,164.67,175.32,294.6,216.95,199.55]
x4.sort()
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'r', label='q*=0.5%')
plt.plot(x2, y, 'g', label='q*=0.7%')
plt.plot(x3, y, 'b', label='q*=0.9%')
plt.plot(x4, y, 'y', label='q*=1.1%')
plt.xlabel('run-time [CPU sec]')
plt.ylabel('P(solve)')
plt.title('LS2 power.graph QRTD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

import matplotlib.pyplot as plt

x1 = np.array([330.06,365.63,372.01,416.59,431,481.52,510.58,516.43,516.95,564.96])
x2 = [259.71,339.23,295.73,206.18,392.52,300.75,249.2,340.16,385.92,329.63]
x2.sort()
x3 = [165.8,180.42,199.23,231.14,240.27,240.3,255.18,258.39,261.72,343.52]
x4 = [79.83,110.11,120.92,124.23,141.57,147.45,147.68,150.19,169.97,200.04]
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot(x1, y, 'r', label='q*=6.5%')
plt.plot(x2, y, 'g', label='q*=6.7%')
plt.plot(x3, y, 'b', label='q*=6.8%')
plt.plot(x4, y, 'y', label='q*=6.9%')
plt.xlabel('run-time [CPU sec]')
plt.ylabel('P(solve)')
plt.title('LS2 star2.graph QRTD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

import matplotlib.pyplot as plt
x1 = sorted([62,62,62,62,63,63,62,63,64,62])
x2 = sorted([35,50,42,39,43,47,36,40,41,35])
x3 = sorted([19,41,23,21,25,24,18,19,21,15])
x4 = sorted([8,15,5,7,9,5,6,9,6,6])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(2200+x-2203)/2203 for x in x1], y, 'r', label='t=0.5s')
plt.plot([(2200+x-2203)/2203 for x in x2], y, 'b', label='t=5s')
plt.plot([(2200+x-2203)/2203 for x in x3], y, 'g', label='t=10s')
plt.plot([(2200+x-2203)/2203 for x in x4], y, 'y', label='t=20s')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('LS1 power.graph SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

x1 = sorted([41,56,50,51,61,56,56,53,57,57])
x2 = sorted([23,96,74,63,17,88,94,87,100,94])
x3 = sorted([48,15,103,89,45,97,16,16,23,25])
x4 = sorted([76,122,131,140,153,115,126,144,142,150])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(4800+x-4542)/4542 for x in x1], y, 'r', label='t=30s')
plt.plot([(4700+x-4542)/4542 for x in x2], y, 'b', label='t=180s')
plt.plot([(4600+x-4542)/4542 for x in x3], y, 'g', label='t=360s')
plt.plot([(4500+x-4542)/4542 for x in x4], y, 'y', label='t=540s')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('LS1 star2.graph SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

x1 = sorted([60,58,58,56,58,54,53,61,60,57])
x2 = sorted([51,52,47,51,52,37,42,50,51,48])
x3 = sorted([33,27,29,36,31,18,26,31,33,30])
x4 = sorted([18,17,13,18,16,10,15,17,18,15])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(2200+x-2203)/2203 for x in x1], y, 'r', label='t=30s')
plt.plot([(2200+x-2203)/2203 for x in x2], y, 'b', label='t=60s')
plt.plot([(2200+x-2203)/2203 for x in x3], y, 'g', label='t=180s')
plt.plot([(2200+x-2203)/2203 for x in x4], y, 'y', label='t=360s')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('LS2 power.graph SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

x1 = sorted([56,58,58,57,58,58,58,58,58,58])
x2 = sorted([49,51,55,52,54,55,54,56,54,53])
x3 = sorted([40,34,45,45,50,48,40,46,46,38])
x4 = sorted([27,19,30,35,40,34,26,35,32,13])
y = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]

plt.plot([(4800+x-4542)/4542 for x in x1], y, 'r', label='t=0.5s')
plt.plot([(4800+x-4542)/4542 for x in x2], y, 'b', label='t=10s')
plt.plot([(4800+x-4542)/4542 for x in x3], y, 'g', label='t=5s')
plt.plot([(4800+x-4542)/4542 for x in x4], y, 'y', label='t=20')
plt.xlabel('relative solution quality [%]')
plt.ylabel('P(solve)')
plt.title('LS2 star2.graph SQD')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)