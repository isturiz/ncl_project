from django.db import models

class Representative(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):

    AGE_CATEGORIES = (
        ('A', '1 a 3 años de edad'),
        ('B', '4 a 6 años de edad'),
        ('C', '7 a 9 años de edad'),
        ('D', '10 a 12 años de edad'),
        ('E', 'Adolescente'),
    )


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    birthdate = models.DateField()
    age_category = models.CharField(max_length=1, choices=AGE_CATEGORIES)
    representative = models.ForeignKey(Representative, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment_date = models.DateField()
    reference_number = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.amount}"

class Inscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.course.name}"
