"""
Innovation Scout Agent for CrewAI Research Swarm.
Specializes in discovering novel applications and breakthrough technologies.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class InnovationScoutAgent:
    """Agent specialized in discovering innovative applications and breakthrough technologies."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Innovation Scout agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Innovation Scout',
            goal='Discover novel applications and breakthrough technologies related to Random Forest and ensemble methods',
            backstory="""You are an innovation specialist and technology scout with a passion for discovering
            breakthrough applications of machine learning. You have a background in R&D and technology transfer,
            with expertise in identifying unconventional uses of Random Forest algorithms across different
            industries. You excel at connecting seemingly unrelated fields and finding creative applications
            that push the boundaries of what's possible with ensemble learning methods.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Highly collaborative for innovation
            tools=tools,
        )
