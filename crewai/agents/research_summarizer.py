"""
Research Summarizer Agent for CrewAI Research Swarm.
Specializes in synthesizing and summarizing research findings.
"""

from crewai import Agent
from crewai_tools import SerperDevTool
from ..config import config


class ResearchSummarizerAgent:
    """Agent specialized in synthesizing and summarizing research findings."""

    @staticmethod
    def create() -> Agent:
        """Create and return the Research Summarizer agent."""

        # Initialize tools
        search_tool = SerperDevTool() if config.SERPER_API_KEY else None

        tools = []
        if search_tool:
            tools.append(search_tool)

        return Agent(
            role='Research Synthesis Specialist',
            goal='Synthesize complex research findings into clear, actionable insights for Random Forest development',
            backstory="""You are a master synthesizer of complex information with a talent for distilling
            intricate research findings into clear, actionable insights. With a background in science
            communication and technical writing, you excel at bridging the gap between academic research
            and practical application. You have a particular gift for explaining complex ensemble learning
            concepts in ways that both experts and practitioners can understand and apply.""",
            verbose=config.VERBOSE,
            allow_delegation=True,  # Works well with other research agents
            tools=tools,
        )
