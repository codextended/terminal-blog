import pymongo
from database import Database
from models.post import Post
from models.blog import Blog


Database.initialize()

# post = Post("1234", "First Post", "This is my first post.", "Smath Cadet")
# post.save_to_mongo()

# post = Post("5678", "Second Post", "This is the second post added to the database.", "Smath Cadet")
# post.save_to_mongo()

blog = Blog(author="Smath Cadet", title="Sample Title", description="Sample description")

blog.new_post()
blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())


# uri = "mongodb://127.0.0.1:27017"
# client = pymongo.MongoClient(uri)
# database = client['blog']
# collection = database['students']

# # students = collection.find({})
# students = [student for student in collection.find({})]

# for student in students:
#     print(student)

