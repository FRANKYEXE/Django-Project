from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile

# to view a particular user profile (similar to insta:no of blog posts/articles, total number of likes overall, user bio, picture, list all the blogs posted)
def view_profile(request, id):
    user = get_object_or_404(User, id=id)
    profile = get_object_or_404(Profile, user=user)
    blogs = user.blog_set.all()  # Assuming you have a Blog model with a ForeignKey to User
    total_likes = sum(blog.likes.count() for blog in blogs)  # Assuming you have a likes field in Blog model
    context = {
        'user': user,
        'profile': profile,
        'blogs': blogs,
        'total_likes': total_likes,
    }
    return render(request, 'view_profile.html', context)

# user should be able to edit only his own profile, not other users profile
# can edit bio and profile picture only
@login_required
def edit_profile(request, id):
    user = get_object_or_404(User, id=id)
    if request.user != user:
        return redirect('home')  # Redirect to home or some other page if the user is not the owner

    profile = get_object_or_404(Profile, user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile', id=user.id)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

# Optional...
# user should be able to delete only his own profile, not other users profile
# make sure to give a confirmation message ....
# as all the posts will be connected to the user..
@login_required
def delete_profile(request, id):
    user = get_object_or_404(User, id=id)
    if request.user != user:
        return redirect('home')

    if request.method == 'POST':
        user.delete()
        return redirect('home')
    return render(request, 'delete_profile.html', {'user': user})