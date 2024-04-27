from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=80, null=False)
    slag = models.SlugField(max_length=80, null=False)
    fullname = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=80, null=False)
    slag = models.SlugField(max_length=80, null=False)
    sort = models.IntegerField()
    cut = models.CharField(max_length=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class GroupsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(group=Sku.group)


class Sku(models.Model):
    name = models.CharField(max_length=80, null=False)
    slug = models.SlugField(max_length=80, null=False)
    gtin = models.CharField(max_length=14, null=False)
    prefix = models.CharField(max_length=5, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
