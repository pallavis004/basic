# Simple Blog System

posts = []

def create_post(title, content, author):
    post = {
        "id": len(posts) + 1,
        "title": title,
        "content": content,
        "author": author
    }
    posts.append(post)
    return post

def get_all_posts():
    return posts

def get_post_by_id(post_id):
    for post in posts:
        if post["id"] == post_id:
            return post
    return None

def display_post(post):
    print(f"\n--- Post #{post['id']} ---")
    print(f"Title: {post['title']}")
    print(f"Author: {post['author']}")
    print(f"Content: {post['content']}")

# Sample posts
create_post("Getting Started with Python", "Python is a great language for beginners.", "Alice")
create_post("Web Development Basics", "HTML, CSS, and JavaScript are the building blocks of the web.", "Bob")
create_post("Why I Love Coding", "Coding allows you to build anything you imagine.", "Charlie")

# Display all posts
for post in get_all_posts():
    display_post(post)
