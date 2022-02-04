import speech_recognition as sr

# filename = "audio_cortado.wav"

class Conversor:
    def __init__(self, filename):
        self.filename = filename

    def conversor(self):
        r = sr.Recognizer()

        with sr.AudioFile(self.filename) as source:

            audio_data = r.record(source)

            texto = r.recognize_google(audio_data, language='pt-BR')

            print(texto)
        return texto
