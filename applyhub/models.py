from django.db import models
from django.contrib.auth.models import User



###########################
#### Application model ####
###########################
class Application(models.Model):
    """
    Represents a job application submitted by a user.

    The Application model stores information related to job applications,
    including the position applied for, company details, application status, 
    and the method of application. Each application is linked to a specific user 
    through a foreign key relationship, allowing users to manage and track 
    their job applications effectively.

    Fields:
    - position: The title of the job position applied for.
    - description: A detailed description of the job or application.
    - slug: A URL-friendly identifier for the application, unique for each entry.
    - position_level: The level of the position (Junior, Associate, Mid senior, Senior).
    - company_name: The name of the company where the application is submitted.
    - date_applied: The date when the application was submitted.
    - status: The current status of the application (Applied, Interview, Offer, Rejected).
    - applied_method: The method used for applying (Website, Job board, Referral, Email).
    - location: The location of the job or the company.
    - job_link: A link to the job listing or application page.
    - recruiter_contact: Contact information for the recruiter (if applicable).
    - follow_up_date: The date when the user plans to follow up on the application.
    - created_on: The timestamp for when the application was created (automatically set).
    - applicant: A foreign key linking to the User model, indicating which user submitted the application.
    
    Meta:
    - Ordering: Applications are ordered by the creation date, with the most recent first.
    """
    # Choices for the position level of the application
    POSITION_LEVEL_CHOICES = (
        ("Junior", "Junior"),
        ("Associate", "Associate"),
        ("Mid senior", "Mid senior"),
        ("Senior", "Senior")
    )

    # Choices for the status of the application
    STATUS_CHOICES = (
        ("Applied", "Applied"),
        ("Interview", "Interview"),
        ("Offer", "Offer"),
        ("Rejected", "Rejected")
    )

    # Choices for the method used to apply for the job
    APPLIED_METHOD_CHOICES = (
        ("Website", "Website"),
        ("Job board", "Job board"),
        ("Referral", "Referral"),
        ("Email", "Email")
    )

    # Fields
    position = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    position_level = models.CharField(max_length=10, choices=POSITION_LEVEL_CHOICES, default="Junior")
    company_name = models.CharField(max_length=255)
    date_applied = models.DateField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="Applied")
    applied_method = models.CharField(max_length=9, choices=APPLIED_METHOD_CHOICES, default="website")
    location = models.CharField(max_length=255)
    job_link = models.URLField(max_length=300, null=True, blank=True)
    recruiter_contact = models.CharField(max_length=255, null=True, blank=True)
    follow_up_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    class Meta:
        ordering = ["-created_on"]


