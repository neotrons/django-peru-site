from string import punctuation
from django.db import models
from mezzanine.galleries.models import Gallery
from mezzanine.core.models import Orderable
from django.utils.encoding import python_2_unicode_compatible
from mezzanine.core.fields import FileField
from mezzanine.utils.models import upload_to
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class SlideImage(Orderable):
    title = models.CharField(_("Title"), max_length=100, blank=True, help_text=_("Title of slide"))
    file = FileField(_("File"), max_length=200, format="Image",
                     upload_to=upload_to("jedi.SlidesImage.file", "slidesimage"))
    description = models.CharField(_("Description"), max_length=1000, blank=True)
    link = models.URLField(_("Link"), max_length=200, blank=True, null=True, default=None,
                           help_text=_("Slug of Learn More"))
    video = models.URLField(_("video"), max_length=200, blank=True, null=True, default=None,
                            help_text=_("Youtube or Vimeo link"))
    active = models.BooleanField(_("Active"), default=True, help_text=_("Slide is active"))

    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = force_text(self.file)
            name = name.rsplit("/", 1)[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(SlideImage, self).save(*args, **kwargs)

