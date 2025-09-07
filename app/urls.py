from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashbord.dashboard_view, name='dashboard'),
    path("list/", views.ListView.all_info, name='list_view'),
    path("register/", views.Register_view.register, name='register_page'),
    path("login/", views.Login_View.login_user, name='login_page'),
    path("log_out/", views.Log_Out_View.log_out, name='log_out_page'),
    path("create/", views.Create_View.create_autho, name='create_author'),
    path('update/<int:id>/', views.Update_View.update_page, name='update_view'),
    path('delete/<int:id>/', views.Delete_View.delete_page, name='delete_view'),
# books
    path("books-list/", views.Book_List_view.all_books, name='books'),
    path("books-create/", views.Book_Create.create_books, name='create_books'),
    path("books-update/<int:id>/", views.Update_Book.update_books, name='update_books'),
    path("books-delete/<int:id>/", views.Delete_Books.delete_b, name='delete_books'),
    






]
