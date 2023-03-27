from django.contrib import admin
from .models import Student, AgeCategory,Representative, Course, Teacher, Payment, Inscription

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'birthdate', 'age_category', 'representative')

# class AgeCategoryAdmin(admin.ModelAdmin):
    # list_display = ('name')

class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_teacher_names')

    def get_teacher_names(self, obj):
        return ", ".join([t.first_name for t in obj.teacher.all()])

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'phone_number')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'payment_date', 'reference_number', 'amount', 'description')

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')

admin.site.register(Student, StudentAdmin)
admin.site.register(AgeCategory)
admin.site.register(Representative, RepresentativeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Inscription, InscriptionAdmin)
