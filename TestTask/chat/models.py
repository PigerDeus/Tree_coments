from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    class Meta(object):
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    id = models.AutoField(
    primary_key = True)
    text = models.TextField(
        max_length=2000,
        help_text='Please, your Comment',
        verbose_name='Comment',
        blank=True)
    seq=models.PositiveSmallIntegerField(default=0)
    public_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    User,
    on_delete= models.CASCADE,)


class TreeOrderField(models.CharField):
	def pre_save(self, model_instance, add):
		if add:
			parent=(model_instance.parent or model_instance.coment);
			if parent.seq<1000:
				parent.seq+=1;
				parent.save();
			else:
				pass
			value=('%s%03d'%(getattr(parent,
                                    self.attname, ''),
                                    parent.seq,))[:255]
			setattr(model_instance,
                    self.attname,
                    value)
			return value
		return models.CharField.pre_save(self, model_instance, add)


class SubComment(models.Model):
    coment=models.ForeignKey(
                            Comment,
                            on_delete = models.CASCADE)
    parent=models.ForeignKey(
                            'self',
                            blank=True,
                            null=True,
                            related_name='child_set',
                            on_delete = models.CASCADE)
    author=models.ForeignKey(
                            User,
                            on_delete= models.CASCADE,)
    text=models.TextField()
    pub_date=models.DateTimeField(
                                'date published',
                                auto_now_add=True)
    path=TreeOrderField(
                        max_length=255,
                        blank=True)
    seq=models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering=[ 'pub_date', ]
