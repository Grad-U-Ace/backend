import uuid
from datetime import datetime


class Ecommerce:
    def __init__(self, name, products):
        self.name = name
        self.products = products

class Product:
    def __init__(self, name, price, description, messages):
        self.id = uuid.uuid4()
        self.name = name,
        self.price = price,
        self.description = description
        self.messages = messages

class Message:
    def __init__(self, customer_name, replies):
        self.customer_name = customer_name
        self.replies = replies


class Reply:
    def __init__(self, sender, reply, date_created=datetime.now()):
        self.sender = sender
        self.reply = reply
        self.date_created = date_created

reply_tokped_a_1 = Reply("user1", "halo")
reply_tokped_a_2 = Reply("seller", "hai")
reply_tokped_a_3 = Reply("user1", "barangnysa bagus")
reply_tokped_a_4 = Reply("seller", "hehe makasih")

message_tokped_a = Message("user1", [reply_tokped_a_1, reply_tokped_a_2, reply_tokped_a_3, reply_tokped_a_4])

product_tokped_1 = Product("Product 1", 80000, "Description of Product 1", [message_tokped_a])

tokopedia = Ecommerce("Tokopedia", [product_tokped_1])



# stores = [
#         {
#             "name": "tokopedia",
#             "products": [
#                 {
#                     "id": "p1",
#                     "name": "Product 1",
#                     # "thumbnail": generateThumbnail("p1"),
#                     "price": 50000,
#                     "description": "Description of Product 1",
#                     "messages": [
#                         {
#                             "id": "m1",
#                             "customerName": "Alice",
#                             # profilePicture: generateThumbnail("m1"),
#                             "message": "Is this product available?",
#                             "time": "2024-06-01 10:00:00",
#                         },
#                         {
#                             "id": "m2",
#                             "customerName": "Bob",
#                             # profilePicture: generateThumbnail("m2"),
#                             "message": "Can I get a discount?",
#                             "time": "2024-06-01 10:15:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p2",
#                     "name": "Product 2",
#                     # "thumbnail": generateThumbnail("p2"),
#                     "price": 80000,
#                     "description": "Description of Product 2",
#                     "messages": [
#                         {
#                             "id": "m3",
#                             "customerName": "Carol",
#                             # profilePicture: generateThumbnail("m3"),
#                             "message": "Does this come in different colors?",
#                             "time": "2024-06-02 11:00:00",
#                         },
#                         {
#                             "id": "m4",
#                             "customerName": "Dave",
#                             # profilePicture: generateThumbnail("m4"),
#                             "message": "What's the return policy?",
#                             "time": "2024-06-02 11:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p3",
#                     "name": "Product 3",
#                     # "thumbnail": generateThumbnail("p3"),
#                     "price": 120000,
#                     "description": "Description of Product 3",
#                     "messages": [
#                         {
#                             "id": "m5",
#                             "customerName": "Eve",
#                             # profilePicture: generateThumbnail("m5"),
#                             "message": "Is this product new?",
#                             "time": "2024-06-03 12:00:00",
#                         },
#                         {
#                             "id": "m6",
#                             "customerName": "Frank",
#                             # profilePicture: generateThumbnail("m6"),
#                             "message": "Can I return this product?",
#                             "time": "2024-06-03 12:45:00",
#                         },
#                     ],
#                 },
#             ],
#         },
#         {
#             "name": "shopee",
#             "products": [
#                 {
#                     "id": "p4",
#                     "name": "Product 4",
#                     # "thumbnail": generateThumbnail("p4"),
#                     "price": 75000,
#                     "description": "Description of Product 4",
#                     "messages": [
#                         {
#                             "id": "m7",
#                             "customerName": "Grace",
#                             # profilePicture: generateThumbnail("m7"),
#                             "message": "What is the warranty period?",
#                             "time": "2024-06-04 13:00:00",
#                         },
#                         {
#                             "id": "m8",
#                             "customerName": "Hank",
#                             # profilePicture: generateThumbnail("m8"),
#                             "message": "Is there free shipping?",
#                             "time": "2024-06-04 13:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p5",
#                     "name": "Product 5",
#                     # "thumbnail": generateThumbnail("p5"),
#                     "price": 60000,
#                     "description": "Description of Product 5",
#                     "messages": [
#                         {
#                             "id": "m9",
#                             "customerName": "Ivy",
#                             # profilePicture: generateThumbnail("m9"),
#                             "message": "Does it include accessories?",
#                             "time": "2024-06-05 14:00:00",
#                         },
#                         {
#                             "id": "m10",
#                             "customerName": "Jack",
#                             # profilePicture: generateThumbnail("m10"),
#                             "message": "What are the dimensions?",
#                             "time": "2024-06-05 14:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p6",
#                     "name": "Product 6",
#                     # "thumbnail": generateThumbnail("p6"),
#                     "price": 90000,
#                     "description": "Description of Product 6",
#                     "messages": [
#                         {
#                             "id": "m11",
#                             "customerName": "Kim",
#                             # profilePicture: generateThumbnail("m11"),
#                             "message": "Is this eco-friendly?",
#                             "time": "2024-06-06 15:00:00",
#                         },
#                         {
#                             "id": "m12",
#                             "customerName": "Liam",
#                             # profilePicture: generateThumbnail("m12"),
#                             "message": "What are the payment options?",
#                             "time": "2024-06-06 15:30:00",
#                         },
#                     ],
#                 },
#             ],
#         },
#         {
#             "name": "lazada",
#             "products": [
#                 {
#                     "id": "p7",
#                     "name": "Product 7",
#                     # "thumbnail": generateThumbnail("p7"),
#                     "price": 60000,
#                     "description": "Description of Product 7",
#                     "messages": [
#                         {
#                             "id": "m13",
#                             "customerName": "Mike",
#                             # profilePicture: generateThumbnail("m13"),
#                             "message": "Is this product new?",
#                             "time": "2024-06-07 16:00:00",
#                         },
#                         {
#                             "id": "m14",
#                             "customerName": "Nina",
#                             # profilePicture: generateThumbnail("m14"),
#                             "message": "Can I return this product?",
#                             "time": "2024-06-07 16:45:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p8",
#                     "name": "Product 8",
#                     # "thumbnail": generateThumbnail("p8"),
#                     "price": 85000,
#                     "description": "Description of Product 8",
#                     "messages": [
#                         {
#                             "id": "m15",
#                             "customerName": "Oscar",
#                             # profilePicture: generateThumbnail("m15"),
#                             "message": "What is the material?",
#                             "time": "2024-06-08 17:00:00",
#                         },
#                         {
#                             "id": "m16",
#                             "customerName": "Pam",
#                             # profilePicture: generateThumbnail("m16"),
#                             "message": "Is it available in other sizes?",
#                             "time": "2024-06-08 17:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p9",
#                     "name": "Product 9",
#                     # "thumbnail": generateThumbnail("p9"),
#                     "price": 100000,
#                     "description": "Description of Product 9",
#                     "messages": [
#                         {
#                             "id": "m17",
#                             "customerName": "Quinn",
#                             # profilePicture: generateThumbnail("m17"),
#                             "message": "Does it come with a warranty?",
#                             "time": "2024-06-09 18:00:00",
#                         },
#                         {
#                             "id": "m18",
#                             "customerName": "Ray",
#                             # profilePicture: generateThumbnail("m18"),
#                             "message": "Can I get expedited shipping?",
#                             "time": "2024-06-09 18:30:00",
#                         },
#                     ],
#                 },
#             ],
#         },
#         {
#             "name": "blibli",
#             "products": [
#                 {
#                     "id": "p10",
#                     "name": "Product 10",
#                     # "thumbnail": generateThumbnail("p10"),
#                     "price": 90000,
#                     "description": "Description of Product 10",
#                     "messages": [
#                         {
#                             "id": "m19",
#                             "customerName": "Sara",
#                             # profilePicture: generateThumbnail("m19"),
#                             "message": "What colors are available?",
#                             "time": "2024-06-10 19:00:00",
#                         },
#                         {
#                             "id": "m20",
#                             "customerName": "Tom",
#                             # profilePicture: generateThumbnail("m20"),
#                             "message": "Do you ship internationally?",
#                             "time": "2024-06-10 19:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p11",
#                     "name": "Product 11",
#                     # "thumbnail": generateThumbnail("p11"),
#                     "price": 70000,
#                     "description": "Description of Product 11",
#                     "messages": [
#                         {
#                             "id": "m21",
#                             "customerName": "Uma",
#                             # profilePicture: generateThumbnail("m21"),
#                             "message": "Is it durable?",
#                             "time": "2024-06-11 20:00:00",
#                         },
#                         {
#                             "id": "m22",
#                             "customerName": "Victor",
#                             # profilePicture: generateThumbnail("m22"),
#                             "message": "What is the return policy?",
#                             "time": "2024-06-11 20:30:00",
#                         },
#                     ],
#                 },
#                 {
#                     "id": "p12",
#                     "name": "Product 12",
#                     # "thumbnail": generateThumbnail("p12"),
#                     "price": 95000,
#                     "description": "Description of Product 12",
#                     "messages": [
#                         {
#                             "id": "m23",
#                             "customerName": "Wendy",
#                             # profilePicture: generateThumbnail("m23"),
#                             "message": "How long is the delivery time?",
#                             "time": "2024-06-12 21:00:00",
#                         },
#                         {
#                             "id": "m24",
#                             "customerName": "Xander",
#                             # profilePicture: generateThumbnail("m24"),
#                             "message": "Can I change my order after placing it?",
#                             "time": "2024-06-12 21:30:00",
#                         },
#                     ],
#                 },
#             ],
#         },
#     ]