"""
Feature Engineer Agent for CrewAI ML workflows.
Specializes in feature analysis, engineering, and importance assessment.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class FeatureEngineerAgent:
    """Agent specialized in feature engineering and importance analysis."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Feature Engineer agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Feature Engineering Specialist',
            goal='Analyze feature importance, identify engineering opportunities, and optimize feature sets for Random Forest models',
            backstory="""You are a feature engineering expert with extensive experience in optimizing datasets
            for Random Forest and other ensemble methods. You excel at interpreting feature importance rankings,
            identifying redundant features, discovering interaction effects, and creating new features that
            improve model performance. You understand how Random Forest handles different types of features
            and can provide targeted recommendations for feature engineering and selection.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can collaborate with data analyst
            tools=tools,
        )
