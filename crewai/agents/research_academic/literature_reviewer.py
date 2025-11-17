"""
Literature Reviewer Agent for CrewAI academic research workflows.
Specializes in systematic literature review and analysis.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ...config import config


class LiteratureReviewerAgent:
    """Agent specialized in literature review and scholarly research."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Literature Reviewer agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Senior Literature Reviewer',
            goal='Conduct systematic literature reviews and synthesize scholarly research findings',
            backstory="""You are an expert in academic literature review with extensive experience in
            systematic review methodologies. You excel at identifying relevant scholarly sources,
            evaluating research quality, and synthesizing complex research findings into coherent
            narratives. Your work forms the foundation for rigorous academic research.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Independent research required
            tools=tools,
        )
