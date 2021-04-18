class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.funds = 0
    def __str__(self):
        name_length = len(self.name)
        star_count = (30 - name_length)
        title_line = '*'*star_count + self.name + '*'*star_count
        if len(title_line) != 30: title_line = '*' + title_line
        ledger_list = ""
        for list_item in self.ledger:
            amt = list_item.get("amount")
            descr = list_item.get("description")
            descr = descr[:23]
            amt = '%.2f' % amt
            amt = amt[:7]
            ledger_list += descr + str(amt).rjust(30 - len(descr)) + '\n'

        # Returning full list.
        object_list = title_line + '\n' + ledger_list + 'Total: ' + str(self.funds)
        return object_list

    def deposit(self, amount, description = ""):
        """Method to deposit a certain amount with an optional description."""
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount, description = ""):
        """Method to withdraw a certain amount with an optional description."""
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            self.funds += amount
            return True
        else:
            return False

    def get_balance(self):
        """Method to returns current balance."""
        return self.funds

    def transfer(self, amount, budget_category):
        """Method to transfer money from one category to another."""
        if self.check_funds(amount):
            amount *= -1
            self.ledger.append({"amount": amount, "description": f"Transfer to {budget_category.name}"})
            budget_category.ledger.append({"amount": amount * -1, "description": f"Transfer from {self.name}"})
            self.funds += amount
            budget_category.funds -= amount
            return True
        else:
            return False

    def check_funds(self, amount):
        """Method to check if funds are available for certain amount."""
        if amount < self.funds:
            return True
        else:
            return False