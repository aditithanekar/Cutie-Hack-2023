from PIL import Image
import pytesseract
import pyperclip
def image_to_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

def text_to_latex(text):
    # Basic formatting for LaTeX code
    latex_code = f"\\documentclass{{article}}\n\\begin{{document}}\n{text}\n\\end{{document}}"

    return latex_code

def main():
    # Ask the user for the path to the image file
    image_path = input("Enter the path to the image file: ")

    # Extract text from the image
    extracted_text = image_to_text(image_path)

    # Convert extracted text to LaTeX code
    latex_code = text_to_latex(extracted_text)

    # Copy the LaTeX code to the clipboard
    pyperclip.copy(latex_code)

    print("LaTeX code has been copied to the clipboard.")
    # DELETE THIS AFTER - TEMPORARY JUST FOR US TO SEE WHAT IS GETTING COPIED ONTO THE CLIPBOARD
    print(latex_code)

if __name__ == "__main__":
    main()

#use this to check: /Users/keerthi/Desktop/trydiv.png  or /Users/keerthi/Desktop/wp2.png



