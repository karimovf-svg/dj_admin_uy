from django.db import models

class Kurs(models.Model):
    title = models.CharField(max_length=50, verbose_name="Kurs nomi")
    start_time = models.TimeField(verbose_name="Boshlanish vaqti")
    end_time = models.TimeField(verbose_name="Tugash vaqti")
    description = models.TextField(verbose_name="Tavsif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Student(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="To‘liq ismi")
    phone_number = models.CharField(max_length=15, verbose_name="Telefon raqami")
    email = models.EmailField(unique=True, verbose_name="Email")
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, verbose_name="Kurs")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Talaba"
        verbose_name_plural = "Talabalar"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name