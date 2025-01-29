

import sounddevice as sd
from scipy.io.wavfile import write, read


def voiceRecording(duration: int):
    frequency = 44100

    print("recording...")
    recording = sd.rec(int(frequency*duration),
                       samplerate=frequency, channels=1)
    sd.wait()
    write("output.wav", frequency, recording)

    return "recodring saved"


def playRecording(filename: str):
    frequency, recording = read(filename)
    print("playing recording...")
    sd.play(recording, samplerate=frequency)
    sd.wait()
    return "recording finished"


test = voiceRecording(5)
print(test)

output = playRecording("output.wav")
print(output)
