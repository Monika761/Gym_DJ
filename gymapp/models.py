from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.name} - {self.amount}"


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=(('Present', 'Present'), ('Absent', 'Absent')))

    def __str__(self):
        return f"{self.member.name} - {self.date}"
