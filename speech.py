import speech_recognition as sr

#url = {'https://speech.googleapis.com/$discovery/rest?version=v1'
#       'key=AIzaSyD4sNrpPT1RFuhMxpfIF8LK2E8uBgDYPTg'}

class speech():

    @staticmethod
    def record():
        r = sr.Recognizer()
        with sr.Microphone(device_index = 1) as source:
            print("Say something!")
            audio = r.listen(source)
            
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return "Could not request results from Google Speech Recognition service; {0}".format(e)
