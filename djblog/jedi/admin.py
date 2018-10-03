from django.contrib import admin
from jedi.models import SlideImage
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.utils.static import static_lazy as static


class SlideAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": (static("mezzanine/css/admin/gallery.css"),)}


admin.site.register(SlideImage, SlideAdmin)

