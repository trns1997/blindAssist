
import speech_recognition as sr
#import pyaudio

#index = pyaudio.PyAudio().get_device_count() - 1
#print index

def speech_text():
	r = sr.Recognizer()
	with sr.Microphone(device_index=19) as source:
		print("Say something!")
    		audio = r.record(source, duration = 2)
	with open("play.wav", "wb") as f:
    		f.write(audio.get_wav_data())


	with sr.AudioFile("play.wav") as source:
		audio = r.listen(source)
#print(r.recognize_google(audio))
# Speech recognition using Google Speech Recognition
	try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
		obj = r.recognize_google(audio)
		with open("templates/crap.txt", "wb") as f:
                	f.write(obj)
	except sr.UnknownValueError:
   		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

