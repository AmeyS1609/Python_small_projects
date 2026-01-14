class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
    def deposit(self,amt,des=''):
        self.ledger.append({'amount': amt, 'description': des})
    def withdraw(self,amt,des=''):
        if sum(item['amount'] for item in self.ledger)-(amt)>=0:
            self.ledger.append({'amount': -amt, 'description': des})
            return True
        return False
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
    def transfer(self,amt,destination):
        if self.withdraw(amt,f"Transfer to {destination.name}"):#remember, good method
            destination.deposit(amt,f"Transfer from {self.name}")
            return True
        return False
    def check_funds(self,amt):
        if amt>sum(item['amount'] for item in self.ledger):
            return False
        return True
    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += desc + amt + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    spents=[]
    perct=[]
    output = "Percentage spent by category\n"
    for obj in categories:
        spents.append(-sum(item["amount"] for item in obj.ledger if item["amount"] < 0))
    total=sum(spents)
    for spent in spents:
        per=(spent/total)*100
        rp = int(per // 10) * 10
        perct.append(rp)
    for y in range(100,-1,-10):
        output+=f"{y:>3}| "#another method to align
        for per in perct:
            if per>=y:
                output+="o  "
            else:
                output+="   " 
        output+="\n"
    output += "    " + ("-" * (3 * len(categories) + 1)) + "\n"
    names=[item.name for item in categories]
    maxlen=max(len(name) for name in names)
    for i in range(maxlen):
        output+="     "
        for name in names:
            output += (name[i] + "  ") if i < len(name) else "   "
        output+="\n"
    return output.rstrip("\n")
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
    