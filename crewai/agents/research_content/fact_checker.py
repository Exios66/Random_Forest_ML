"""
Fact Checker Agent for CrewAI research content workflows.
Specializes in verifying information accuracy and credibility.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ...config import config


class FactCheckerAgent:
    """Agent specialized in fact-checking and information validation."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Fact Checker agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Senior Fact Checker',
            goal='Verify the accuracy, credibility, and timeliness of information to ensure content reliability',
            backstory="""You are a meticulous fact-checker with extensive experience in journalism and
            academic research. You have a keen eye for detail and a commitment to accuracy that borders
            on obsession. You understand how misinformation spreads and have developed sophisticated
            techniques for verifying claims across multiple sources. Your work ensures that all content
            meets the highest standards of factual accuracy.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent verification required
            tools=tools,
        )
