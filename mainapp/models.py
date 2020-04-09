from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe


class Crew(models.Model):
    profile_picture = models.ImageField(upload_to='crew_pictures', default='crew_pictures/default.png', blank=True,
                                        null=True, verbose_name="عکس پروفایل")
    full_name = models.CharField(max_length=100, verbose_name="نام کامل")
    skill = models.CharField(max_length=100, verbose_name="حرفه")
    active = models.BooleanField(default=True, verbose_name="عضو فعال")

    class Meta:
        verbose_name_plural = "اعضای تیم"

    def __str__(self):
        if self.active:
            return self.full_name + " - " + self.skill + "(فعال)"
        elif not self.active:
            return self.full_name + " - " + self.skill + "(غیرفعال)"

    @property
    def current_profile_picture(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /> </a>'.format(
            url=self.profile_picture.url,
        )
        )


class Service(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان خدمت")
    active = models.BooleanField(default=True, verbose_name="خدمت فعال")

    class Meta:
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="خدمت مربوطه",
                                default=0)
    # default=Service.objects.first().pk)
    title = models.CharField(max_length=30, verbose_name="عنوان نمونه کار")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    date_modified = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین تغییر")
    big_image_or_video = models.FileField(upload_to='portfolios', default='portfolios/default.png', blank=True,
                                          null=True, verbose_name="عکس یا فیلم نمونه بزرگ")
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
    active = models.BooleanField(default=True, verbose_name="نمونه کار فعال")

    class Meta:
        verbose_name_plural = "نمونه کارها"

    def __str__(self):
        if self.active:
            return self.title + "(فعال)"
        elif not self.active:
            return self.title + "(غیرفعال)"

    @property
    def current_big_image_or_video(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=200 height=250 /></a>'.format(
            url=self.big_image_or_video.url,
        )
        )

    @property
    def current_image1(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image1.url,
        )
        )

    @property
    def current_image2(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image2.url,
        )
        )

    @property
    def current_image3(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image3.url,
        )
        )

    @property
    def current_image4(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image4.url,
        )
        )

    @property
    def current_image5(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image5.url,
        )
        )

    @property
    def current_image6(self):
        return mark_safe('<a href="{url}" target="_blank"><img src="{url}" width=150 height=200 /></a>'.format(
            url=self.image6.url,
        )
        )


class PortfolioDescription(models.Model):
    title = models.CharField(max_length=30, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name_plural = "توضیحات در صفحه ی نمونه کارها"

    def __str__(self):
        return self.title + " - " + self.description[0:10] + "..."

    def save(self, *args, **kwargs):
        PortfolioDescription.objects.all().delete()
        super().save()

    @property
    def short_description(self):
        return truncatechars(self.description, 50)


class LandingDescription(models.Model):
    title = models.CharField(max_length=30, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name_plural = "توضیحات در صفحه ی اصلی"

    def __str__(self):
        return self.title + " - " + self.description[0:10] + "..."

    def save(self, *args, **kwargs):
        LandingDescription.objects.all().delete()
        super().save()

    @property
    def short_description(self):
        return truncatechars(self.description, 50)


class AboutUsDescription(models.Model):
    title = models.CharField(max_length=30, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name_plural = "توضیحات در صفحه ی درباره ما"

    def __str__(self):
        return self.title + " - " + self.description[0:10] + "..."

    def save(self, *args, **kwargs):
        AboutUsDescription.objects.all().delete()
        super().save()

    @property
    def short_description(self):
        return truncatechars(self.description, 50)
