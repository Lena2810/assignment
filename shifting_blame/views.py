from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WaitPage0(WaitPage):
    group_by_arrival_time = True

    title_text = "Please wait to be grouped."


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

    def is_displayed(self):
        return self.group.investment_A == "I want to delegate the investment decision to player B."



    #def before_next_page(self):
       # self.group.determine_payoffs_investment()

#class WaitPage2(WaitPage):
    #def after_all_players_arrive(self):
       # self.group.determine_payoffs_investment()
   # title_text = "wait for the other players decision."

class DeterminePayoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_project_success()
        self.group.determine_payoffs_investment()


class Information(Page):
    pass



class Punishment(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 4
    form_model=models.Group
    form_fields=["punishment"]


class PunishmentDecision(Page):
    def is_displayed(self):
        return self.group.punishment == True

    form_model=models.Player

    def get_form_fields(self):
        if self.player.id_in_group == 3:
            return ["punishment_A", "punishment_B", "punishment_D"]

        if self.player.id_in_group == 4:
            return ["punishment_A", "punishment_B", "punishment_C"]


    def error_message(self, values):
        if self.player.id_in_group == 3:
            if int(values["punishment_A"]) + int(values["punishment_B"]) + int(values["punishment_D"]) > 70:
                return 'The sum must be below or equal 70.'

        if self.player.id_in_group == 4:
            if int(values["punishment_A"]) + int(values["punishment_B"]) + int(values["punishment_C"]) > 70:
                return 'The sum must be below or equal 70.'

    
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.determine_punishment_selection()
        self.group.determine_final_payoffs()


class Results(Page):
    pass

class Questions(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","no_student","willingness_risk","nationality"]


page_sequence = [
    WaitPage0,
    Instructions,
    Role,
    DecisionA,
    WaitPage1,
    DecisionB,
    WaitPage2,
    DeterminePayoffs,
    Information,
    Punishment,
    PunishmentDecision,
    ResultsWaitPage,
    Results,
    Questions
]
