# Inventory Management System
from services.inventory import *

#id, name, quantity, reorder_level, supplier
inventory1 = ("P001", "Steel Rods", 100, 20, "Steel Co.")
inventory2 = ("P002", "Aluminum Sheets", 50, 10, "Aluminum Inc.")
inventory3 = ("P003", "Copper Wires", 200, 30, "Copper Ltd.")
inventory4 = ("P004", "Plastic Pellets", 300, 50, "Plastic Corp.")
inventory5 = ("P005", "Rubber Gaskets", 150, 25, "Rubber Co.")
inventory6 = ("P006", "Glass Panels", 80, 15, "Glass Inc.")
inventory7 = ("P007", "Wooden Planks", 120, 20, "Wood Co.")

inventory_list = [inventory1, inventory2, inventory3, inventory4, inventory5, inventory6, inventory7]

for inventory in inventory_list:
    print(add_product(*inventory))

print(get_product("P001"))

print(update_product_stock("P001", 85))
print(update_product_stock("P001", 15))

print(view_inventory())

print(restock_product("P001", 50))
