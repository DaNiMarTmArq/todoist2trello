from todoist_api_python.api import TodoistAPI


class TodoistClient:
    def __init__(self, api_key: str):
        """
        Initialize the TodoistClient with an API key.
        
        :param api_key: The API key for Todoist.
        """
        self.api = TodoistAPI(api_key)

    def get_tasks(self, project_id: str) -> list[str]:
        """
        Get tasks from a Todoist project.
        
        :param project_id: The ID of the Todoist project.
        :return: A list of task contents in the project.
        """
        task_response = self.api.get_tasks(project_id=project_id)
        return [task.content for task in task_response]

    def complete_task(self, task_id: str) -> bool:
        """
        Complete a task by its ID.
        
        :param task_id: The ID of the task to complete.
        :return: True if the task was successfully completed, False otherwise.
        """
        try:
            self.api.close_task(task_id=task_id)
            return True
        except Exception as e:
            print(f"Error completing task: {e}")
            return False