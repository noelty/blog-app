from django.db import migrations
from django.utils.text import slugify

def backfill_slugs(apps, schema_editor):
    Post = apps.get_model("blog", "Post")   # historical Post (gotcha #1)
    for post in Post.objects.all():
        if post.slug:
            continue                          # skip any already-set
        base = slugify(post.title)
        slug = base
        n = 1
        while Post.objects.filter(slug=slug).exclude(pk=post.pk).exists():
            slug = f"{base}-{n}"
            n += 1
        post.slug = slug
        post.save()                           # historical model has no custom save() — fine, we set slug ourselves

class Migration(migrations.Migration):
    dependencies = [("blog", "0012_post_slug")]
    operations = [
        migrations.RunPython(backfill_slugs, migrations.RunPython.noop),
    ]
