"""
Content Organizer Agent for CrewAI documentation workflows.
Specializes in information architecture and content structuring.
"""

from crewai import Agent
from ...config import config


class ContentOrganizerAgent:
    """Agent specialized in content organization and information architecture."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Content Organizer agent."""

        return Agent(
            role='Information Architect',
            goal='Design and organize content structures that maximize findability and usability',
            backstory="""You are an information architecture expert who understands how to structure
            complex information for optimal user experience. You excel at creating logical hierarchies,
            developing navigation systems, and organizing content in ways that make it easy for users
            to find and understand the information they need.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate content organization
            tools=[],
        )
