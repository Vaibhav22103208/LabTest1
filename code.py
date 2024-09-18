import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


np.random.seed(42)  
totalMinutes = 1440

traffic_data = np.random.randint(10, 50, size= totalMinutes)

print(f"Traffic data: {traffic_data}")



noise = np.random.randint(-5, 6, totalMinutes)
noisy_traffic_data = traffic_data + noise

print(f"\nNoisy traffic data would be: {noisy_traffic_data}")


b, a = signal.butter(3, 0.05)
smoothed_traffic_data = signal.filtfilt(b, a, noisy_traffic_data)

print(f"\nSmooth traffic data would be: {smoothed_traffic_data}")


hourly_averages = np.mean(smoothed_traffic_data.reshape(24, 60), axis=1)

print(f"\nHourly averages would be: {hourly_averages}")


time = np.arange(0, totalMinutes)


plt.figure(figsize=(12, 6))


plt.plot(time, noisy_traffic_data, label='Noisy Data', alpha=0.5)

plt.plot(time, smoothed_traffic_data, label='Smoothed Data', linewidth=2)


hourly_time = np.arange(0, totalMinutes, 60)
plt.scatter(hourly_time, hourly_averages, color='red', label='Hourly Averages', zorder=5)



high_traffic_periods = np.where(smoothed_traffic_data > 100)[0]
consecutive_periods = np.split(high_traffic_periods, np.where(np.diff(high_traffic_periods) != 1)[0] + 1)

for period in consecutive_periods:
    if len(period) > 20:
        plt.axvspan(period[0], period[-1], color='yellow', alpha=0.3, label='High Traffic (>100 for 20+ min)')

plt.xlabel('Time (minutes)')
plt.ylabel('Number of Vehicles')
plt.title('Traffic Flow Monitoring')
plt.legend()
plt.show()

