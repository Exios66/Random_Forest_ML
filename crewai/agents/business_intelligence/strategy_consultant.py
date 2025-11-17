"""
Strategy Consultant Agent for CrewAI business intelligence workflows.
Specializes in strategic planning and recommendations.
"""

from crewai import Agent
from ...config import config


class StrategyConsultantAgent:
    """Agent specialized in business strategy development and consulting."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Strategy Consultant agent."""

        return Agent(
            role='Senior Strategy Consultant',
            goal='Develop strategic recommendations based on business intelligence and market insights',
            backstory="""You are a strategic consultant who synthesizes complex business information
            into clear strategic recommendations. You understand how to align business objectives with
            market opportunities, competitive dynamics, and internal capabilities to create actionable
            strategies that drive sustainable growth.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate strategic initiatives
            tools=[],
        )
