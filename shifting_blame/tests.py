from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):


        yield (views.Instructions)

        yield (views.Role)

        
        yield (views.DecisionA, {"investment_A":"Project 1"})
        assert self.player.payoff == c(150)
            
        if project_success == "successful":
            assert self.player.payoff == c(150)
        else:
            assert self.player.payoff == c(50)


        yield(views.Information)

        
        if self.player.id_in_group == 3 or self.player.id_in_group == 4:
            yield(views.Punishment, {"punishment":True})
            yield SubmissionMustFail(views.PunishmentDecision, {"punishment_A": 80})
            yield (views.PunishmentDecision, {"punishment_A": 20, "punishment_B": 10, "punishment_C": 5})
        if punishment_selection == "D":
            assert p1.payoff == p1.payoff - 20
            assert p2.payoff == p2.payoff -10
            assert p3.payoff == p3.payoff - 5


        yield (views.Results)

        yield (view.Questions)

        yield (views.Finish)

