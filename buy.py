import price
mydict = {"1": price.Dry_goods, "2": price.Fresh_produce, "3": price.Bakery_items, "4": price.Frozen_foods, "5": price.Personal_care_items}
def category():
    selected = []
    while True:
        match input('[Yes] To add another category\n[No] To exit the program\n').lower():
            case 'yes':
                try:
                    mydict[input("Choose one category:\n1,Dry Goods \n 2,Fresh produce \n 3,Bakery items \n 4,Frozen_foods \n 5,Personal care items \n Answer : ")]()
                except:
                    exit()
                selected.append(input("Enter the name of product : "))
            case 'no':
                with open('save.txt', 'w') as f:
                    f.write(' '.join(selected))
                break

category()
