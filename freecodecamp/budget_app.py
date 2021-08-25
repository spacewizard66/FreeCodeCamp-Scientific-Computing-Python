
# !!! SUCCESS !!!
# Passes test but may contain input bugs, but no biggie


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description,})
        return self.ledger

    def withdraw(self, amount, description=''):
        less = self.check_funds(amount)
        if less == True:
            self.ledger.append({'amount': -amount, 'description': description,})
            return True
        else:
            return False

    def get_balance(self):
        fund = 0
        for i in range(len(self.ledger)):
            fund += self.ledger[i]['amount']
        return fund

    def transfer(self, amount, obj):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {obj.name}")
            obj.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        fund = 0
        for i in range(len(self.ledger)):
            fund += self.ledger[i]['amount']
        if fund < amount:
            return False
        else:
            return True

    def __str__(self):
        title = '{:*^30}'.format(self.name) + '\n'
        items = ''
        total = 0
        #return title
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']
        output = title + items + 'Total: ' + str(total)
        return output


    def get_withdrawls(self):
        total = 0
        for item in self.ledger:
            if item['amount'] < 0:
                total += item['amount']
        return total



#################################################################################
def truncate(n):
    multiplier = 10
    return int(n * multiplier) / multiplier

def get_totals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawls()
        breakdown.append(category.get_withdrawls())
    #round = list(map(int(total * 1), breakdown))
    rounded = list(map(lambda x: truncate(x/total), breakdown))
    return rounded

def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    dashes = '    ' + '---' * len(categories) + '-' + '\n'
    totals = get_totals(categories)
    p = 100
    for i in range(11):
        space = ' '
        for total in totals:
            if total * 100 >= p:
                space += 'o  '
            else:
                space += '   '
        result += str(p).rjust(3) + '|' + space + '\n'
        p -= 10
    result += dashes

    names = []
    row = ""
    for category in categories:
        names.append(category.name)
    maximum = len(max(names, key=len))
    for x in range(maximum):
        strang = "     "
        for name in names:
            try:
                strang += name[x] + "  "
            except IndexError:
                strang += "   "
        strang += '\n'
        row += strang
    #row -= '\n'
    result += row.rstrip("\n")
    return result

    #return categories



# Test Prints
# Press CTRL+K+C / CTRL+K+U to comment out entire blocks

# clothing = Category('Clothing')
# food = Category('Food')
# print(food.deposit(1000, 'Initial deposit'))
# print(food.withdraw(200))
# print(food.check_funds(800))
# print(food.get_balance())
# print(food.transfer(50, clothing))
# print(clothing.get_balance())
# print(food)
# create_spend_chart(food)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))