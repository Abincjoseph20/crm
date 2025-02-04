from django.db import models
# # Create your models here.





class DSA(models.Model):
    dsa_name = models.CharField(max_length=50)
    dsa_code = models.CharField(max_length=50)
    dsa_phone_number = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.dsa_name


BANK_CHOICE = (
    ('SBI','State Bank Of India'),
    ('HDFC','HDFC'),
    ('AXIX','AXIS'),
    ('cANARA','canara')
)

PRODUCT_CHOICE = (
    ('HL','Home LONE'),
    ('PL','Personal Loan'),
    ('CL','Car Loan'),
    ('BL','Business Loan'),
    ('RF','Re-Fenace'),
)

STATUS_CHOICES = (
    ('login_submit', 'Login Submit'),
    ('login_complete', 'Login Complete'),
    ('tec_completed', 'TEC Completed'),
    ('legal_completed', 'Legal Completed'),
    ('disp', 'Dispatched'),
    ('reject', 'Rejected')
)

TYPE_CHOICES = (
    ('DSA', 'DSA'),
    ('SELF', 'Self')
)

class Customer(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    product = models.CharField(choices=PRODUCT_CHOICE, max_length=20)
    bank = models.CharField(choices=BANK_CHOICE, max_length=20)
    
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    type = models.CharField(choices=TYPE_CHOICES, max_length=4)
    dsa = models.ForeignKey(DSA, on_delete=models.SET_NULL, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    

class Task(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True,null=True)
    task_date = models.DateField()
    task_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.task_date} {self.task_time}"
    
    
    