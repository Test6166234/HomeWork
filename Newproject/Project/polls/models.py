from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    # Поле order удалено

    def __str__(self):
        return self.title

    class Meta:
        pass # Класс Meta пустой, сортировка по умолчанию Django ID

class TaskStep(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'готово' if self.done else 'не готово'})"

