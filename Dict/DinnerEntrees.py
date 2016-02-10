__author__ = 'ambli'

def get_quantities(table_to_foods):
    entree_orders = {}

    for table_order in table_to_foods:
        for entree in table_order:
            if entree not in entree_orders:
                entree_orders[entree] = 1
            else:
                entree_total = entree_orders[entree]
                entree_total += 1
                entree_orders[entree] = entree_total

    return entree_orders

table = {'t1' : ['Vegetarian stew', 'Poutine', "Vegetarian stew"],
         't2' : ['Steak pie', 'Poutine', 'Vegetarian stew'],
         't3' : ['Steak pie', 'Steak pie']}

entree_orders = get_quantities(table)

print (entree_orders)
