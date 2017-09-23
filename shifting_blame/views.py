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

class WaitPage1(WaitPage):
    title_text = "wait for Player A's decision."

class DecisionB(Page):
    def is_displayed(self):
        return self.group.investment_A == "I want to delegate the investment decision to player B." and self.player.id_in_group == 2
    form_model=models.Group
    form_fields=["investment_B"]

class WaitPage2(WaitPage):
    title_text = "wait for Player B to make his decision."
    #def before_next_page(self):
        #self.group.determine_payoffs_investment()

#class WaitPage2(WaitPage):
    #def after_all_players_arrive(self):
       # self.group.determine_payoffs_investment()
   # title_text = "wait for the other players decision."

class Information(Page):
    pass


class Punishment(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 4
    form_model=models.Player
    form_fields=["punishment"]

class PunishmentDecision_C(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 and self.player.punishment == True

    form_model=models.Player
    form_fields=["punishment_A", "punishment_B", "punishment_D"]

class PunishmentDecision_D(Page):
    def is_displayed(self):
        return self.player.id_in_group == 4 and self.player.punishment == True

    form_model=models.Player
    form_fields=["punishment_A", "punishment_B","punishment_C"]

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
    WaitPage1,
    DecisionB,
    WaitPage2,
    Information,
    Punishment,
    PunishmentDecision_C,
    PunishmentDecision_D,
    ResultsWaitPage,
    Results,
    Questions
]
