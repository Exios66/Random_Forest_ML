"""
Knowledge Manager Agent for CrewAI documentation workflows.
Specializes in knowledge base management and information retrieval.
"""

from crewai import Agent
from ...config import config


class KnowledgeManagerAgent:
    """Agent specialized in knowledge management and information organization."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Knowledge Manager agent."""

        return Agent(
            role='Knowledge Base Manager',
            goal='Organize, maintain, and optimize knowledge bases for efficient information retrieval',
            backstory="""You are a knowledge management expert who understands how to capture, organize,
            and make information accessible. You excel at creating taxonomies, implementing search systems,
            and ensuring that knowledge remains current and valuable. Your work ensures that organizational
            knowledge is preserved and easily accessible to those who need it.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate knowledge management initiatives
            tools=[],
        )
