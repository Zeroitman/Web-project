from django.db import models


class Employee(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=30)
    surname = models.CharField(verbose_name="Фамилие", max_length=50)
    middle_name = models.CharField(verbose_name="Отчество", max_length=50, blank=True)
    position = models.CharField(verbose_name="Должность", max_length=100)
    employment_date = models.DateField(verbose_name="Дата приема на работу")
    salary = models.PositiveIntegerField(verbose_name="Размер зарплаты в рублях")

    def __str__(self):
        return "%s. %s %s. Должность: %s." % (self.id, self.surname, self.name, self.position)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
