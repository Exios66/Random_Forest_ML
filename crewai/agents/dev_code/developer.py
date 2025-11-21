"""
Developer Agent for CrewAI development workflows.
Specializes in code implementation and development.
"""

from crewai import Agent
from ...config import config


class DeveloperAgent:
    """Agent specialized in code implementation and development."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Developer agent."""

        return Agent(
            role='Senior Software Developer',
            goal='Write clean, efficient, and maintainable code that implements architectural specifications',
            backstory="""You are an experienced developer who writes code that is not just functional
            but also readable, maintainable, and efficient. You understand software development best
            practices, design patterns, and testing principles. Your code serves as a foundation for
            robust, scalable applications.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Focus on individual coding tasks
            tools=[],  # Development tools would include IDE integrations
        )
