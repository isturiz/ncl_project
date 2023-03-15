from django.db import models

# Create your models here.
class Representative(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    
class Student(models.Model):
    AGE_CATEGORIES = (
        ('A', '3 to 5 years old'),
        ('B', '6 to 9 years old'),
        ('C', '10 to 12 years old'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()
    age_category = models.CharField(max_length=1, choices=AGE_CATEGORIES)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}: {self.amount} ({self.payment_date})"