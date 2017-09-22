from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class Role(Page):
    pass

class DecisionA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model=models.Group
    form_fields=["investment_A"]

class DecisionB(Page):
    def is_displayed(self):
        return self.group.investment_A == "I want to delegate the investment decision to player B." and self.player.id_in_group == 2
    form_model=models.Group
    form_fields=["investment_B"]

class Information(Page):
   pass
   # def after_all_players_arrive(self):
     #   return self.Group.

class Punishment(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 4
    form_model=models.Player
    form_fields=["punishment"]

class PunishmentDecision(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 4 and self.player.punishment == True

    form_model=models.Player
    form_fields=["punishment_A", "punishment_B","punishment_C", "punishment_D"]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass

class Questions(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","no_student","willingness_risk","nationality"]


page_sequence = [
    Instructions,
    Role,
    DecisionA,
    DecisionB,
    Information,
    Punishment,
    PunishmentDecision,
    ResultsWaitPage,
    Results,
    Questions
]
