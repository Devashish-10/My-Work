import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 1, 1000)  # 1 second with 1000 time points

# Frequency and amplitude pairs
frequency_amplitude_pairs = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

# Initialize the signal
signal = np.zeros_like(t)

# Create the signal by summing sine waves with different frequencies and amplitudes
for freq, amp in frequency_amplitude_pairs:
    signal += amp * np.sin(2 * np.pi * freq * t)

# Plot the time-domain signal
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Time Domain Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Perform the FFT
fft_result = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(t), 1.0 / 1000)  # Frequency values in Hz

# Plot the frequency-domain representation
plt.subplot(2, 1, 2)
plt.plot(fft_freqs, np.abs(fft_result))
plt.title('Frequency Domain Signal (FFT)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.xlim(0, 4)  # Set the x-axis limit to visualize frequencies up to 4 Hz

plt.tight_layout()
plt.show()
