from django.contrib import admin
from .models import User,Subject,Quiz,Student,TakenQuiz,StudentAnswer
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)