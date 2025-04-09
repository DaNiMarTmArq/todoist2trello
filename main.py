from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.environ["TODOIST_API_TOKEN"]
api = TodoistAPI(key)
inbox_id = os.environ["TODOIST_INBOX_ID"]

def get_todoist_tasks(project_id: str) -> list[str]:
    """
    Get tasks from a Todoist project.
    
    :param project_id: The ID of the Todoist project.
    :return: A list of tasks in the project.
    """
    task_response = api.get_tasks(project_id=project_id)
    return [task.content for task in task_response]

try:
    # Get tasks from the inbox
    tasks = get_todoist_tasks(inbox_id)
    
    # Print the tasks
    for task in tasks:
        print(task)
   
except Exception as error:
    print(error)