"""
Content Strategist Agent for CrewAI research content workflows.
Specializes in content strategy and planning.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ...config import config


class ContentStrategistAgent:
    """Agent specialized in content strategy and planning."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Content Strategist agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Content Strategy Director',
            goal='Develop compelling content strategies that engage target audiences and achieve communication objectives',
            backstory="""You are a seasoned content strategist with a proven track record of creating
            engaging content across multiple platforms. You understand audience psychology, content
            marketing best practices, and how to structure information for maximum impact. Your
            strategies balance creativity with data-driven insights to deliver content that resonates
            and drives results.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can coordinate with other content team members
            tools=tools,
        )
