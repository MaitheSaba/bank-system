from account import Account

class CheckingAccount(Account):
    def __init__(self, client, number, statement = "", balance=0.0, limit = 500, max_daily_withdrawals = 3, withdrawal_count = 0):
        super().__init__(client, number, statement, balance)
        self._limit = limit
        self._max_daily_withdrawals = max_daily_withdrawals
        self._withdrawal_count = withdrawal_count

    def limit(self):
        return self._limit
    
    def withdrawal_count(self):
        return self._withdrawal_count
    
    def add_withdrawal_count(self):
        """
        Increments the withdrawal count for the account

        Incrementa a contagem de saques da conta
        """
        self._withdrawal_count += 1

    def max_daily_withdrawals(self):
        return self._max_daily_withdrawals