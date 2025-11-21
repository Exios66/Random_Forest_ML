"""
Research Analyst Agent for CrewAI research content workflows.
Specializes in comprehensive research and analysis.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ...config import config


class ResearchAnalystAgent:
    """Agent specialized in research and analysis for content creation."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Research Analyst agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Senior Research Analyst',
            goal='Conduct comprehensive research and analysis to gather accurate, relevant information for content creation',
            backstory="""You are an experienced research analyst with expertise in gathering and synthesizing
            information from diverse sources. You excel at identifying credible sources, analyzing trends,
            and providing well-substantiated insights. Your research is thorough, objective, and tailored
            to support high-quality content creation across various domains.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Focus on research expertise
            tools=tools,
        )
