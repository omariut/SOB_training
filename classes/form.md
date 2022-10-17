# Django Forms
**Syntax:**  Django Fields work like Django Model Fields and have the syntax:
```
 field_name = forms.FieldType(**options) 
 ```
 ### Creating Django Forms
 #### Syntax:
```
from django import forms
        
class FormName(forms.Form):
         # each field would be mapped as an input field in HTML
        field_name = forms.Field(**options)
```
**Example**
```from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField()
    text=forms.CharField()
```

### Render Django Forms:
{{ form.as_table }} will render them as table cells wrapped in <tr> tags
{{ form.as_p }} will render them wrapped in <p> tags
{{ form.as_ul }} will render them wrapped in <li> tags

**view**
```
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
```
**template**
```
<form action = "" method = "post">
	{% csrf_token %}
	{{form }}
	<input type="submit" value=Submit">
</form>
```
![form](/images/form/form1.png "form")

### Create Django Form from Models

**model**
```
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

**form**
```
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
```
### Basic form data types and fields list

![field1](/images/form/field1.png "field1")
![field2](/images/form/field2.png "field2")

### Core Field Arguments
![option](/images/form/option.png "option")



## Render HTML Forms (GET & POST) in Django
#### GET:
GET, by contrast, bundles the submitted data into a string, and uses this to compose a URL. The URL contains the address where the data must be sent, as well as the data keys and values. You can see this in action if you do a search in the Django documentation, which will produce a URL of the form https://docs.djangoproject.com/search/?q=forms&release=1.

#### POST: 
Any request that could be used to change the state of the system – for example, a request that makes changes in the database – should use POST.

**template**
```
<form action = "" method = "get">
	<label for="your_name">Your name: </label>
	<input id="your_name" type="text" name="your_name">
	<input type="submit" value="OK">
</form>

```
**view**
```
def test_form(request):
    print(request.GET)
    print(request.POST)
    return render(request, 'blog/test_form.html')

```
## Widget
**form**
```
class PostForm(forms.Form):
    title = forms.CharField()
    #text=forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
```
**template**
```
<form action = "" method = "post">
	{% csrf_token %}
    {{ form.as_p }}
	<input type="submit" value=Submit">
</form>
```
![form2](/images/form/form2.png "form2")

**More widget: https://docs.djangoproject.com/en/4.1/ref/forms/widgets/**
## ModelForm
**model**
```
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```
**form**
```
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
````

**view**
```def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
  ```
## Assignment
**Create a view to edit the posts.**