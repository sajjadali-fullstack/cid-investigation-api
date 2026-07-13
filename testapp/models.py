from django.db import models

# Create your models / SQL Table here.

# Officer
class Officer(models.Model):
    RANK = (

        ('ACP',' ACP'),
        ('High Commission SOS Officer', 'High Commission SOS Officer'),

        ('Inspector', 'Inspector'),
        ('Sub Inspector', 'Sub Inspector'),
        ('Senior Inspector', 'Senior Inspector'),
        
        ('Assistant Forensic Expert', 'Assistant Forensic Expert'),
        ('Senior Forensic Expert', 'Senior Forensic Expert'),
        ('Lab Assistant', 'Lab Assistant'),
        ('Chief Forensic Expert', 'Chief Forensic Expert'),
        ('Head of Forensic Lab', 'Head of Forensic Lab'),

    )

    name = models.CharField(max_length=250)
    rank = models.CharField(max_length=200, choices=RANK)
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.rank} {self.name}"


# Criminal
class Criminal(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=250, blank=True, null=True)
    # nickname / jooti paichan 
    alias = models.CharField(max_length=150, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER,blank=True, null=True)
    criminal_history = models.TextField(null=True, blank=True)
    wanted = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    


# Case
class Case(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Investigating', 'Investigating'),
        ('Solved', 'Solved'),
        ('Closed', 'Closed'),
    )

    title = models.CharField(max_length=200)
    case_number = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date_registered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS)

    officer = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE,
        related_name="cases"
    )


    criminal = models.ForeignKey(
        Criminal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cases"
    )

    def __str__(self):
        return self.case_number
    


# Evidence
class Evidence(models.Model):

    EVIDENCE_TYPE = (
        ('Fingerprint', 'Fingerprint'),
        ('DNA', 'DNA'),
        ('Weapon', 'Weapon'),
        ('Photo', 'Photo'),
        ('Video', 'Video'),
        ('Document', 'Document'),
        ('CCTV Footage', 'CCTV Footage'),
        ('Eye Witness', 'Eye Witness'),
        ('Voice Recording', 'Voice Recording'),
        ('Mobile Call Records', 'Mobile Call Records'),
        ('Liquids', 'Liquids'),
        ('Electronic / Audio Threat Tape', 'Electronic / Audio Threat Tape'),
        ('RDX Explosive Residue / Timer Link', 'RDX Explosive Residue / Timer Link'),
        ('Other', 'Other'),



    )

    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name='evidence'
    )

    evidence_type = models.CharField(max_length=300, choices=EVIDENCE_TYPE)
    description = models.TextField()
    collected_by = models.ForeignKey(
        Officer,
        on_delete=models.CASCADE
    )
    collected_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.evidence_type



# Witness
class Witness(models.Model):
    case = models.ForeignKey(
        Case,
        on_delete=models.CASCADE,
        related_name='witnesses'
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    statement = models.TextField()

    def __str__(self):
        return self.name
    

