"""
Trend Analyzer Agent for CrewAI Research Swarm.
Specializes in identifying and analyzing ML industry trends.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class TrendAnalyzerAgent:
    """Agent specialized in analyzing ML industry trends and market developments."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Trend Analyzer agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='ML Industry Trend Analyst',
            goal='Identify and analyze emerging trends in machine learning, particularly Random Forest and ensemble methods',
            backstory="""You are a seasoned industry analyst specializing in machine learning trends and market
            intelligence. With a background in data science consulting and technology forecasting, you excel at
            identifying emerging patterns, new applications, and technological shifts in the ML landscape.
            You have a knack for connecting academic research with industry applications and predicting
            which trends will have the most significant impact on Random Forest and ensemble learning.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can collaborate with other research agents
            tools=tools,
        )
