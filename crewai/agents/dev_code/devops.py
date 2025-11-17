"""
DevOps Agent for CrewAI development workflows.
Specializes in deployment, infrastructure, and CI/CD.
"""

from crewai import Agent
from ...config import config


class DevOpsAgent:
    """Agent specialized in DevOps, deployment, and infrastructure management."""

    @staticmethod
    def create() -> Agent:
        """Create and return the DevOps agent."""

        return Agent(
            role='Senior DevOps Engineer',
            goal='Implement reliable deployment pipelines, infrastructure automation, and operational excellence',
            backstory="""You are a DevOps expert who bridges the gap between development and operations.
            You understand how to automate deployment processes, manage infrastructure as code, and
            ensure that applications run reliably in production. Your expertise ensures smooth,
            efficient, and secure software delivery.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Coordinates deployment and operations
            tools=[],  # DevOps tools would include infrastructure automation
        )
