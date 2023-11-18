#pip install flet
import flet
from flet import *

def main(page: Page):
    page.title = "Counter App" #app name
    page.vertical_alignment = "center"

    txt_field = TextField(value="0", width=100, text_align="right")
    page

    def minus_clicked(e):
        txt_field.value = int(txt_field.value) - 1
        page.update()
    
    def plus_clicked(e):
        txt_field.value = int(txt_field.value) + 1
        page.update()

    page.add(
        Row(
            [
        IconButton(icons.REMOVE, on_click=minus_clicked),
        txt_field,
        IconButton(icons.ADD, on_click=plus_clicked),
            ],
    alignment="center"
        )
    )

flet.app(target=main)