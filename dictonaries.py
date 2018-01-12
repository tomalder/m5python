"""list: General purpose, most widely used structure
can grow and shrink sequence type sortable

Tuple: cannot add or change useful for fixed data
faster than lists sequence type

Set: store non-duplicate items very fast acess 
math set ops unordered

dict: ley/value pairs assoicate array, like java hasmap, Unordered"""
# user_id = 209
# message = hello
# langauge = "english"
# datetime = "202"
# location = (44, -104)

post = {"user_id":209, "message":"hello","language":"english",
        "datetime":"202", "location":(44, -104)}
print(post)
#print(post(1)) printing something that does not exist
#print(post["message"]) how to actaully print something
#print(post["stuff"])
