from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'category'
    verbose_name_plural = 'categories'

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
          verbose_name = 'author'
          verbose_name_plural = 'authors'

    def get_full_name(self):
        return f"{self.first_name}, {self.last_name}"



class BookModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.CASCADE,
        related_name='book',
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='book',
    )
    pages = models.IntegerField()
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'book'




























