from django import forms

class UserForm(forms.Form):
    email = forms.CharField(max_length=50)
    name = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=200, required=True)
    #reg_dt = forms.DateTimeField(auto_now_add=True)
    #modify_dt = forms.DateTimeField(auto_now=True)
    
class BookForm(forms.Form):
    yes24_product_no = forms.IntegerField()
    book_name = forms.CharField(max_length=200, required=True)
    user_score = forms.IntegerField()
    total_page = forms.IntegerField(required=True)
    current_page = forms.IntegerField()
    #reg_dt = forms.DateTimeField(auto_now_add=True)
    #modify_dt = forms.DateTimeField(auto_now=True)
    
class BestWordForm(forms.Form):
    best_word = forms.CharField(max_length=400, required=True)
    #reg_dt = forms.DateTimeField(auto_now_add=True)
    #modify_dt = forms.DateTimeField(auto_now=True)

class ReviewForm(forms.Form):
    review_name = forms.CharField(max_length=200, required=True)
    review_contents = forms.CharField(required=True)
    #reg_dt = forms.DateTimeField(auto_now_add=True)
    #modify_dt = forms.DateTimeField(auto_now=True)

class ReadingNowForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    #reg_dt = forms.DateTimeField(auto_now_add=True)
    #modify_dt = forms.DateTimeField(auto_now=True)
