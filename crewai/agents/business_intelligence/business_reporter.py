"""
Business Reporter Agent for CrewAI business intelligence workflows.
Specializes in business reporting and executive communications.
"""

from crewai import Agent
from ...config import config


class BusinessReporterAgent:
    """Agent specialized in business reporting and executive communications."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Business Reporter agent."""

        return Agent(
            role='Business Intelligence Reporter',
            goal='Create clear, actionable business reports and executive summaries for stakeholders',
            backstory="""You are a business communications expert who knows how to present complex
            business information in clear, compelling formats. You excel at creating executive summaries,
            dashboards, and reports that make data-driven insights accessible to decision-makers at
            all levels of the organization.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate reporting efforts
            tools=[],
        )
