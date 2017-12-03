import speech_recognition as sr

#url = {'https://speech.googleapis.com/$discovery/rest?version=v1'
#       'key=AIzaSyD4sNrpPT1RFuhMxpfIF8LK2E8uBgDYPTg'}

class Speech():

    @staticmethod
    def record():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
        try:
            return r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)
