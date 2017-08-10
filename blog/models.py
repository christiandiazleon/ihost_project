from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=250)
    text = models.TextField()

    image = models.ImageField(
        upload_to='article_images',
        blank=False,
        null=False,
        verbose_name='Image'
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    # Asi puedo grabar una imagen por defecto
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

'''
class Comment(models.Model):
    article = models.ForeignKey('blog.Article',related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
'''


class Comment(models.Model):
    article = models.ForeignKey('blog.Article', related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    # We use the created field to sort comments in chronological order by default.
    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    # active boolean field that we will use to manually deactivate
    # inappropriate comments.
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.article)
