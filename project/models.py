from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Department(MPTTModel):
    class Meta:
        db_table = 'department'
        verbose_name_plural = "Отделы"
        verbose_name = "Отдел"
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=50, unique=True, verbose_name="Название отдела")
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            verbose_name=u'Родительская категория отдела', db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Employee(models.Model):
    class Meta:
        db_table = 'employee'
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"

    name = models.CharField(verbose_name="Имя", max_length=30)
    surname = models.CharField(verbose_name="Фамилие", max_length=50)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, blank=True)
    position = models.CharField(verbose_name="Должность", max_length=100)
    employment_date = models.DateField(verbose_name="Дата приема на работу")
    salary = models.PositiveIntegerField(verbose_name="Размер зарплаты в рублях")
    department = TreeForeignKey(Department, null=True, blank=True, related_name='cat', on_delete=models.CASCADE)

    def __str__(self):
        return "%s. %s %s. Должность: %s." % (self.id, self.surname, self.name, self.position)

