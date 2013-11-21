from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=200, null=False)
    reg_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)

class UserForm(ModelForm):
    class Meta:
        model = User
        #fields = ['email', 'name', 'password']
        #exclude = ['reg_dt']
        
class Book(models.Model):
    isbn = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=200, null=False)
    user_score = models.FloatField()
    total_page = models.IntegerField(null=False)
    current_page = models.IntegerField()
    image_url = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    pub_date = models.CharField(max_length=8)
    link_naver = models.TextField()
    reg_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

class BookForm(ModelForm):
    class Meta:
        model = Book
    
class BestWord(models.Model):
    best_word = models.CharField(primary_key=True, max_length=400, null=False)
    reg_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)

class BestWordForm(ModelForm):
    class Meta:
        model = BestWord

class Review(models.Model):
    review_name = models.CharField(primary_key=True, max_length=200, null=False)
    review_contents = models.TextField(null=False)
    reg_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)

class ReviewForm(ModelForm):
    class Meta:
        model = Review

class ReadingNow(models.Model):
    current_ratio = models.FloatField(null=False)
    current_page = models.IntegerField(null=False)
    reg_dt = models.DateTimeField(auto_now_add=True)
    modify_dt = models.DateTimeField(auto_now=True)
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    
class ReadingNowForm(ModelForm):
    class Meta:
        model = ReadingNow