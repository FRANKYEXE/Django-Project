from django.shortcuts import render

# Create your views here.

# Public Feed
# list all the articles
def article_list_views(request):
    pass


# list all the categories
def category_list_view(request):
    pass


# list all the articles under a specific category
def category_post_view(request,id):
    pass


# button (my blogs/my article), when clicked on this
# show only the logged-in users articles
def user_article_list_views(request,id):
    pass


# Show full details of a blog post / article when clicked on it
def article_details_view(request,id):
    pass

# Allow only logged-in user to create a new article
def article_create_view(request):
    pass

# allow only logged-in user to update only his own article
# user must not be able to edit anything from other users article/blog post
def article_update_view(request,id):
    pass

# Allow user to delete the article which only belongs to them.
def article_delete_view(request,id):
    pass