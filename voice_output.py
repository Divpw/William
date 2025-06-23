import pyttsx3

def speak(text):
    """
    Uses the pyttsx3 library to speak the given text aloud.
    """
    engine = pyttsx3.init()

    # You can adjust properties like rate and volume if needed
    # rate = engine.getProperty('rate')
    # engine.setProperty('rate', rate - 50) # Slow down the speech
    # volume = engine.getProperty('volume')
    # engine.setProperty('volume', volume + 0.25) # Increase volume

    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    # Example usage:
    print("Testing the speak function...")
    speak("Hello, this is William. I am now able to speak.")
    speak("This is a second sentence to ensure runAndWait works correctly.")
    print("Speech test complete.")
