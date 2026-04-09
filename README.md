# Clipped

## What did I do?

There are three main things in this project.

1. Creation of a sine wave WAV file named 'sine.wav' with the following specifications:
   1. Mono channel
   2. Sample format of 16-bit signed
   3. Amplitude of 1/4th maximum possible 16-bit amplitude
   4. Duration of one second
   5. Frequency of 440Hz
   6. Sample Rate of 48000 samples per second
2. Creation of another sine wave WAV file named 'clipped.wav,' with similar specificaitons to 'sine.wav' except:
   1. Amplitude is 1/2th maximum possible
   2. Samples are 'clipped' to 1/4th maximum amplitude.
3. 'clipped.wav' is played
   1. **Note:** 'clipped.wav' might be loud. Please play at low volume.

## How did it Go?

The creation of the file went smoothly; there were not really anything to struggle on during creation, although I had to bugtest why Sounddevice was not playing any audio. numpy made the process straightforward.

## What's next?

The way the fuctions are set up, you can really plug in any sample rate and frequency. Perhaps a small interface can be provided to the user.

## How to Build

Follow the instructions to install the uv package manager [here](https://docs.astral.sh/uv/getting-started/installation/). Then simply run this program via `uv run clipped.py`
