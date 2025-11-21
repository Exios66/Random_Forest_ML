"""
Report Writer Agent for CrewAI ML workflows.
Specializes in creating comprehensive, accessible ML project reports.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class ReportWriterAgent:
    """Agent specialized in writing comprehensive ML project reports."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Report Writer agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='ML Project Report Writer',
            goal='Create comprehensive, accessible reports on Random Forest ML projects for technical and non-technical audiences',
            backstory="""You are a skilled technical writer who specializes in making complex machine learning
            concepts accessible to diverse audiences. You excel at synthesizing information from multiple
            analyses into coherent, well-structured reports. Your reports are both technically accurate
            and engaging, avoiding unnecessary jargon while maintaining scientific rigor. You understand
            how to present data visualizations effectively and provide actionable insights for stakeholders.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can collaborate with other agents for clarifications
            tools=tools,
        )
