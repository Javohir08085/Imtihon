from modeltranslation.translator import translator,TranslationOptions
from app_politicians.models import PoliticiansModel

class PoliticiansTranslationOptions(TranslationOptions):
    fields = ('name', 'position')
    required_languages = ('uz','position')


translator.register(PoliticiansModel, PoliticiansTranslationOptions)