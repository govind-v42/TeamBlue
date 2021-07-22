import redis
import csv


r = redis.Redis(
host='127.0.0.1',
port=6379)

# with open('C:/Users/govin/Desktop/dataset/ModifiedReview.csv', 'rt', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=';')
#     headers = reader.fieldnames
#     for row in reader:
#         Review = row['Review_translation']
#         id = row['\ufefforder_id']
#         r.set(id, Review)
        
    
# with open('C:/Users/govin/Desktop/dataset/olist_order_items_dataset.csv', 'rt', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=',')
#     headers = reader.fieldnames
    
#     for row in reader:
#         productid = row['product_id']
#         sellerid = row['seller_id']
#         orderquantity = row['order_item_id']
#         r.hset(productid, sellerid, orderquantity)


# with open('C:/Users/govin/Desktop/dataset/householdsupplies.csv', 'rt', encoding='utf-8') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter=';')
#    headers = reader.fieldnames
   
#    for row in reader:
#     item = row['\ufeffitem']
#     quantity = row['quantity']
#     r.zadd("homesupplies", {item:quantity})

print(r.get("658677c97b385a9be170737859d3511b"))
print(r.hget("4244733e06e7ecb4970a6e2683c13e61","48436dade18ac8b2bce089ec2a041202"))
print(r.zrevrange("homesupplies","0","-1"))






  

#As a seller, i want to view a list of items in home supplies section that are most bought by the customers so that i can add them to my inventory and increase my sales
       

  

        


