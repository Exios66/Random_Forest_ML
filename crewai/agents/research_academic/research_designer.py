"""
Research Designer Agent for CrewAI academic research workflows.
Specializes in research methodology and experimental design.
"""

from crewai import Agent
from ...config import config


class ResearchDesignerAgent:
    """Agent specialized in research design and methodology."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Research Designer agent."""

        return Agent(
            role='Research Methodology Expert',
            goal='Design rigorous research methodologies and experimental frameworks for academic studies',
            backstory="""You are a research design specialist with deep knowledge of quantitative and
            qualitative methodologies. You excel at developing research questions, designing experiments,
            and creating frameworks that produce valid, reliable results. Your designs ensure research
            integrity and contribute meaningfully to academic knowledge.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can collaborate on design decisions
            tools=[],
        )
