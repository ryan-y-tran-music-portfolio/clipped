from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd


def create_sine_wav(sample_rate: int, frequency: int) -> None:
    """Creates a sine.wav WAV File in the current directory.
    Args:
        sample_rate (int): Samples per Second
        frequency (int): Cycles per Second
    """

    t = np.linspace(0.0, 1.0, sample_rate, endpoint=False)
    amplitude = np.iinfo(np.int16).max // 4

    data = amplitude * np.sin(2.0 * np.pi * frequency * t)

    write("sine.wav", sample_rate, data.astype(np.int16))

    print(
        f"Created sine.wav with sample rate of {sample_rate} and frequency of {frequency}"
    )


def create_clipped_wav(sample_rate: int, frequency: int) -> None:
    """Creates a clipped.wav WAV File in the current directory.
    Args:
        sample_rate (int): Samples per Second
        frequency (int): Cycles per Second
    """

    t = np.linspace(0.0, 1.0, sample_rate, endpoint=False)
    amplitude = np.iinfo(np.int16).max // 2

    data = amplitude * np.sin(2.0 * np.pi * frequency * t)

    max_sample = np.iinfo(np.int16).max // 4
    min_sample = np.iinfo(np.int16).min // 4
    clipped_data = np.clip(data, min_sample, max_sample)

    write("clipped.wav", sample_rate, clipped_data.astype(np.int16))

    print(
        f"Created clipped.wav with sample rate of {sample_rate} and frequency of {frequency}"
    )

    play_clipped_wav(clipped_data, sample_rate)


def play_clipped_wav(clipped_array: np.ndarray, sampling_rate: int) -> None:
    """Directly plays a created clipped_wav, using the clipped array.
    Args:
        clipped_array (np.ndarray): clipped_wav array
        sampling_rate (int): Samples per Second
    """
    print("Now playing clipped.wav.")
    sd.play(clipped_array, samplerate=sampling_rate)
    sd.wait()


if __name__ == "__main__":
    create_sine_wav(48000, 440)
    create_clipped_wav(48000, 440)
