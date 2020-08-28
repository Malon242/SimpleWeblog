from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import PostComment

def posts(request):
	# 5 most recent admin posts
	all_posts = Post.objects.all()[:5]
	data = {"posts": all_posts,}
	return render(request, 'weblog/posts.html', data)


def comments(request, pk):
	post = get_object_or_404(Post, pk=pk)

	new_comment = None

	if request.method == 'POST':
		# Posted comment
		form = PostComment(data=request.POST)

		if form.is_valid():
			# Create Comment object
			new_comment = form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			return HttpResponseRedirect('/post'+str(pk))

	else:
		form = PostComment()

	data = {"post": post, "comments": comments, 
		"new_comment": new_comment, "form": form}
	return render(request, 'weblog/comments.html', data)