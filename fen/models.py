from django.db import models
from datetime import date

class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва кафедри")
    head = models.CharField(max_length=100, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"


class Program(models.Model):
    name = models.CharField(max_length=150, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=20, verbose_name="Код спеціальності")
    description = models.TextField(verbose_name="Повний опис")
    coordinator_name = models.CharField(max_length=100, verbose_name="Ім'я координатора набору")
    coordinator_contact = models.CharField(max_length=100, verbose_name="Контакт координатора")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs', verbose_name="Випускова кафедра")
    disciplines = models.TextField(verbose_name="Список дисциплін")

    def __str__(self):
        return f"{self.code} — {self.name}"

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"


class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я викладача")
    position = models.CharField(max_length=100, verbose_name="Посада")
    degree = models.CharField(max_length=100, blank=True, null=True, verbose_name="Науковий ступінь")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers', verbose_name="Кафедра")

    def __str__(self):
        return f"{self.name} ({self.position})"

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"


class HomePageContent(models.Model):
    title = models.CharField(max_length=200, default="Факультет економічних наук (ФЕН) НаУКМА", verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис факультету")
    contacts = models.TextField(verbose_name="Контактна інформація")

    def __str__(self):
        return "Налаштування головної сторінки"

    class Meta:
        verbose_name = "Контент головної сторінки"
        verbose_name_plural = "Контент головної сторінки"


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=200, verbose_name="Університет")
    country = models.CharField(max_length=100, verbose_name="Країна")
    languages = models.CharField(max_length=200, verbose_name="Мови навчання")
    slots = models.IntegerField(verbose_name="Кількість місць")
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")

    @property
    def is_active(self):
        return self.deadline >= date.today()

    def __str__(self):
        return f"{self.university}, {self.country}"