import threading
from pydub import AudioSegment
from pydub.playback import _play_with_pyaudio

class AudioPlayer:
    def __init__(self):
        self.audio = None
        self.playing = False
        self.thread = None

    def play_audio(self, file):
        self.audio = AudioSegment.from_mp3(file)
        _play_with_pyaudio(self.audio)

    def play(self, file):
        if not self.playing:
            self.playing = True
            self.thread = threading.Thread(target=self.play_audio, args=(file,))
            self.thread.start()

    def stop(self):
        if self.playing:
            self.playing = False
            self.thread.join()
