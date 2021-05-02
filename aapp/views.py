from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Sura, Comment, IslaminSpb, Family, Article, Fcomment, About
from .forms import NewComment



# def base(request):
#     return render_to_response('aapp/base.html')
    
def home(request):
	posts = Post.objects.order_by('-date')[0:4]
	articles=Article.objects.order_by('-date')[0:4]
	families=Family.objects.order_by('-date')[0:4]
	islams=IslaminSpb.objects.order_by('-date')[0:4]

	# paginator = Paginator(posts, 4)
	# page = request.GET.get('page')
	# try:
	# 	posts = paginator.page(page)
	# except PageNotAnInteger:
	# 	posts = paginator.page(1)
	# except EmptyPage:
	# 	posts = paginator.page(paginator.num_page)
	context = {
	'title': 'Главная' ,
	'posts': posts ,
	'articles': articles,
	'families': families,
	'islams': islams,
	
	}
	return render(request, 'aapp/home.html', context)

#-------------------------------------------------------------
#Раздел О нас
def about(request):
	abouts = About.objects.all()
	context = {
	'title': 'Контакты' ,
	'abouts': abouts,
	}
	return render(request, 'aapp/about.html', context)

def contact(request):
	context = {
	'title': 'Контакты' ,
	}
	return render(request, 'aapp/contact.html', context)
    
#-------------------------------------------------------------
#Раздел новости с деталями и комментариями
def blog(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 4)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_page)
	context = {
	'title': 'Новости' ,
	'posts': posts ,
	'page': page,
	}
	return render(request, 'aapp/blog.html', context)


def post_details(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comments = post.comments.filter(active=True)
	if request.method == 'POST':
		comment_form = NewComment(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.save()
			comment_form = NewComment()
	else:
		comment_form = NewComment()
	context = {
        'title': post,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        }
	return render(request, 'aapp/details.html', context)



#------------------------------------------------------------
#Раздел Коран с сурами и аятами
def quran(request):
	qurans = Sura.objects.all()
	context = {
	'title': 'Коран' ,
	'qurans': qurans ,
	}
	return render(request, 'aapp/quran.html', context)

def sura_details(request, sura_id):
	sura = get_object_or_404(Sura, pk=sura_id)
	context = {
	'title': sura ,
	'sura': sura ,
	}
	return render(request, 'aapp/sura_details.html', context)
#-------------------------------------------------------------------

#Раздел Ислам в СПб с деталями комментариями
def islaminspb(request):
	islams = IslaminSpb.objects.all()
	paginator = Paginator(islams, 4)
	page = request.GET.get('page')
	try:
		islams = paginator.page(page)
	except PageNotAnInteger:
		islams = paginator.page(1)
	except EmptyPage:
		islams = paginator.page(paginator.num_page)
	context = {
	'title': 'Ислам в СПб' ,
	'islams': islams ,
	'page': page ,
	}
	return render(request, 'aapp/islaminspb.html', context)


def islam_details(request, islam_id):
	islam = get_object_or_404(IslaminSpb, pk=islam_id)
	# comments = islam.comments.filter(active=True)
	# if request.method == 'POST':
	# 	comment_form = NewComment(data=request.POST)
	# 	if comment_form.is_valid():
	# 		new_comment = comment_form.save(commit=False)
	# 		new_comment.islam = islam
	# 		new_comment.save()
	# 		comment_form = NewComment()
	# else:
	# 	comment_form = NewComment()
	context = {
        'title': islam,
        'islam': islam,
        # 'comments': comments,
        # 'comment_form': comment_form,
        }
	return render(request, 'aapp/islam_details.html', context)
#===================================================================


#Раздел семья с детальями 
def family(request):
	families = Family.objects.all()
	paginator = Paginator(families, 4)
	page = request.GET.get('page')
	try:
		families = paginator.page(page)
	except PageNotAnInteger:
		families = paginator.page(1)
	except EmptyPage:
		families = paginator.page(paginator.num_page)
	context = {
	'title': 'Семья' ,
	'families': families ,
	'page': page ,
	}
	return render(request, 'aapp/family.html', context)


def family_details(request, family_id):
	family = get_object_or_404(Family, pk=family_id)
	# fcomments = family.fcomments.filter(active=True)
	# if request.method == 'POST':
	# 	fcomment_form = NewComment(data=request.POST)
	# 	if fcomment_form.is_valid():
	# 		new_comment = fcomment_form.save(commit=False)
	# 		new_comment.family = family
	# 		new_comment.save()
	# 		fcomment_form = NewComment()
	# else:
	# 	fcomment_form = NewComment()
	context = {
        'title': family,
        'family': family,
        # 'fcomments': fcomments,
        # 'fcomment_form': fcomment_form,
        }
	return render(request, 'aapp/family_details.html', context)
#===================================================================



def articles(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 4)
	page = request.GET.get('page')
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_page)
	context = {
	'title': 'Статьи' ,
	'articles': articles ,
	'page': page ,
	}
	return render(request, 'aapp/articles.html', context)

def article_details(request, article_id):
	article = get_object_or_404(Article, pk=article_id)
	# comments = islamm.comments.filter(active=True)
	# if request.method == 'POST':
	# 	comment_form = NewComment(data=request.POST)
	# 	if comment_form.is_valid():
	# 		new_comment = comment_form.save(commit=False)
	# 		new_comment.islamm = islamm
	# 		new_comment.save()
	# 		comment_form = NewComment()
	# else:
	# 	comment_form = NewComment()
	context = {
        'title': article,
        'article': article,
        # 'comments': comments,
        # 'comment_form': comment_form,
        }
	return render(request, 'aapp/article_details.html', context)
#===================================================================


# from django.utils.safestring import mark_safe
# def save(self, *args, **kwargs):
#     self.text_field = mark_safe(self.text_field.replace("\n", "<br/>"))
#     super(Sura, self).save(*args, **kwargs)


