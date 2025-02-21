import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def first_order_lag_filter(input_signal, k_coeff):
    """First-order lag filter"""
    output_signal = np.zeros_like(input_signal)
    output_signal[0] = input_signal[0]

    for i in range(1, len(input_signal)):
        output_signal[i] = output_signal[i - 1] + k_coeff * (input_signal[i] - output_signal[i - 1])

    return output_signal


def double_first_order_lag_filter(input_signal, k1, k2):
    """Double first-order lag filter (equivalent to second-order)"""
    first_filtered = first_order_lag_filter(input_signal, k1)
    second_filtered = first_order_lag_filter(first_filtered, k2)
    return second_filtered


def windows_average(input_signal, window_size):
    """Moving average filter"""
    output_signal = np.zeros_like(input_signal)
    window_sum = 0

    for i in range(window_size):
        window_sum += input_signal[i]
        output_signal[i] = window_sum / (i + 1)

    for i in range(window_size, len(input_signal)):
        window_sum = window_sum - input_signal[i - window_size] + input_signal[i]
        output_signal[i] = window_sum / window_size

    return output_signal


def windows_then_first_order(input_signal, window_size, k):
    """Moving average followed by first-order lag filter"""
    window_filtered = windows_average(input_signal, window_size)
    final_filtered = first_order_lag_filter(window_filtered, k)
    return final_filtered


# Generate test signal
t = np.linspace(0, 10, 1000)  # 10 seconds, 1000 samples
clean_signal = np.sin(2 * np.pi * 0.5 * t)  # 0.5 Hz sine wave
noise = np.random.normal(0, 0.3, len(t))  # Add Gaussian noise
noisy_signal = clean_signal + noise

# Create figure
fig = plt.figure(figsize=(15, 10))
gs = plt.GridSpec(3, 1, height_ratios=[1, 1, 1], hspace=0.4)
plt.subplots_adjust(bottom=0.25)

# Upper subplot: Original signal
ax1 = fig.add_subplot(gs[0])
ax1.plot(t, noisy_signal, 'gray', alpha=0.7, label='Noisy Signal')
ax1.plot(t, clean_signal, 'b', label='Original Signal')
ax1.set_title('Original vs Noisy Signal')
ax1.grid(True)
ax1.legend()

# Middle subplot: Single method filtering
ax2 = fig.add_subplot(gs[1])
ax2.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')

# Lower subplot: Combined method filtering
ax3 = fig.add_subplot(gs[2])
ax3.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')

# Initial parameters
initial_k = 0.1
initial_k2 = 0.1
initial_w = 3

# Calculate initial filtered signals
first_order_signal = first_order_lag_filter(noisy_signal, initial_k)
window_signal = windows_average(noisy_signal, initial_w)
double_filtered = double_first_order_lag_filter(noisy_signal, initial_k, initial_k2)
combined_filtered = windows_then_first_order(noisy_signal, initial_w, initial_k)

# Plot filtered signals
line_first, = ax2.plot(t, first_order_signal, 'r', label=f'First-Order (k={initial_k})')
line_window, = ax2.plot(t, window_signal, 'g', label=f'Moving Average (w={initial_w})')
ax2.set_title('Single Filter Method Comparison')
ax2.grid(True)
ax2.legend()

line_double, = ax3.plot(t, double_filtered, 'r', label=f'Second-Order (k1={initial_k}, k2={initial_k2})')
line_combined, = ax3.plot(t, combined_filtered, 'g', label=f'MA + First-Order (w={initial_w}, k={initial_k})')
ax3.set_title('Combined Filter Method Comparison')
ax3.grid(True)
ax3.legend()

# Create sliders
slider_k = plt.axes([0.2, 0.15, 0.6, 0.02])
k_slider = Slider(ax=slider_k, label='First-Order Coefficient (k)', valmin=0.01, valmax=1.0, valinit=initial_k,
                  color='red')

slider_k2 = plt.axes([0.2, 0.11, 0.6, 0.02])
k2_slider = Slider(ax=slider_k2, label='Second-Order Coefficient (k2)', valmin=0.01, valmax=1.0, valinit=initial_k2,
                   color='blue')

slider_w = plt.axes([0.2, 0.07, 0.6, 0.02])
w_slider = Slider(ax=slider_w, label='Window Size (w)', valmin=1, valmax=20, valinit=initial_w, valstep=1,
                  color='green')


# Update function
def update(val):
    k = k_slider.val
    k2 = k2_slider.val
    w = int(w_slider.val)

    # Update all filtered signals
    first_order_signal = first_order_lag_filter(noisy_signal, k)
    window_signal = windows_average(noisy_signal, w)
    double_filtered = double_first_order_lag_filter(noisy_signal, k, k2)
    combined_filtered = windows_then_first_order(noisy_signal, w, k)

    # Update plots
    line_first.set_ydata(first_order_signal)
    line_window.set_ydata(window_signal)
    line_double.set_ydata(double_filtered)
    line_combined.set_ydata(combined_filtered)

    # Update labels
    line_first.set_label(f'First-Order (k={k:.2f})')
    line_window.set_label(f'Moving Average (w={w})')
    line_double.set_label(f'Second-Order (k1={k:.2f}, k2={k2:.2f})')
    line_combined.set_label(f'MA + First-Order (w={w}, k={k:.2f})')

    # Update legends
    ax2.legend()
    ax3.legend()

    fig.canvas.draw_idle()


# Register slider updates
k_slider.on_changed(update)
k2_slider.on_changed(update)
w_slider.on_changed(update)

plt.show()