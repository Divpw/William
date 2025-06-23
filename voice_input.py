import speech_recognition as sr

def listen_for_command():
    """
    Listens for audio from the default microphone, transcribes it to text,
    and returns the transcribed text.
    """
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10) # Added timeout and phrase_time_limit
        except sr.WaitTimeoutError:
            print("No speech detected within the time limit.")
            return ""

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred during speech recognition: {e}")
        return ""

if __name__ == '__main__':
    # Example usage:
    print("Speak a command into your microphone.")
    command = listen_for_command()
    if command:
        print(f"Command received: {command}")
    else:
        print("No command was recognized.")
