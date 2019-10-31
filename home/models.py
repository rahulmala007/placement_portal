from django.db import models


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
	branch = models.CharField(max_length=50, default="")
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



class BranchNumberPlaced(models.Model):
	branch = models.CharField(max_length=50, default="")




