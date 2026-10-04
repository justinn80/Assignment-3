#!/usr/bin/env python
"""
Tournament Agent: King kong
Student: Doug Dahl
Generated: 2026-10-04 16:12:26

Evolution Details:
- Generations: 100
- Final Fitness: N/A
- Trained against: Always Invest, Random (0.3), Gradual, Generous Tit-for-Tat, Random (0.7)...

Strategy: climb to the top of the empire state building
"""

from agents import Agent, INVEST, UNDERCUT
import random


class DougDahlAgent(Agent):
    """
    King kong

    climb to the top of the empire state building

    Evolved Genes: [0.9291904438144574, 0.9974994406924076, 0.7133959105813934, 0.6005873881319868, 0.8065522815665713, 0.040499051689909776, 0.7425123473423182, 0.9788349521483356, 0.48892297297185144, 0.4833454723872471]
    """

    def __init__(self):
        # These genes were evolved through 100 generations
        self.genes = [0.9291904438144574, 0.9974994406924076, 0.7133959105813934, 0.6005873881319868, 0.8065522815665713, 0.040499051689909776, 0.7425123473423182, 0.9788349521483356, 0.48892297297185144, 0.4833454723872471]

        # Required for tournament compatibility
        self.student_name = "Doug Dahl"

        super().__init__(
            name="King kong",
            description="climb to the top of the empire state building"
        )

    def choose_action(self) -> bool:
        if len(self.history) == 0:          # new game will wipe my own move log
            self.my_moves = []

        opp = [bool(x) for x in self.history]
        n = min(len(opp), len(self.my_moves))
        opp, mine = opp[:n], self.my_moves[:n]

        cooperate = self._decide(self.traits(), opp, mine, n)
        self.my_moves.append(bool(cooperate))
        return INVEST if cooperate else UNDERCUT



# Convenience function for tournament loading
def get_agent():
    """Return an instance of this agent for tournament use"""
    return DougDahlAgent()


if __name__ == "__main__":
    # Test that the agent can be instantiated
    agent = get_agent()
    print(f"✅ Agent loaded successfully: {agent.name}")
    print(f"   Genes: {agent.genes}")
    print(f"   Description: {agent.description}")
