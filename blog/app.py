MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create post, "q" to quit.'

blogs = dict()  # blog_name: Blog object

def menu():
    # Show the user the available blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)


def print_blogs():
    # Print ht available blogs
    for key, blog in blogs.items():     # itmes() give a list of tuples
        print('- {}'.format(blog))
