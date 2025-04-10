from todoist_api_python.api import Task
from clients.todoist import TodoistClient
from clients.trello import TrelloClient
import os
from dotenv import load_dotenv
import argparse


load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_API_TOKEN = os.getenv("TRELLO_TOKEN")
TODOIST_API_KEY = os.getenv("TODOIST_API_TOKEN")

todoist_client = TodoistClient(TODOIST_API_KEY)
trello_client = TrelloClient(TRELLO_API_KEY, TRELLO_API_TOKEN)

def complete_todoist_tasks(tasks: list[Task]):
    for task in tasks:
        try:
            todoist_client.complete_task(task_id=task.id)
            print(f"Task {task.id} marked as complete in Todoist\n")
        except Exception as e:
            print(f"An error occurred while marking tasks as complete in Todoist: {e}")
   


def main(): 
    parser = argparse.ArgumentParser(description="Transfer tasks from Todoist to Trello.")
    parser.add_argument("-d", "-D", action="store_true", dest="delete", help="Delete tasks after transferring")
    args = parser.parse_args()
    delete = args.delete

    project_id = os.getenv("TODOIST_INBOX_ID")
    trello_list_id = os.getenv("TRELLO_LIST_ID")

    try:
        # Get tasks from Todoist
        tasks = todoist_client.get_tasks(project_id)
        if len(tasks) == 0:
            print("No tasks to export")
            return
    except Exception as e:
        print(f"An error occurred while fetching tasks from Todoist: {e}")
        tasks = []

    try:
        # Post tasks to Trello
        for task in tasks:
            trello_client.create_card(trello_list_id, task.content)
            print(f"Task '{task.content}' have been successfully transferred from Todoist to Trello. \n")
    except Exception as e:
        print(f"An error occurred while posting tasks to Trello: {e}")

    if delete:
        complete_todoist_tasks(tasks)    
    else:
        user_input = input("Do you want to mark the tasks as complete in Todoist? (yes/no): ").strip().lower()
        if user_input in ["yes", "y"]:
            complete_todoist_tasks(tasks)



if __name__ == "__main__":
    main()