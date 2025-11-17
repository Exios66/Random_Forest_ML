"""
Model Evaluator Agent for CrewAI ML workflows.
Specializes in model performance assessment and comparison.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class ModelEvaluatorAgent:
    """Agent specialized in evaluating and comparing ML model performance."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Model Evaluator agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='ML Model Evaluator',
            goal='Evaluate Random Forest model performance, compare with baselines, and provide detailed performance analysis',
            backstory="""You are a seasoned machine learning engineer with deep expertise in model evaluation
            and performance analysis. You specialize in Random Forest algorithms and understand their strengths
            and limitations across different types of datasets. You excel at interpreting confusion matrices,
            ROC curves, feature importance rankings, and other evaluation metrics. You provide comprehensive
            performance reports with clear recommendations for model improvement.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Can delegate to other agents for specific analyses
            tools=tools,
        )
