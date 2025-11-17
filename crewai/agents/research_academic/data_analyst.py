"""
Data Analyst Agent for CrewAI academic research workflows.
Specializes in statistical analysis and data interpretation.
"""

from crewai import Agent
from ...config import config


class DataAnalystAgent:
    """Agent specialized in academic data analysis and statistical methods."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Data Analyst agent."""

        return Agent(
            role='Academic Data Analyst',
            goal='Perform rigorous statistical analysis and interpret research data for academic publications',
            backstory="""You are a statistical expert who applies advanced analytical techniques to
            research data. You understand the nuances of different statistical methods and their
            appropriate applications in academic research. Your analyses are methodologically sound
            and contribute to the advancement of knowledge in your field.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent analysis required
            tools=[],
        )
