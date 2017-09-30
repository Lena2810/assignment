from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class WaitPage0(WaitPage):
    group_by_arrival_time = True

    title_text = "Please wait to be grouped."


class Instructions(Page):
    def before_next_page(self):
        self.group.set_treatment()
    
    timeout_seconds = 180

class Role(Page):
    pass
    
    timeout_seconds = 60

class DecisionA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1
    form_model=models.Group
    form_fields=["investment_A"]

    timeout_seconds = 120
    timeout_submission = {"investment_A": "I want to delegate the investment decision to player B."}

class WaitPage1(WaitPage):
    def is_displayed(self):
        return self.player.id_in_group != 1

    title_text = "Wait for player A's decision."


class DecisionB(Page):
    def is_displayed(self):
        return self.group.investment_A == "I want to delegate the investment decision to player B." and self.player.id_in_group == 2
    
    form_model=models.Group
    form_fields=["investment_B"]

    timeout_seconds = 120
    timeout_submission = {"investment_B": "Project 1"}


class WaitPage2(WaitPage):

    title_text = "Wait for player B to make his decision."

    def is_displayed(self):
        return self.player.id_in_group != 2 and self.group.investment_A == "I want to delegate the investment decision to player B."


class DeterminePayoffs(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_project_success()
        self.group.determine_payoffs_investment()


class Information(Page):
    pass
    timeout_seconds = 120


class Punishment(Page):
    def is_displayed(self):
        return self.player.id_in_group == 3 or self.player.id_in_group == 4
    form_model=models.Player
    form_fields=["punishment"]

    timeout_seconds = 120


class PunishmentDecision(Page):
    def is_displayed(self):
        return self.player.punishment == True

    form_model=models.Player

    def get_form_fields(self):
        if self.player.id_in_group == 3:
            return ["punishment_A", "punishment_B", "punishment_D"]

        if self.player.id_in_group == 4:
            return ["punishment_A", "punishment_B", "punishment_C"]


    def punishment_error_message(self, values):
        if self.player.id_in_group == 3:
            if int(values["punishment_A"]) + int(values["punishment_B"]) + int(values["punishment_D"]) > 70:
                return 'The sum must be below or equal 70.'

        if self.player.id_in_group == 4:
            if int(values["punishment_A"]) + int(values["punishment_B"]) + int(values["punishment_C"]) > 70:
                return 'The sum must be below or equal 70.'

    timeout_seconds = 180   

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.determine_punishment_selection()
        self.group.determine_final_payoffs()




class Results(Page):
    pass

    timeout_seconds = 120

class Questions(Page):
    form_model=models.Player
    form_fields=["age","gender","field_of_studies","no_student","willingness_risk","nationality"]

    def error_message(self, values):
        if values["field_of_studies"] == '' and values["no_student"] == False:
            return "Please fill in either a field of study or check the box."
        if values["field_of_studies"] != '' and values["no_student"] == True:
            return "Please fill in a field of study or check the box."


    timeout_seconds = 180

class Finish(Page):
    pass

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
    Questions,
    Finish
]
