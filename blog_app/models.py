from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
## 1 -1 relationship with User model
# 1 user can have only 1 profile => 1
#1 profile is associated with only 1 user => 1
#OneToOneField() => Any Model

## 1 - M relationship with User model
# 1 user can have many posts => M
# 1 post is associated to only 1 user => 1
# in  django use ForeignKey() => Use in many side Model

## M-M Relationship with User model
# 1 students can learn many teachers => M
# 1 teacher can teach many students => M
#ManyToManyField() => Any Place