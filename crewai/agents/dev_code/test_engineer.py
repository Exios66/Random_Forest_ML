"""
Test Engineer Agent for CrewAI development workflows.
Specializes in testing strategy and implementation.
"""

from crewai import Agent
from ...config import config


class TestEngineerAgent:
    """Agent specialized in testing and quality assurance."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Test Engineer agent."""

        return Agent(
            role='Senior Test Engineer',
            goal='Develop comprehensive testing strategies and ensure software reliability through systematic testing',
            backstory="""You are a testing expert who understands that quality is built into software
            through comprehensive testing strategies. You excel at designing test plans, writing
            automated tests, and identifying edge cases that could cause failures. Your work ensures
            that software performs reliably under various conditions.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate testing efforts
            tools=[],  # Testing tools would include test frameworks
        )
