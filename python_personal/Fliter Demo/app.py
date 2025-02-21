import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Filter Demo", layout="wide")


@st.cache_data
def generate_signal(t):
    """Generate test signal with noise"""
    clean_signal = np.sin(2 * np.pi * 0.5 * t) + 0.5 * np.sin(2 * np.pi * 2 * t)
    noise = np.random.normal(0, 0.3, len(t))
    return clean_signal, clean_signal + noise


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


# Set page title
st.title('Filter Demo')
st.write('This demo shows the effects of first-order and second-order low-pass filters on a noisy signal.')

# Sidebar controls
st.sidebar.header('Filter Parameters')

# First-order filter parameter
k = st.sidebar.slider('First-order Coefficient (k)',
                      min_value=0.01,
                      max_value=1.0,
                      value=0.1,
                      step=0.01)

# Second-order filter parameters
f0 = st.sidebar.slider('Second-order Cutoff Freq (f0)',
                       min_value=0.1,
                       max_value=2.0,
                       value=0.5,
                       step=0.1)

damp = st.sidebar.slider('Second-order Damping (ζ)',
                         min_value=0.1,
                         max_value=2.0,
                         value=0.707,
                         step=0.1)

# Generate test signal
t = np.linspace(0, 10, 1000)
clean_signal, noisy_signal = generate_signal(t)

# Calculate filtered signals
first_order_output = first_order_filter(noisy_signal, k)
second_order_output = second_order_filter(noisy_signal, f0, damp)

# Create plots
fig = plt.figure(figsize=(12, 12))

# Original vs Noisy Signal
plt.subplot(311)
plt.plot(t, noisy_signal, 'gray', alpha=0.7, label='Noisy Signal')
plt.plot(t, clean_signal, 'b', label='Original Signal')
plt.title('Original vs Noisy Signal')
plt.grid(True)
plt.legend()

# First-order Filter Output
plt.subplot(312)
plt.plot(t, first_order_output, 'r', label=f'First-order Filter (k={k:.3f})')
plt.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')
plt.title(f'First-order Filter Output (k={k:.3f})')
plt.grid(True)
plt.legend()

# Second-order Filter Output
plt.subplot(313)
plt.plot(t, second_order_output, 'g', label=f'Second-order Filter (f0={f0:.3f}, ζ={damp:.3f})')
plt.plot(t, noisy_signal, 'gray', alpha=0.3, label='Noisy Signal')
plt.title(f'Second-order Filter Output (f0={f0:.3f}, ζ={damp:.3f})')
plt.grid(True)
plt.legend()

plt.tight_layout()
st.pyplot(fig)