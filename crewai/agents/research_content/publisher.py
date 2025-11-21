"""
Publisher Agent for CrewAI research content workflows.
Specializes in content publishing and distribution.
"""

from crewai import Agent
from ...config import config


class PublisherAgent:
    """Agent specialized in content publishing and distribution."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Publisher agent."""

        return Agent(
            role='Digital Publishing Manager',
            goal='Optimize and distribute content across appropriate channels to maximize reach and engagement',
            backstory="""You are a publishing expert who understands the nuances of different platforms
            and audiences. You know how to optimize content for search engines, social media algorithms,
            and various publishing formats. Your expertise ensures that high-quality content reaches
            its intended audience effectively and achieves maximum impact.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate publication logistics
            tools=[],  # Publishing tools would be integrated based on platform
        )
