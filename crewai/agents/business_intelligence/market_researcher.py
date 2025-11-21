"""
Market Researcher Agent for CrewAI business intelligence workflows.
Specializes in market analysis and competitive intelligence.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ...config import config


class MarketResearcherAgent:
    """Agent specialized in market research and competitive analysis."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Market Researcher agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Senior Market Research Analyst',
            goal='Conduct comprehensive market analysis and competitive intelligence for strategic decision-making',
            backstory="""You are an experienced market researcher who understands how to gather and
            analyze market data to uncover trends, opportunities, and competitive threats. You excel
            at combining quantitative data with qualitative insights to provide actionable intelligence
            that drives business strategy and growth.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent research required
            tools=tools,
        )
