from django.db import models
from ..user.models import User

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="todos")
    title=models.CharField(max_length=100,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    complate=models.BooleanField(default=False)
    complate_at=models.DateTimeField(null=True)

    class Meta:

        db_table="todo_project_todo"

        indexes=[
            models.Index(
                fields=["user","-created_at"]
            )
        ]