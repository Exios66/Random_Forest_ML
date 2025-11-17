"""
Data Analyst Agent for CrewAI ML workflows.
Specializes in data exploration, quality assessment, and preprocessing recommendations.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class DataAnalystAgent:
    """Agent specialized in data analysis and preprocessing for ML projects."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Data Analyst agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Senior Data Analyst',
            goal='Analyze datasets, identify data quality issues, and provide preprocessing recommendations for Random Forest models',
            backstory="""You are an experienced data analyst specializing in machine learning datasets.
            You excel at understanding data distributions, identifying missing values, detecting outliers,
            and recommending appropriate preprocessing steps. You have extensive experience with
            Random Forest algorithms and understand what data characteristics affect their performance.
            You work methodically, providing detailed analysis with actionable insights.""",
            verbose=config.VERBOSE,
            allow_delegation=False,  # Focus on analysis, not delegation
            tools=tools,
        )
