productID=[]
name=[]
category=[]
price=[]
stock=[]
sellerID=[]
cartid=[]
custid=[]
items=[]
totalamt=0
def updateStock():
    print("\n1.add /2.remove /3.update stock")
    choice=int(input())
    if choice==1:
        pID=int(input("Enter product ID: "))
        productID.append(pID)
        na=input("Enter product name: ")
        name.append(na)
        cat=input("Enter product category: ")
        category.append(cat)
        pri=int(input("Enter price of the product: "))
        price.append(pri)
        s=int(input("1.available / 2.out of stock : "))
        if s==1:
            stock.append(True)
        else:
            stock.append(False)
        sellID=int(input("Enter seller id: "))
        sellerID.append(sellID)
        print("product added successfully")
    elif choice==2:
        rID=int(input("Enter the product ID for removal of product: "))
        if rID in productID:
            productID.remove(rID)
            print("product removed sucessfully")
        else:
            print("The product ID is not available from our list of products")
    elif choice==3:
        rid=int(input("enter product id to update the status of the product: "))
        a=int(input("\nchoose the operation \n1.available \n2.out of stock: "))
        if rid in productID:
            ind=productID.index(rid)
            if a==1:
                stock[ind]=True
            else:
                stock[ind]=False
            print("\nstock updated successfully")
    else:
        print("enter valid number")
def getDetails():
    print("get details")
    PId=int(input("Enter product ID: "))
    if PId in productID:
        ind=productID.index(PId)
        print(name[ind])
        print(category[ind])
        print(price[ind])
        if stock[ind]:
            print("product available")
        else:
            print("Out of stock")
        print(sellerID[ind])
    else:
        print("There is currently NO PID retaled informations are available")
def cart():
    choice=int(input("1.add to cart \n2.remove from cart \n3.view items\n"))
    a=int(input("enter cart ID: "))
    b=int(input("Enter customer ID: "))
    if choice==1:
        cartid.append(a)
        custid.append(b)
        itm=input("enter the item to add: ")
        items.append(itm)
        print("item added successfully")
    elif choice==2:
        itm=input("enter the item to remove: ")
        items.remove(itm)
        print("item removed successfully")
    elif choice==3:
        if items:
            for i in range(len(items)):
                print(items[i])
        else:
            print("there is no items")
    

while True:
    c=int(input("1.add/remove/update products \n2.getdetails \n3.cart \n4.Exit \n"))
    if c==1:
        updateStock()
    elif c==2:
        getDetails()
    elif c==3:
        cart()
    elif c==4:
        break
    else:
        print("Enter valid number")
