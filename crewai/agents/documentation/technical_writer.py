"""
Technical Writer Agent for CrewAI documentation workflows.
Specializes in creating clear technical documentation.
"""

from crewai import Agent
from ...config import config


class TechnicalWriterAgent:
    """Agent specialized in technical writing and documentation."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Technical Writer agent."""

        return Agent(
            role='Senior Technical Writer',
            goal='Create clear, accurate, and comprehensive technical documentation for various audiences',
            backstory="""You are a technical writing expert who knows how to translate complex technical
            concepts into clear, accessible documentation. You understand different audience needs and
            can adjust your writing style accordingly, from developer documentation to end-user guides.
            Your documentation helps users understand and effectively use technical systems.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can collaborate on documentation projects
            tools=[],
        )
