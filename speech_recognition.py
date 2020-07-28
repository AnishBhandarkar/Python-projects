#Speech Recognition
#Internet required to run the program

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print("speak anything :")
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print("You said : {}".format(text))

	except:
		print("sorry could not recognize what you said")
	
print("Thank you :)")
