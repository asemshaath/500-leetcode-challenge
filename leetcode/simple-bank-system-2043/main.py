class Bank:

    def __init__(self, balance: List[int]):
        self.accounts_balances = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._is_valid_account(account1) and self._is_valid_account(account2):
            if self.accounts_balances[account1-1] >= money:
                self.accounts_balances[account1-1] -= money
                self.accounts_balances[account2-1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._is_valid_account(account):
            self.accounts_balances[account-1] += money
            return True
        return False        

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        
        if self.accounts_balances[account-1] >= money:
            self.accounts_balances[account-1] -= money
            return True
        return False 

        
    
    def _is_valid_account(self, account):
        if account >= 1 and account <= len(self.accounts_balances):
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
