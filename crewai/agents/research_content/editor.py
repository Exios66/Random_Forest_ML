"""
Editor Agent for CrewAI research content workflows.
Specializes in content editing and refinement.
"""

from crewai import Agent
from ...config import config


class EditorAgent:
    """Agent specialized in content editing and refinement."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Editor agent."""

        return Agent(
            role='Senior Content Editor',
            goal='Refine and polish content to ensure clarity, engagement, and professional quality',
            backstory="""You are an accomplished editor with years of experience refining content across
            various mediums. You excel at improving clarity without losing voice, strengthening arguments
            without changing meaning, and ensuring content flows naturally for the intended audience.
            Your edits enhance readability while maintaining the author's original intent and expertise.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can work with writers and strategists
            tools=[],  # Editors typically don't need external tools
        )
