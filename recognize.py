import os
import glob
import json
import wave
from vosk import Model, KaldiRecognizer

MODEL_PATH = os.getcwd() + '/data/model'
SAMPLES_PATH = os.getcwd() + '/samples'

RATE = 8000 * 2  # hz
CHUNK = 1024 * 4


def check_model_existence():
    if not os.path.exists(MODEL_PATH):
        print("Please download the model from "
              "https://drive.google.com/file/d/1MdlN3JWUe8bpCR9A0irEr-Icc1WiPgZs/view?usp=sharing"
              f" and unpack it to '{MODEL_PATH}'.")
        exit(1)


def recognizer():
    return KaldiRecognizer(Model(MODEL_PATH), RATE)


def get_samples():
    return glob.glob(SAMPLES_PATH + '/*.wav')


def recognize_file(rec, file_path):
    wf = wave.open(file_path, 'rb')

    data = wf.readframes(CHUNK)

    while len(data) > 0:
        data = wf.readframes(CHUNK)

        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if len(result['text']) > 1:
                print(result)
        else:
            result = json.loads(rec.PartialResult())
            if len(result['partial']) > 1:
                print(result)

    wf.close()


def run():
    check_model_existence()

    r = recognizer()

    samples = get_samples()
    for sample in samples:
        print(f'Processing the file: {sample}')

        recognize_file(r, sample)


if __name__ == '__main__':
    run()
