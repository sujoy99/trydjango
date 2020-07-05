from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Product Title', widget=forms.TextInput(
        attrs={
            "placeholder" : "Type Title"
            }
        ))
    
    email = forms.EmailField()

    description = forms.CharField(label='Product Description', required=False, widget=forms.Textarea(
        attrs={
            "class"       : "new-class",
            "id"          : "new-id",
            "rows"        : 20,
            "cols"        : 20,
            "placeholder" : "Type Description"
            }
        ))
    price = forms.DecimalField(label='Product Price', initial=200.00, widget=forms.TextInput(
        attrs={
            "placeholder" : "Type Price"
            }
        ))
    class Meta:
        model = Product
        fields = [ 
            'title',
            'description',
            'price'
        ]

    # validation check
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("this is not a valid email")
        return email

# class RawProductForm(forms.Form):
#     title       = forms.CharField(label='Product Title', 
#         widget=forms.TextInput(
#             attrs = {
#                 "placeholder" : "Type Title"
#             }
#         )
#     )
#     description = forms.CharField(label='Product Description', required=False, 
#         widget=forms.Textarea(
#             attrs={
#                 "class"       : "new-class",
#                 "id"          : "new-id",
#                 "rows"        : 20,
#                 "cols"        : 20,
#                 "placeholder" : "Type Description"
#             }
#         )
#     )
#     price       = forms.DecimalField(label='Product Price', initial=200.00,
#         widget = forms.TextInput(
#             attrs={
#                 "placeholder" : "Type Price"
#             }
#         )
#      )
