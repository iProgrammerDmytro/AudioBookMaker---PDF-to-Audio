import threading
from tkinter import Tk, Frame, Label, Button, filedialog
import PyPDF2
from text_to_speech import TextToSpeechThread
from audio_player import AudioPlayer

class Application:
    def __init__(self, root):
        self.root = root
        self.audio_thread = None
        self.player = AudioPlayer()
        self.extracted_text = ""
        self.setup_gui()

    def extract_text(self):
        def _play_audio():
            file = filedialog.askopenfile(parent=self.root, mode="rb", title="Choose a PDF File")
            if file:
                pdf_reader = PyPDF2.PdfFileReader(file)
                for page_num in range(pdf_reader.numPages):
                    page_object = pdf_reader.getPage(page_num)
                    self.extracted_text += page_object.extractText()
                file.close()
        threading.Thread(target=_play_audio).start()

    def speak_text(self):
        self.audio_thread = TextToSpeechThread(self.extracted_text)
        self.audio_thread.start()

    def stop_speaking(self):
        if self.audio_thread is not None:
            self.audio_thread.stop_audio()

    def setup_gui(self):
        self.root.geometry("700x600")
        self.root.resizable(width=False, height=False)
        self.root.title("PDF to Audio")
        self.root.configure(background="light grey")

        frame1 = Frame(self.root, width=500, height=200, bg="indigo")
        frame1.pack(side="top", fill="both")

        frame2 = Frame(self.root, width=500, height=450, bg="light grey")
        frame2.pack(side="top", fill="y")

        title = Label(frame1, text="PDF to Audio", fg="black", bg="blue", font="Arial 28 bold")
        subtitle = Label(frame1, text="Hear your PDF File", fg="red", bg="indigo", font="Arial 25 bold")
        title.pack()
        subtitle.pack()

        select_button = Button(frame2, text="Select PDF File", activeforeground="red", command=self.extract_text, padx="70", pady="10", fg="black", bg="black", font="Arial 12")
        select_button.grid(row=0, pady=20, columnspan=2)

        play_button = Button(frame2, text="Play PDF File", command=self.speak_text, activeforeground="red", padx=60, pady="10", fg="black", bg="black", font="Arial 12")
        stop_button = Button(frame2, text="Stop Playing", command=self.stop_speaking, activeforeground="red", padx=60, pady="10", fg="black", bg="black", font="Arial 12")
        play_button.grid(row=4, column=0, pady=65)
        stop_button.grid(row=4, column=1, pady=65)

if __name__ == "__main__":
    root = Tk()  # Create the Tk root widget
    Application(root)  # Call the Application class to build the GUI
    root.mainloop()  # Start the Tkinter event loop
