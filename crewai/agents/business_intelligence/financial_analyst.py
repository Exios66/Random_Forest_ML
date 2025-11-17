"""
Financial Analyst Agent for CrewAI business intelligence workflows.
Specializes in financial modeling and valuation.
"""

from crewai import Agent
from ...config import config


class FinancialAnalystAgent:
    """Agent specialized in financial analysis and business valuation."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Financial Analyst agent."""

        return Agent(
            role='Senior Financial Analyst',
            goal='Perform financial modeling, valuation, and investment analysis for business decisions',
            backstory="""You are a financial expert who understands how to model business performance,
            assess investment opportunities, and evaluate financial risks. You excel at creating
            financial projections, performing valuations, and providing insights that inform
            investment and strategic financial decisions.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent financial analysis required
            tools=[],
        )
