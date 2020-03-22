from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import Person, Documento, Venda, Produto

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {
            'classes': ('collapse',),
            'fields': ('age', 'salary', 'bio', 'photo')
        })
    )
    # fields = (('first_name', 'doc'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    #exclude = ('bio',)
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    list_filter = ('age', 'salary')
    search_fields = ('id', 'first_name')
    autocomplete_fields = ('doc')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'

    tem_foto.short_description = 'Possui foto'

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    #raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa', 'produtos')
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'total', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]
    #filter_vertical = ['produtos']
    #filter_horizontal = ['produtos']

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ('id', 'descricao')

class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ('num_doc')

admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
