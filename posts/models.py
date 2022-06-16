from django.db import models

TYPE = (
    (0, 'FASHION'),
    (1, 'TRAVEL'),
)


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title

class Tag(models.Model):
    tag = models.CharField(max_length=221)

    def __str__(self):
        return self.tag

# get_<field_name>_display
def post_image_path(instance, filename):
    return 'posts/%s/%s' % (instance.get_type_display(), filename)


class Post(models.Model):
    title = models.CharField(max_length=221)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.IntegerField(choices=TYPE, null=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to=post_image_path)
    written_by = models.ImageField(upload_to=post_image_path , null=True)
    name = models.CharField(max_length=200 , null=True)
    content = models.TextField()
    written = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=221)
    avatar = models.ImageField(upload_to='comments', null=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
