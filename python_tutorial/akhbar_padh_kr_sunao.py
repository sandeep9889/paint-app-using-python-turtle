# akhbar padh kr sunao
from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")
speak.Speak("harrybhaihowareyou")
if __name__ =="__main__":
    speak("kaisehoharrybhai")