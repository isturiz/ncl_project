from django.urls import path


from .views import *


#app_name = 'ncl_app'

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    # Una posible modularización para todos los edit, podría funcionar, en donde item = student or item = teacher
    # path('student/edit/item/<int:item_id>', ItemViews.edit_form, name='edit_form'),

    path('student/', StudentViews.index, name='student'), 
    path('student/register/', StudentViews.register_form, name='register_form_student'), 
    path('student/save/', StudentViews.register_form_process, name='register_form_process__student'), 
    path('student/edit/<int:student_id>', StudentViews.edit_form, name='edit_form__student'),
    path('student/update/<int:student_id>', StudentViews.edit_form_process, name='edit_form_process__student'),
    path('student/<int:student_id>/delete/', delete_student, name='delete_student'),

    path('representative/', RepresentativeViews.index, name='representative'), 
    path('representative/register/', RepresentativeViews.register_form, name='register_form_representative'), 
    path('representative/save/', RepresentativeViews.register_form_process, name='register_form_process__representative'), 
    path('representative/edit/<int:representative_id>', RepresentativeViews.edit_form, name='edit_form__representative'),
    path('representative/update/<int:representative_id>', RepresentativeViews.edit_form_process, name='edit_form_process__representative'),
    path('representative/<int:representative_id>/delete/', delete_representative, name='delete_representative'),

    #ex: ncl/teacher
    path('teacher/', TeacherViews.index, name='teacher'), 
    path('teacher/register/', TeacherViews.register_form, name='register_form_teacher'), 
    path('teacher/save/', TeacherViews.register_form_process, name='register_form_process__teacher'), 
    path('teacher/edit/<int:teacher_id>', TeacherViews.edit_form, name='edit_form__teacher'),
    path('teacher/update/<int:teacher_id>', TeacherViews.edit_form_process, name='edit_form_process__teacher'),
    path('teacher/<int:teacher_id>/delete/', delete_teacher, name='delete_teacher'),


    #ex: ncl/payment
    path('payment/', PaymentViews.index, name='payment'), 
    path('payment/register/', PaymentViews.register_form, name='register_form_payment'), 
    path('payment/save/', PaymentViews.register_form_process, name='register_form_process__payment'), 
    path('payment/edit/<int:payment_id>', PaymentViews.edit_form, name='edit_form__payment'),
    path('payment/update/<int:payment_id>', PaymentViews.edit_form_process, name='edit_form_process__payment'),
    path('payment/<int:payment_id>/delete/', delete_payment, name='delete_payment'),


    path('inscription/', InscriptionViews.index, name='inscription'), 
    path('inscription/register/', InscriptionViews.register_form, name='register_form_inscription'), 
    path('inscription/save/', InscriptionViews.register_form_process, name='register_form_process__inscription'), 
    path('inscription/edit/<int:inscription_id>', InscriptionViews.edit_form, name='edit_form__inscription'),
    path('inscription/update/<int:inscription_id>', InscriptionViews.edit_form_process, name='edit_form_process__inscription'),
    path('inscription/<int:inscription_id>/delete/', delete_inscription, name='delete_inscription'),

    #ex: ncl/course
    path('course/', CourseViews.index, name='course'), 
    path('course/register/', CourseViews.register_form, name='register_form_course'), 
    path('course/save/', CourseViews.register_form_process, name='register_form_process__course'), 
    path('course/edit/<int:course_id>', CourseViews.edit_form, name='edit_form__course'),
    path('course/update/<int:course_id>', CourseViews.edit_form_process, name='edit_form_process__course'),
    path('course/<int:course_id>/delete/', delete_course, name='delete_course'),

    #ex: ncl/inscription

    path('reports/', ReportsView.index, name='reports'), 
    path('generar_pdf/', ReportsView.generar_pdf, name='generar_pdf'),
    path('test_report/', ReportsView.test_report, name='test_report'),
    
]
