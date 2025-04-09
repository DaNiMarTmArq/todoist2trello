from clients.todoist import TodoistClient
from clients.trello import TrelloClient
import os
from dotenv import load_dotenv


load_dotenv()

TRELLO_API_KEY = os.getenv("TRELLO_API_KEY")
TRELLO_API_TOKEN = os.getenv("TRELLO_TOKEN")
TODOIST_API_KEY = os.getenv("TODOIST_API_TOKEN")

todoist_client = TodoistClient(TODOIST_API_KEY)
trello_client = TrelloClient(TRELLO_API_KEY, TRELLO_API_TOKEN)

def main(): 
    project_id = os.getenv("TODOIST_INBOX_ID")
    trello_list_id = os.getenv("TRELLO_LIST_ID")

    try:
        # Get tasks from Todoist
        tasks = todoist_client.get_tasks(project_id)
    except Exception as e:
        print(f"An error occurred while fetching tasks from Todoist: {e}")
        tasks = []

    try:
        # Post tasks to Trello
        for task in tasks:
            trello_client.create_card(trello_list_id, task)
            print(f"Task '{task}' have been successfully transferred from Todoist to Trello.")
    except Exception as e:
        print(f"An error occurred while posting tasks to Trello: {e}")

    

if __name__ == "__main__":
    main()