from random import randint
from webapp.cat_db import CatDB


class Cat:

    def __init__(self):
        self.name = None
        self.age = 1
        self.satiety_level = 40
        self.happiness_level = 40
        self.is_sleeping = False
        self.img_path = CatDB.img_path["netrual"]

    def feed(self):
        if not self.is_sleeping:
            self.satiety_level += 15
            if self.satiety_level > 100:
                self.happiness_level -= 30
            else:
                self.happiness_level += 5

        self.check_cat()
        self.check_cat_img()

    def play(self):
        if not self.is_sleeping:
            self.happiness_level += 15
            self.satiety_level -= 10
            if randint(1, 3) == 1:
                self.happiness_level = 0
        else:
            self.is_sleeping = False
            self.happiness_level -= 5

        self.check_cat()
        self.check_cat_img()

    def sleep(self):
        self.is_sleeping = True
        self.check_cat()
        self.check_cat_img()

    def check_cat(self):
        if self.satiety_level < 0:
            self.satiety_level = 0
        elif self.satiety_level > 100:
            self.satiety_level = 100

        if self.happiness_level < 0:
            self.happiness_level = 0
        elif self.happiness_level > 100:
            self.happiness_level = 100

    def check_cat_img(self):
        if self.happiness_level >= 70:
            self.img_path = CatDB.img_path["happy"]
        elif self.happiness_level >= 30:
            self.img_path = CatDB.img_path["netrual"]
        else:
            self.img_path = CatDB.img_path["sad"]
