import sounddevice as sd
from scipy.io.wavfile import write

#
def rec(secs):
    fs = 44100 #standard frequency for audio
    secs = int(secs)
    if secs > 0 :

        sound_record = sd.rec(int(secs * fs), fs, dtype = 'float64', channels = 2)
        # this turns our record int a file
        write('C:/Users/MONOUSO/Desktop/newrec.wav', fs, sound_record)
    return

rec(20)