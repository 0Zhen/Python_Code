import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def first_order_filter(input_signal, k):
    """First-order low-pass filter"""
    output = np.zeros_like(input_signal)
    output[0] = input_signal[0]

    for i in range(1, len(input_signal)):
        output[i] = output[i - 1] + k * (input_signal[i] - output[i - 1])
    return output


def second_order_filter(input_signal, f0, damp):
    """Second-order low-pass filter"""
    output = np.zeros_like(input_signal)
    output[0] = input_signal[0]
    output[1] = input_signal[1]

    omega = 2 * np.pi * f0
    dt = 0.01
    alpha = omega * dt
    beta = damp * omega * dt

    a1 = 2.0 - beta
    a2 = beta - 1.0
    b0 = alpha * alpha / 2.0
    b1 = alpha * alpha
    b2 = alpha * alpha / 2.0

    scale = 1.0 / (1.0 + beta + alpha * alpha)
    a1 *= scale
    a2 *= scale
    b0 *= scale
    b1 *= scale
    b2 *= scale

    for i in range(2, len(input_signal)):
        output[i] = (a1 * output[i - 1] +
                     a2 * output[i - 2] +
                     b0 * input_signal[i] +
                     b1 * input_signal[i - 1] +
                     b2 * input_signal[i - 2])
    return output


# Generate test signal
t = np.linspace(0, 10, 1000)
clean_signal = np.sin(2 * np.pi * 0.5 * t) + 0.5 * np.sin(2 * np.pi * 2 * t)
noise = np.random.normal(0, 0.3, len(t))
noisy_signal = clean_signal + noise

# Create figure and subplots with adjusted size and spacing
fig = plt.figure(figsize=(14, 12))
plt.subplots_adjust(left=0.1, right=0.95, bottom=0.35, top=0.95, hspace=0.4)

ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

# Plot original signals
ax1.plot(t, noisy_signal, 'gray', alpha=0.7, label='Noisy Signal')
ax1.plot(t, clean_signal, 'b', label='Original Signal')
ax1.set_title('Original vs Noisy Signal', pad=20)
ax1.grid(True)
ax1.legend()

# Initial parameters
initial_k = 0.1
initial_f0 = 0.5
initial_damp = 0.707

# Calculate initial filtered results
first_order_output = first_order_filter(noisy_signal, initial_k)
second_order_output = second_order_filter(noisy_signal, initial_f0, initial_damp)

# Plot filtered results
line_first, = ax2.plot(t, first_order_output, 'r', label=f'First-order Filter (k={initial_k})')
ax2.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')
ax2.set_title(f'First-order Filter Output (k={initial_k})', pad=20)
ax2.grid(True)
ax2.legend()

line_second, = ax3.plot(t, second_order_output, 'g', label=f'Second-order Filter (f0={initial_f0}, ζ={initial_damp})')
ax3.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')
ax3.set_title(f'Second-order Filter Output (f0={initial_f0}, ζ={initial_damp})', pad=20)
ax3.grid(True)
ax3.legend()

# Create sliders
slider_k_ax = plt.axes([0.2, 0.22, 0.6, 0.03])
slider_f0_ax = plt.axes([0.2, 0.15, 0.6, 0.03])
slider_damp_ax = plt.axes([0.2, 0.08, 0.6, 0.03])

k_slider = Slider(slider_k_ax, 'First-order Coefficient (k)', 0.01, 1.0, valinit=initial_k)
f0_slider = Slider(slider_f0_ax, 'Second-order Cutoff Freq (f0)', 0.1, 2.0, valinit=initial_f0)
damp_slider = Slider(slider_damp_ax, 'Second-order Damping (ζ)', 0.1, 2.0, valinit=initial_damp)


# Update function
def update(val):
    # Get current slider values
    k = k_slider.val
    f0 = f0_slider.val
    damp = damp_slider.val

    # Recalculate filtered results
    first_filtered = first_order_filter(noisy_signal, k)
    second_filtered = second_order_filter(noisy_signal, f0, damp)

    # Update plots
    line_first.set_ydata(first_filtered)
    line_second.set_ydata(second_filtered)
    ax2.set_title(f'First-order Filter Output (k={k:.3f})', pad=20)
    ax3.set_title(f'Second-order Filter Output (f0={f0:.3f}, ζ={damp:.3f})', pad=20)

    fig.canvas.draw_idle()


# Register update function
k_slider.on_changed(update)
f0_slider.on_changed(update)
damp_slider.on_changed(update)

plt.show()