from django.test import TestCase


# Create your tests here.
# class ForeignKey(to, on_delete,**options):
#     pass

# 啦啦啦啦啦
class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pass

if __name__ == '__main__':
    Car()
    Manufacturer()









