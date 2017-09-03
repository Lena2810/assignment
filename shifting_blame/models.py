from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Lena'

doc = """
Shifting blame
"""


class Constants(BaseConstants):
    name_in_url = 'shifting_blame'
    players_per_group = 4
    num_rounds = 1
    endowment = c(100)
    treatment_risk = 0.3
    treatment_baseline = 0


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        for group in self.get_groups():
            if 'treatment' in self.session.config:
                group.risk = self.session.config['treatment']       #demo
            else:
                group.risk = random.choice(['baseline', 'risk'])    #live experiment



class Group(BaseGroup):

    risk=models.CharField(
        #choices=["baseline","risk"],
        #doc="treatment of investment"
        )
        # randomize to treatments

    investment_A=models.CharField(
        choices=["Investment 1", "Investment 2", "I want to delegate the investment decision to player B."],
        widget=widgets.RadioSelect(),
        verbose_name="Which investment do you want to choose?",
        doc="Decision player A investment, Charfield input"
        )
    investment_B=models.CharField(
        choices=["Investment 1", "Investment 2"],
        widget=widgets.RadioSelect(),
        verbose_name="Which investment do you want to choose?",
        doc="Decision player B investment, Charfield input"
        )

    #payoffs

    def set_payoffs(self):
        p1 = self.get_player_by_role("A")
        p2 = self.get_player_by_role("B")
        p3 = self.get_player_by_role("C")
        p4 = self.get_player_by_role("D")
    #if self.investment_A== "Investment 1":
       # if self.punishment:
       # p1.payoff=Constants.endowment - self.offer
       # p2.payoff=self.offer
    #else:
       # p1.payoff=0
        #p2.payoff=0

class Player(BasePlayer):

    def role(self):
        if self.id_in_group == 1:
            return "A"
        if self.id_in_group == 2:
            return "B"
        if self.id_in_group == 3:
            return "C"
        else:
            return "D"

#punishment
    punishment=models.BooleanField(
        choices=[(True, "Yes"), (False, "No")],
        widget=widgets.RadioSelect(),
        verbose_name="Do you want to pay 10 of your points to get 70 punishment points?",
        doc="Boolean Field for decision C and D whether to buy punishment points."
        )

    punishment_A=models.PositiveIntegerField(
        choices = range(0, 70),
        widget=widgets.SliderInput(),
        verbose_name="How much do you want to punish A?",
        doc= "Punishment A")
    punishment_B=models.PositiveIntegerField(
        min= 0,
        max= 70,
        widget=widgets.SliderInput(),
        verbose_name="How much do you want to punish B?",
        doc= "Punishment B")
    punishment_C=models.PositiveIntegerField(
        min=0,
        max= 70,
        widget=widgets.SliderInput(),
        verbose_name="How much do you want to punish C?",
        doc= "Punishment C")
    punishment_D=models.PositiveIntegerField(
        choices = range(0, 70),
        widget=widgets.SliderInput(),
        verbose_name="How much do you want to punish D?",
        doc= "Punishment D")

    #demographics
    age = models.PositiveIntegerField(
        max=120,
        blank=True,
        verbose_name="How old are you?",
        doc="collect age data between 0 and 120"
        )
    gender = models.CharField(
        choices=["Female", "Male"],
        widget=widgets.RadioSelect(),
        blank=True,
        verbose_name="What is your gender?",
        doc="Ask for the gender"
        )
    field_of_studies = models.CharField(
        blank=True,
        verbose_name="What do you study if at all?",
        doc="free text input of field of studies"       
        )
    no_student = models.BooleanField(
        verbose_name="I'm not a student",
        widget=widgets.CheckboxInput(),
        doc="Boolean Field, if player is no student: 1")
    willingness_risk= models.CharField(
        choices=["Strongly disagree", "Disagree", "Moderately Disagree", "Undecided", "Moderately Agree", "Agree", "Strongly Agree"],
        blank=True,
        widget=widgets.RadioSelectHorizontal(),
        verbose_name="My willigness to take risk is high:",
        doc="willigness to take risk input CharField"
        )
    nationality=models.CharField(
        choices=["German", "Italian","French","Spanish","American","Swedish","Great Britain", "Chinese", "Japan","other"],
        blank=True,
        verbose_name="What is your nationality?",
        doc= "input nationality dropdown"
        )