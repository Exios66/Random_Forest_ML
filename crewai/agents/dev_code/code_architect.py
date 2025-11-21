"""
Code Architect Agent for CrewAI development workflows.
Specializes in system design and architecture planning.
"""

from crewai import Agent
from ...config import config


class CodeArchitectAgent:
    """Agent specialized in software architecture and system design."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Code Architect agent."""

        return Agent(
            role='Senior Software Architect',
            goal='Design scalable, maintainable software architectures that meet technical requirements and business objectives',
            backstory="""You are a seasoned software architect with extensive experience in designing
            complex systems across multiple domains. You excel at understanding business requirements
            and translating them into technical solutions that are both elegant and practical. Your
            architectures balance current needs with future scalability, maintainability, and
            technological evolution.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Architects coordinate with development teams
            tools=[],  # Architecture tools would be specialized design tools
        )
