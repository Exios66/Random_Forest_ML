"""
Code Reviewer Agent for CrewAI development workflows.
Specializes in code quality assessment and review.
"""

from crewai import Agent
from ...config import config


class CodeReviewerAgent:
    """Agent specialized in code review and quality assessment."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Code Reviewer agent."""

        return Agent(
            role='Senior Code Reviewer',
            goal='Ensure code quality, identify bugs, and enforce coding standards and best practices',
            backstory="""You are a meticulous code reviewer with a keen eye for detail and a deep
            understanding of software quality principles. You excel at identifying potential bugs,
            security vulnerabilities, performance issues, and maintainability concerns. Your reviews
            help teams deliver high-quality, reliable software.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent review process
            tools=[],  # Code review tools would include static analysis
        )
