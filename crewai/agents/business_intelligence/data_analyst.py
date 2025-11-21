"""
Data Analyst Agent for CrewAI business intelligence workflows.
Specializes in business data analysis and insights.
"""

from crewai import Agent
from ...config import config


class DataAnalystAgent:
    """Agent specialized in business data analysis and KPI development."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Data Analyst agent."""

        return Agent(
            role='Business Intelligence Analyst',
            goal='Transform business data into actionable insights and performance metrics',
            backstory="""You are a business data expert who understands how to extract meaningful
            insights from complex business datasets. You excel at identifying key performance indicators,
            uncovering hidden patterns, and translating data into business intelligence that drives
            operational improvements and strategic decisions.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent analysis required
            tools=[],
        )
