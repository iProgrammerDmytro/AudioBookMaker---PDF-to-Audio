import tempfile
from threading import Thread
from gtts import gTTS
from pygame import mixer

class TextToSpeechThread(Thread):
    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        self.play_audio(self.text)

    def play_audio(self, text):
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            tts.save(fp.name)
            mixer.init()
            mixer.music.load(fp.name)
            mixer.music.play()

    def stop_audio(self):
        mixer.music.stop()
