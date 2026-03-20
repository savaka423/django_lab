from django.contrib.auth import authenticate, login as login_user
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect

from articles.models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, "article.html", {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            if Article.objects.filter(title=form['title']).exists():
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            if form["text"] and form["title"]:
                article = Article.objects.create(text=form["text"],
                                                 title=form["title"],
                                                 author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def registration(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password1 = request.POST.get("password1", "").strip()
        password2 = request.POST.get("password2", "").strip()

        form = {
            "username": username
        }

        if not username or not password1 or not password2:
            form["errors"] = "Все поля должны быть заполнены"
            return render(request, "registration.html", {"form": form})

        if password1 != password2:
            form["errors"] = "Пароли не совпадают"
            return render(request, "registration.html", {"form": form})

        if User.objects.filter(username=username).exists():
            form["errors"] = "Пользователь с таким именем уже существует"
            return render(request, "registration.html", {"form": form})

        User.objects.create_user(
            username=username,
            password=password1
        )

        return redirect("archive")

    return render(request, "registration.html")


def login(request):
    if request.method == "POST":

        form = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password")
        }

        if not form["username"] or not form["password"]:
            form["error"] = "Заполните все поля"
            return render(request, "login.html", {"form": form})

        user = authenticate(
            request,
            username=form["username"],
            password=form["password"]
        )

        if user is not None:
            login_user(request, user)
            return redirect("archive")

        else:
            form["error"] = "Нет аккаунта с таким сочетанием логина и пароля"
            return render(request, "login.html", {"form": form})

    return render(request, "login.html", {})