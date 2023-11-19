import flet as ft
import openai
import tkinter as tk
from tkinter import filedialog

# Set your OpenAI API key
openai.api_key = "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"

def main(page):
    page.scroll = True

    # Declare text_input as a global variable
    global text_input

    def btn_clicked(e):
        # Access text_input from the global scope
        input_text = str(text_input.value)
        output = AI.answer_Generator(input_text)

        clear_button = ft.FloatingActionButton("Clear", height=60, on_click=clear)
        page.add(clear_button)
        page.add(ft.Container(ft.Text(value=text_input.value), bgcolor=ft.colors.GREEN, padding=10))
        page.add(ft.Container(ft.Text(value=output, selectable=True), padding=10))
        text_input.value = ""
        page.update()

    def choose_file(e):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Do something with the selected file path, e.g., display it on the page
            page.add(ft.Container(ft.Text(value=f"Selected File: {file_path}"), padding=10))
            page.update()

    # heading
    page.title = "CutieSolver.ai"
    page.horizontal_alignment = "center"
    heading = ft.Text(value="Need Help With Homework, No Problem", size=24)

    # create a text input field
    text_input = ft.TextField(hint_text="Input question here...", expand=True, multiline=True)

    # create a submit button
    submit_button = ft.ElevatedButton("Submit", height=60, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)), on_click=btn_clicked)

    # create a button to choose a file
    choose_file_button = ft.ElevatedButton("Choose File", height=60, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)), on_click=choose_file)

    # place everything you want in one row into the row object in a list
    row = ft.Row([text_input, submit_button, choose_file_button])
    page.add(heading, row)

    def clear(e):
        if page.controls == 1:
            pass
        else:
            page.controls.pop()
            page.update()

ft.app(target=main)