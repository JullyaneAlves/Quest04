from django.contrib import admin

from .models import *

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"
pt_BR_formats.DATE_FORMAT = "d M Y"


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('dataemp', 'datadev', 'amigo', 'revista')
    date_hierarchy = ('dataemp')
    search_fieldes = ('amigo',)
    list_filter = ['amigo',]

class AmigoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fone')

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('colecao', 'ano', 'numero')


admin.site.register(Caixa)
admin.site.register(Colecao)
admin.site.register(GrupoAmigo)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Revista, RevistaAdmin)
