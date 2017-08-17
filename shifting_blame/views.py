from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class DecisionA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model=models.Group
    form_fields=["investment_A"]

class DecisionB(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2
    form_model=models.Group
    form_fields=["investment_B"]

class Information(Page):
    form_model=models.Group
    form_fields=["punishment"]

class ResultsWaitPage(WaitPage):
	pass
    #def after_all_players_arrive(self):
        #pass


class Results(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","willingness_risk","nationality"]


page_sequence = [
    Instructions,
    DecisionA,
    DecisionB,
    Information,
    Results
]
