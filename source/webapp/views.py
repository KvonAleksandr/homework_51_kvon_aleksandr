from django.shortcuts import render
from webapp.cat_db import CatDB
from webapp.cat import Cat
from django.http import HttpResponseRedirect


def home(request):
    if request.method == 'GET':
        return render(request, "home.html")
    else:
        cat = Cat()
        new_cat = {
            "name": request.POST.get("name"),
            "age": cat.age,
            "satiety_level": cat.satiety_level,
            "happiness_level": cat.happiness_level,
            "is_sleeping": cat.is_sleeping,
            "img_path": cat.img_path
        }
        # print(new_cat)
        CatDB.cats.append(new_cat)
        # print(CatDB.cats)
        return HttpResponseRedirect("/cat_stats")


def cat_stats(request):
    cat = Cat()
    cat_data = CatDB.cats[0]
    cat.name = cat_data.get("name")
    cat.age = cat_data.get("age")
    cat.satiety_level = cat_data.get("satiety_level")
    cat.happiness_level = cat_data.get("happiness_level")
    cat.is_sleeping = cat_data.get("is_sleeping")
    cat.img_path = cat_data.get("img_path")
    print(cat_data)

    if request.method == 'GET':
        context = {"cat": cat, "img_path": CatDB.img_path}
        return render(request, "cat_stats.html", context)
    else:
        action = request.POST.get("action")
        if action == "feed":
            cat.feed()
            # print(cat.img_path)
        elif action == "play":
            cat.play()
            # print(cat.is_sleeping)
        elif action == "sleep":
            cat.sleep()
            # print(cat.is_sleeping)
        cat_upd = {
            "name": cat.name,
            "age": cat.age,
            "satiety_level": cat.satiety_level,
            "happiness_level": cat.happiness_level,
            "is_sleeping": cat.is_sleeping,
            "img_path": cat.img_path
        }
        CatDB.cats[0] = cat_upd
        return HttpResponseRedirect("/cat_stats")
