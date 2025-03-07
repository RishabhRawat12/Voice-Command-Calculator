import pyttsx3 as speak
import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox
import sys

"""Function to convert text to speech using pyttsx3"""
def speak_text(output_text):
    speech_engine = speak.init()
    speech_engine.say(output_text)
    speech_engine.runAndWait()

"""Function to evaluate a mathematical expression"""
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except SyntaxError:
        return "Invalid syntax in the expression."
    except NameError:
        return "Unknown variable or function used in the expression."
    except TypeError:
        return "Invalid operation in the expression."
    except OverflowError:
        return "The result is too large to handle."
    except Exception as error:
        return f"An error occurred: {str(error)}"

"""function to take user's voice for calculating"""
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening for your input...")
        try:
            audio_data = recognizer.listen(mic)
            user_input = recognizer.recognize_google(audio_data)
            return user_input
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "There is an issue with the internet connection."

"""Process the spoken input and convert it into a valid mathematical expression."""
def process_math_expression(user_input):
    word_to_symbol = {
        "plus": "+",
        "minus": "-",
        "times": "*",
        "into": "*",
        "x": "*",
        "divided by": "/",
        "over": "/",
        "raise to power": "**",
        "power of": "**",
        "modulus": "%",
    }

    if "sum of" in user_input:
        numbers = user_input.replace("sum of", "").split(" and ")
        if len(numbers) == 2:
            user_input = f"{numbers[0].strip()} + {numbers[1].strip()}"
        else:
            return "Invalid input for 'sum of'. Please provide two numbers."
    elif "difference of" in user_input:
        numbers = user_input.replace("difference of", "").split(" and ")
        if len(numbers) == 2:
            user_input = f"{numbers[0].strip()} - {numbers[1].strip()}"
        else:
            return "Invalid input for 'difference of'. Please provide two numbers."
    elif "product of" in user_input:
        numbers = user_input.replace("product of", "").split(" and ")
        if len(numbers) == 2:
            user_input = f"{numbers[0].strip()} * {numbers[1].strip()}"
        else:
            return "Invalid input for 'product of'. Please provide two numbers."
    elif "quotient of" in user_input:
        numbers = user_input.replace("quotient of", "").split(" and ")
        if len(numbers) == 2:
            user_input = f"{numbers[0].strip()} / {numbers[1].strip()}"
        else:
            return "Invalid input for 'quotient of'. Please provide two numbers."

    if "square root of" in user_input:
        user_input = user_input.replace("square root of", "") + "**(1/2)"
    if "cube root of" in user_input:
        user_input = user_input.replace("cube root of", "") + "**(1/3)"

    for word, symbol in word_to_symbol.items():
        user_input = user_input.replace(word, symbol)

    user_input = user_input.strip()
    return user_input

"""Main application class for the Voice Command Calculator"""
class VoiceCommandCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Command Calculator")
        self.root.geometry("400x200")
        
        self.label = tk.Label(self.root, text="Welcome to the Voice Command Calculator!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.result_button = tk.Button(self.root, text="Start Listening", font=("Arial", 12), command=self.start_listening)
        self.result_button.pack(pady=20)
        speak_text("Welcome to the Voice Command Calculator.")

    def start_listening(self):
        speak_text("Please say a mathematical expression, or say 'exit' to close the program.")
        spoken_input = get_voice_input()

        if "exit" in spoken_input.lower():
            speak_text("Thank you for using the Voice Command Calculator.")
            messagebox.showinfo("Goodbye", "Thank you for using the Voice Command Calculator!")
            self.root.quit()
            return

        print(f"You said: {spoken_input}")
        math_expression = process_math_expression(spoken_input.lower())
        calculation_result = evaluate_expression(math_expression)
        print(f"Result: {calculation_result}")
        self.label.config(text=f"The result is: {calculation_result}")
        speak_text(f"The result is {calculation_result}")

"""Main execution block"""
if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceCommandCalculatorApp(root)
    root.mainloop()