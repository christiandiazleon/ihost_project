from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from django.utils.text import slugify
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100, blank=True)
    text = models.TextField()

    image = models.ImageField(
        upload_to='article_images',
        blank=False,
        null=False,
        verbose_name='Image'
        # width_field="width_field",
        # height_field="height_field"
        # https://www.youtube.com/watch?v=Bmvd1O5pNIY&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=29
    )
    # width_field=models.IntegerField(default=0)
    # height_field=models.IntegerField(default=0)

    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    # Asi puedo grabar una imagen por defecto
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    #class Meta:
        #ordering = ["-created_date", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Article.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_article_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_article_receiver, sender=Article)



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
        ordering = ('updated',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.article)
