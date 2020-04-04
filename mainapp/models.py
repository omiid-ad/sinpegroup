from django.db import models


class Crew(models.Model):
    profile_picture = models.ImageField(upload_to='crew_pictures', default='crew_pictures/default.png', blank=True,
                                        null=True, verbose_name="عکس پروفایل")
    full_name = models.CharField(max_length=100, verbose_name="نام کامل")
    skill = models.CharField(max_length=100, verbose_name="حرفه")
    active = models.BooleanField(default=True, verbose_name="عضو فعال")

    def __str__(self):
        if self.active:
            return self.full_name + " - " + self.skill + "(فعال)"
        elif not self.active:
            return self.full_name + " - " + self.skill + "(غیرفعال)"


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان خدمت")
    active = models.BooleanField(default=True, verbose_name="خدمت فعال")

    def __str__(self):
        if self.active:
            return self.title + "(فعال)"
        elif not self.active:
            return self.title + "(غیرفعال)"


class Portfolio(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="خدمت مربوطه")
    big_image_or_video = models.FileField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                                          null=True, verbose_name="عکس یا فیلم نمونه")
    image1 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه اول")
    image2 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه دوم")
    image3 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه سوم")
    image4 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه چهارم")
    image5 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه پنجم")
    image6 = models.ImageField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                               null=True, verbose_name="عکس نمونه ششم")
