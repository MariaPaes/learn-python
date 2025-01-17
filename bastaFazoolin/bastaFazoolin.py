class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + " to " + str(self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for cont in purchased_items:
      if cont in self.items:
        bill+= self.items[cont]
    return bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address 
  
  def available_menus(self, time):
    available_menus = []
    for cont in self.menus:
      if time >= cont.start_time and time <= cont.end_time:
        available_menus.append(cont)

    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch_items =  {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu ("Brunch", brunch_items, 1100, 1600)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early_bird", early_bird_items, 1500, 1800)

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu("Kids", kids_items, 1100, 2100)

menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

firstBusiness = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_itens = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepa_menu = Menu("Take a’ Arepa", arepas_itens, 1000, 2000)

arepas_place = Franchise ("189 Fitzgerald Avenue", [arepa_menu])

arepa_newBusiness = Business("Take a' Arepa", [arepas_place])