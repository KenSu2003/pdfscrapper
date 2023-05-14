import pyautogui
from PIL import Image


# Take a screenshot
screenshot = pyautogui.screenshot()

# Locate the question and answer on the screen
question_location = pyautogui.locateOnScreen('question.png')
answer_location = pyautogui.locateOnScreen('answer.png')

# Copy the question and answer to the clipboard
pyautogui.click(question_location)
pyautogui.hotkey('ctrl', 'c')
question = pyperclip.paste()

pyautogui.click(answer_location)
pyautogui.hotkey('ctrl', 'c')
answer = pyperclip.paste()

# Print the question and answer
print(f'Question: {question}')
print(f'Answer: {answer}')