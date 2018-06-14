# Multiple-value field for Django forms

## The problem
Say we want to use a Django form to validate form input such as the following:

```
?foo=spam&foo=egg&foo=chips
```
Django can parse this query-string to generate a list:

```
>>> request.GET.getlist("foo")
['spam', 'egg', 'chips']
```

...but it is not yet capable of validating the input using `django.forms`.


## How to use

Say for example, we want to validate a list of email addresses, with a query-string such as the following:
```
?email=foo@bar.com&email=spam@egg.com
```
Here are the steps we would take:

1. Install this module (e.g. using `pip install django_multivalueformfield`)
2. Define a form like the following:
```
import django.forms as forms

from multivaluefield import MultiValueField

class MultiEmailForm(forms.Form):
    emails = MultiValueField(forms.EmailField(), "email")
```
3. Pass the `QueryDict` into the form and validate as per usual:
```
form = MultiEmailForm(request.GET)
if form.is_valid:
    emails = form.cleaned_data["emails"]
    # do something with emails
else:
    errors = form.errors
    # do something with errors
```
