from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Branch(models.Model):
	branchName = models.CharField(max_length=50, default="")
	num= models.IntegerField(default=0,validators=[MinValueValidator(0)])

	def __str__(self):
		return self.branchName

BRANCH_CHOICES = [
	('CSE', 'Computer Science and Engineering'),
	('MNC', 'Mathematics and Computing'),
	('ECE', 'Electronics and Communication Engineering'),
	('EEE', 'Electronics and Electrical Engineering'),
	('ME', 'Mechanical Engineering'),
	('CE', 'Civil Engineering'),
	('CL', 'Chemical Engineering'),
	('EP' , 'Engineering Physics'),
	('CST','Chemical Science and Technology'),
	('BT','Biotechnology'),
]

class Student(models.Model):
	name = models.CharField(max_length=200)

	PROGRAM_CHOICES = [
        ('BTech', 'Bachelors of Technology'),
        ('BDes', 'Bachelor of Design'),
        ('MTech', 'Master of Technology'),
        ('MDes', 'Master of Design'),
    ]

	programs = models.CharField(
		max_length=5,
        choices=PROGRAM_CHOICES,
        default='BTech',
	)	
	day=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(0)],default=0)
	branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
	company = models.CharField(max_length=100, blank=True)
	placed = models.BooleanField(default=False)
	sector = models.CharField(max_length=100, blank=True)
	profile = models.CharField(max_length=100, blank=True)
	SLOT_CHOICES = [
        ('S1', 'Slot 1'),
        ('S2', 'Slot 2'),
        ('S3', 'Slot 3'),
    ]

	slot = models.CharField(
		max_length=2,
        choices=SLOT_CHOICES,
        blank=True
	)

	def __str__(self):
		return self.name





class Day(models.Model):
	dayNum=models.IntegerField(validators=[MinValueValidator(0)],default=0)
	num = models.IntegerField(default=0,validators=[MinValueValidator(0)])
	branch=models.ForeignKey(Branch,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.dayNum}-{self.branch.branchName}'







