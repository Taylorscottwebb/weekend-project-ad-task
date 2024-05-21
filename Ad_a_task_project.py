# User Interface (UI):
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
# ```
# Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit
#     ```
# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task
# Viewing the list of tasks with from Incomplete and Complete tasks.
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and doc strings for clarity.
# Testing and Debugging:
# Thoroughly test your application to identify and fix any bugs.
# Consider edge cases, such as empty task lists or incorrect user input.
# Documentation:
# Include a README file that explains how to run the application and provides a brief overview of its features.
# Optional Features (Bonus):
# If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
# GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Include a link to your GitHub repository in your project documentation.
# Submission
# Submit your project, including all source code files and the README, to your instructor or designated platform.
# Project Tips
# Start by designing a simple user interface and plan the program's structure.
# Test your code frequently as you build each feature to ensure everything works as expected.
# Collaborate with fellow learners and seek help when needed. Remember, learning is a communal effort!
# By completing this project, you'll gain practical experience in Python programming and have a useful To-Do List Application to help you stay organized in your own life.
# Happy coding! :clipboard::snake:


# driver code that will call the functions based on the response variable thats holding the user input
# we're using cart and bag as parameters to be consistent with the above functions parameter naming conventions
# when we call the run function, we'll take shopping_cart and bagged_items as arguments
# cart and bag parameters will become the arguments in the functions within the run function
# def run(cart,bag):

def main():
    uncompleted_task_list = []
    completed_task_list = []
    while True:
        menu = """
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
        Enter the number -->
        """
        user_input = int(input(menu))
        if user_input == 1:
            user_task = input("What is the task you want to add?")
            add_task_to_list(task=user_task, uncompleted_task_list=uncompleted_task_list)
        elif user_input == 2:
             print(uncompleted_task_list,"these are your uncompleted tasks.",
             completed_task_list, " these are your completed tasks.")
        elif user_input == 3:
            user_completed_task = input("What is the task you want to complete?")
            mark_task_as_completed(task=user_completed_task, completed_task_list=completed_task_list, uncompleted_task_list=uncompleted_task_list)
        elif user_input == 4:
            remove_task == input("what is the task, you would like to delete?")

        elif user_input == 5:
            break
def add_task_to_list(task, uncompleted_task_list):
    uncompleted_task_list.append(task)
def mark_task_as_completed(task, completed_task_list, uncompleted_task_list):
    if task in uncompleted_task_list:
        completed_task_list.append(task)
        uncompleted_task_list.remove(task)
    else:
        print("The task does not exist!")
# This is defining my add to function and is holding our tasks in our notes for our argument in the while loop.
def remove_task(notes):
     tasks = input("what tasks would you like to remove from your notes?").lower()
     try:notes.remove(tasks, notes)
     except ValueError:
      print(f"{tasks}is not in your notes")
#this is also holding a place in our while argument

main()
 


     
