from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(help_text="Value from 0 to 100")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text="Comma-separated list")
    link = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class About(models.Model):
    heading = models.CharField(max_length=200)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.heading


class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=100, help_text="FontAwesome class, e.g. fa fa-github")

    def __str__(self):
        return self.platform

class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/', blank=True, null=True)
    link = models.URLField()
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} at {self.institution}"
