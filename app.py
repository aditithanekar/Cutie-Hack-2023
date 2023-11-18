# Import necessary modules from the flet library
from calendar import c
import flet
from flet import (
    Page,
    TextField,
    FloatingActionButton,
    Column,
    Row,
    Text,
    IconButton,
    OutlinedButton,
    Tabs,
    Tab,
    UserControl,
    Checkbox,
    colors,
    icons,
)

# Define a UserControl class for individual tasks
class Task(UserControl):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete

    def build(self):
        # Create a Checkbox for task completion status
        self.display_task = Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        # Create a TextField for editing task name
        self.edit_name = TextField(expand=1)

        # Create a view for displaying the task and controls for editing/deleting
        self.display_view = Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.display_task,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        IconButton(
                            icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        # Create a view for editing the task (initially not visible)
        self.edit_view = Row(
            visible=False,
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                self.edit_name,
                IconButton(
                    icon=icons.DONE_OUTLINE_OUTLINED,
                    icon_color=colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )

        return Column(controls=[self.display_view, self.edit_view])

    # Handler for the edit button click
    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    # Handler for the save button click
    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    # Handler for the delete button click
    def delete_clicked(self, e):
        self.task_delete(self)

    # Handler for the task completion status change
    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

# Define a UserControl class for the entire Todo App
class MyTodoApp(UserControl):
    def build(self):
        # Create a TextField for adding new tasks
        self.new_task = TextField(hint_text="Add a new task here", expand=True)
        # Create a Column to hold the list of tasks
        self.tasks = Column()

        # Create Tabs for filtering tasks by status
        self.filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="All"), Tab(text="Active"), Tab(text="Completed")],
        )

        # Display the count of active tasks
        self.items_left = Text("0 items left")

        # Return the layout structure of the Todo App
        return Column(
            width=600,
            controls=[
                Row([Text(value="Todos", style="headlineMedium")], alignment="center"),
                Row(
                    controls=[
                        self.new_task,
                        FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                        Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.items_left,
                                OutlinedButton(
                                    text="Clear completed", on_click=self.clear_clicked
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

    # Handler for adding a new task
    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    # Handler for updating task completion status
    def task_status_change(self, task):
        self.update()

    # Handler for deleting a task
    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    # Handler for changing the selected filter tab
    def tabs_changed(self, e):
        self.update()

    # Handler for clearing completed tasks
    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    # Update the visibility and count of tasks based on the selected filter
    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "All"
                or (status == "Active" and not task.completed)
                or (status == "Completed" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} active item(s) left"
        super().update()

# Main function to create and display the Todo App
def main(page: Page):
    page.title = "Todo App"
    page.horizontal_alignment = "center"

    # Create an instance of the Todo App
    app = MyTodoApp()

    # Add the Todo App to the page
    page.add(app)

# Run the Flet app with the main function and Todo App view
flet.app(target=main, view=flet.FLET_APP)




