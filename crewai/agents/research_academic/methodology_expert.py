"""
Methodology Expert Agent for CrewAI academic research workflows.
Specializes in validating research methods and ensuring scientific rigor.
"""

from crewai import Agent
from ...config import config


class MethodologyExpertAgent:
    """Agent specialized in methodology validation and scientific rigor."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Methodology Expert agent."""

        return Agent(
            role='Methodology Validation Expert',
            goal='Ensure research methodologies meet the highest standards of scientific rigor and validity',
            backstory="""You are a methodology expert who evaluates research designs for validity,
            reliability, and appropriateness. You understand the philosophical foundations of different
            research paradigms and can identify methodological flaws or improvements. Your expertise
            ensures that research contributes meaningfully to the scholarly community.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent validation required
            tools=[],
        )
