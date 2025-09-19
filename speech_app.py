import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pt.init()

def speak(text):
    print(f"🗣️ {text}")
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            audio = recognizer.listen(source)
            cmd = recognizer.recognize_google(audio).lower()
            print(f"🎧 You said: {cmd}")
    except Exception as e:
        print(f"⚠️ Error recognizing speech: {e}")
    return cmd

def run():
    command = hear()
    if command:
        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"🎶 Playing {song} on YouTube")
            pk.playonyt(song)
        else:
            speak("❌ Sorry, I can only play songs on YouTube for now.")
    else:
        speak("❌ I didn't catch that. Please try again.")

# Start the assistant
run()
