from django.db import models
# Create your models here.


BANK_CHOICE = (
    ('SBI','State Bank Of India'),
    ('HD','HDFC'),
    ('AX','AXIS'),
    ('CNR','canara')
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
    dsa_name = models.CharField(max_length=50, blank=True, null=True)
    dsa_number = models.CharField(max_length=15, blank=True, null=True)
    dsa_connector_code = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"