import requests


class TrelloClient:
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token
        self.base_url = "https://api.trello.com/1"

    def create_card(self, list_id, name, description=""):
        """
        Creates a card in the specified Trello list.

        :param list_id: The ID of the Trello list where the card will be created.
        :param name: The name of the card.
        :param description: The description of the card (optional).
        :return: The response from the Trello API.
        """
        url = f"{self.base_url}/cards"
        query = {
            "key": self.api_key,
            "token": self.token,
            "idList": list_id,
            "name": name,
            "desc": description,
            "pos": "top"
        }
        response = requests.post(url, params=query)
        response.raise_for_status()
        return response.json()