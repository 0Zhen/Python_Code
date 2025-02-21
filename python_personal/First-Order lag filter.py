import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def first_order_lag_filter(input_signal, k_coeff):
    """
    Implement first-order lag filter
    input_signal: input signal array
    k_coeff: filter coefficient (0 < k_coeff < 1)
    """
    output_signal = np.zeros_like(input_signal)
    output_signal[0] = input_signal[0]  # Initial value

    for i in range(1, len(input_signal)):
        # Y[n] = Y[n-1] + Kc * (X[n] - Y[n-1])
        output_signal[i] = output_signal[i - 1] + k_coeff * (input_signal[i] - output_signal[i - 1])

    return output_signal


def windows_average(input_signal, window_size):
    output_signal = np.zeros_like(input_signal)
    window_sum = 0

    # 處理前 window_size 個元素
    for i in range(window_size):
        window_sum += input_signal[i]
        output_signal[i] = window_sum / (i + 1)

    # 處理剩餘元素
    for i in range(window_size, len(input_signal)):
        window_sum = window_sum - input_signal[i - window_size] + input_signal[i]
        output_signal[i] = window_sum / window_size

    return output_signal


# Generate test signal
t = np.linspace(0, 10, 1000)  # 10 seconds, 1000 samples
# Generate sine wave with noise
clean_signal = np.sin(2 * np.pi * 0.5 * t)  # 0.5 Hz sine wave
noise = np.random.normal(0, 0.3, len(t))  # Add Gaussian noise
noisy_signal = clean_signal + noise

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
plt.subplots_adjust(bottom=0.25)  # Make room for the slider

# Plot original and noisy signals
ax1.plot(t, noisy_signal, 'gray', alpha=0.7, label='Noisy Signal')
ax1.plot(t, clean_signal, 'b', label='Original Signal')
ax1.set_title('Original vs Noisy Signal')
ax1.grid(True)
ax1.legend()

# Initial filter coefficient and window size
initial_k = 0.1
initial_w = 3
filtered_signal = first_order_lag_filter(noisy_signal, initial_k)
window_signal = windows_average(noisy_signal, initial_w)

# Plot filtered signals
line_filtered, = ax2.plot(t, filtered_signal, 'r', label=f'Filtered')
line_windowed, = ax2.plot(t, window_signal, 'green', label=f'Windowed')
ax2.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')
ax2.set_title(f'Filtered Signals (k={initial_k:.2f}, w={initial_w})')
ax2.grid(True)
ax2.legend()

# Create sliders
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])  # [left, bottom, width, height]
k_slider = Slider(
    ax=slider_ax,
    label='Filter Coefficient (k)',
    valmin=0.01,
    valmax=1.0,
    valinit=initial_k,
    color='red'
)

slider_bx = plt.axes([0.2, 0.05, 0.6, 0.03])  # 注意這裡的位置改變了
w_slider = Slider(
    ax=slider_bx,
    label='Window Size (w)',
    valmin=1,
    valmax=20,
    valinit=initial_w,
    valstep=1,  # 這裡設置步長為1，確保只能選擇整數
    color='green'
)


# Update function for slider
def update(val):
    k = k_slider.val
    w = int(w_slider.val)  # 確保窗口大小是整數

    filtered = first_order_lag_filter(noisy_signal, k)
    windowed = windows_average(noisy_signal, w)

    line_filtered.set_ydata(filtered)
    line_windowed.set_ydata(windowed)

    ax2.set_title(f'Filtered Signals (k={k:.2f}, w={w})')
    fig.canvas.draw_idle()


# Register the update function with both sliders
k_slider.on_changed(update)
w_slider.on_changed(update)

plt.show()