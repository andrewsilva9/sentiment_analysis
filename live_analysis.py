import speech_recognition as sr
import text_class

rec = sr.Recognizer()
sentiment = ["Negative", "Positive"]
print("Hello, how are you?")
while True:
	print("open loop")
	with sr.Microphone() as source:
		audio = rec.listen(source=source)

	try:
		transcription = rec.recognize_google(audio)
	except sr.UnknownValueError:
		transcription = "Google Speech API is confused"
	except sr.RequestError as e:
		transcription = "Request to Google Speech API failed, request error: ", e

	print("Input: ", transcription)
	print("returned: ", text_class.classify_text([transcription]))

	print("Sentiment of input: ", sentiment[int(text_class.classify_text([transcription])[0])])

