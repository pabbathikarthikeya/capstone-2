import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)  # Using Google's Speech-to-Text
            print("📝 Converted Text:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand the audio")
        except sr.RequestError:
            print("❌ Could not request results, check your internet connection")

# Call the function
speech_to_text()
