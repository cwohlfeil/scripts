blog_1 = "Awesome"
blog_2 = "Shit"
blog_3 = "Cats"

site_title = "My Blog"


# Args are a list
def blog_posts(title, *args):
    print(title)
    for post in args:
        print(title, post)

blog_posts(site_title, blog_1, blog_2, blog_3)


# Kwargs are a dictionary
def blog_posts(title, **kwargs):
    print(title)
    for p_title, post in kwargs.items():
        print(p_title, post)

# kwargs have to be passed as a key value pair
blog_posts(site_title, blog_a="Super", blog_b="Sports", blog_c="Maymays")


# You can have both but they have to be in order, no mix n match
def fkn_args(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs.items():
        print(kwarg)

fkn_args(blog_1, blog_2, blog_a="fkuc", blog_b="u r mum")

# args is used to send a non-keyworded variable length argument list to the function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function.