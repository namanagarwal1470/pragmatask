def calculatediscounts(user,total,categorycount,itemsinfo):
    discounts={}

    if total>5000:
        discounts["percentagediscount"]=total * 0.10


    ordercount=len(user.get("orders",[]))
    if ordercount > 5:
        discounts["flatdiscount"]=500


    for category,count in categorycount.items():
        if category.lower() == "electronics" and count > 3:
            electronicstotal=sum([i["price"] * i["quantity"] for i in itemsinfo if i["category"].lower() == "electronics"])
            discounts["categorydiscount"] = electronicstotal * 0.05

    return discounts