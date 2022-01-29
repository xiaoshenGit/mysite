from django.test import TestCase


# Create your tests here.
# class ForeignKey(to, on_delete,**options):
#     pass

# 顺序，dev:git add . --git commit--  git push
# master:git pull
# dev---master右键merge
# github处理请求，解决冲突
class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pass


if __name__ == '__main__':
    Car()









