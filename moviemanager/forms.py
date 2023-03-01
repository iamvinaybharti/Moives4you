from django import forms
from moviemanager.models import *



class BookingsForm(forms.ModelForm):
    t = [("1", "09-12 A.M"), ("2", "12-03 P.M"), ("3", "03-06 P.M"), ("4", "06-09 P.M"), ("3", "09-12 P.M")]
    s = [("1", "Platinum"), ("2", "Gold"), ("3", "Silver")]
    movie = forms.CharField(label="Movie Name :", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Movie Name"}),  max_length=20)
    time = forms.ChoiceField(label="Select Time :", choices=t)
    date = forms.DateField(label="Select Date :", widget=forms.SelectDateWidget)
    name = forms.CharField(label="Your Name :", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Your Name"}),max_length=20)
    email = forms.EmailField(label="Your Email :",widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Your Email"}) , max_length=100)
    number = forms.IntegerField(label="Your Number :", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Your Number"}))
    seattype = forms.ChoiceField(label="Seat Type :", choices=s)
    totalseat = forms.IntegerField(label="No. of Seats :", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Enter Total Seat"}))

    class Meta():
        model = Bookings
        fields = ['movie', 'name', 'email', 'number', 'totalseat', 'seattype', 'date', 'time']
