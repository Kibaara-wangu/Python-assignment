from django.urls import path

from api.views import Class_PeriodListViews, ClassroomListViews, CourseListViews, StudentListViews, TeacherListViews, StudentDetailView

urlpatterns = [
    path("Students/",StudentListViews.as_view(),name = "student_list_view"),
    path("Teachers/",TeacherListViews.as_view(),name = "teacher_list_view"),
    path("Courses/",CourseListViews.as_view(),name = "course_list_view"),
    path("Classroom/",ClassroomListViews.as_view(),name = "classroom_list_view"),
    path("Class_Period/",Class_PeriodListViews.as_view(),name = "class_period_list_view"),
    path("Students/<int:id>/",StudentDetailView.as_view(), name = "student_detail_view"),
]