from django.shortcuts import render,redirect, get_object_or_404

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from django.contrib.auth.decorators import login_required


# posting
@require_http_methods(['GET','POST'])
@login_required
def create_posting(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('blog:detail_posting', posting.pk)
    else:
        form = PostingForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })

@require_safe
def index_posting(request):
    postings = Posting.objects.all()
    return render(request,'blog/index.html',{
        'postings':postings,
    })

@require_http_methods(['GET','POST'])
def detail_posting(request,posting_pk):
    posting = get_object_or_404(Posting,pk=posting.pk)
    replies = posting.reply_set.all()
    form = ReplyForm()

    return render(request, 'blog/detail.html', {
        'posting': posting,
        'replies': replies,
        'form': form,
     })

def update_posting(request):
    pass

def delete_posting(request):
    pass




# reply
def create_reply(request):
    pass

def delete_reply(request):
    pass