
class User:
    all_posts = {}

    def __init__(self, name, email, dl_number):
        self.name = name
        self.email = email
        self.dl = dl_number
        self.posts = []
        self.all_posts[name] = self.posts

    def create_post(self, post):
        self.posts.append(post)
        self.all_posts[self.name]= self.posts

    def delete_post(self, index):
        self.posts.pop(index)
        self.all_posts[self.name]= self.posts
        

    


first = User('Matt', 'matt@gmail.com','12345')
second = User('Mark', 'mark@gmail.com','23456')
third = User('Megan', 'megan@gmail.com','34567')

post1 = "Hello World"
post2 = "Goodbye World"
first.create_post(post1)
print(User.all_posts)
second.create_post(post2)
print(User.all_posts)
print(second.posts)
second.delete_post(0)
print(User.all_posts)