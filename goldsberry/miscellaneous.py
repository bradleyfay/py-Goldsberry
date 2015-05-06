class Transactions:
    """
    """
    def __init__(self):
        self._url = "http://stats.nba.com/feeds/NBAPlayerTransactions-559107/json.js"
        self._pull = requests.get(self._url)
    def data(self):
        return self._pull.json()['ListItems']

