import speech_recognition as sr
import json
import deepl as dl
trans = dl.Translator("DeepL auth_key here")
r = sr.Recognizer()
with sr.AudioFile(r"WAV or FLAC, AIFF here") as data1:
    data = r.record(data1)
r.adjust_for_ambient_noise = 0.5
r.energy_threshold = 500
a = r.recognize_google(audio_data=data,language="Language Code",show_all=True)
def tran(text):
    return(str(trans.translate_text(text,target_lang="Language Code")))
source = []
source.append(a["alternative"][0]["transcript"])
after_translate = "".join(list(map(tran,source)))
#print(after_translate)
with open("test.txt","w") as f:
    f.write(after_translate)