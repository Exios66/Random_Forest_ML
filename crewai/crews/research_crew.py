"""
Research Crew Orchestration for CrewAI.
Manages the complete research analysis workflow for ML advancements.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..agents import (
    LiteratureReviewerAgent,
    TrendAnalyzerAgent,
    InnovationScoutAgent,
    ResearchSummarizerAgent,
)
from ..tasks import get_research_workflow_tasks
from ..config import config


class ResearchCrew:
    """Main crew class for orchestrating research analysis workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the research crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized research agents."""
        return {
            "literature_reviewer": LiteratureReviewerAgent.create(),
            "trend_analyzer": TrendAnalyzerAgent.create(),
            "innovation_scout": InnovationScoutAgent.create(),
            "research_summarizer": ResearchSummarizerAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the research workflow tasks."""
        return get_research_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self) -> Any:
        """Execute the research analysis workflow."""
        try:
            print("🔬 Starting Research Analysis Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print("-" * 50)

            result = self.crew.kickoff()

            print("-" * 50)
            print("🎯 Research Analysis Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during research analysis: {str(e)}")
            raise

    def get_agent(self, name: str) -> Any:
        """Get a specific agent by name."""
        return self.agents.get(name)

    def get_task(self, index: int) -> Any:
        """Get a specific task by index."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    @staticmethod
    def get_status() -> Dict[str, Any]:
        """Get crew status and configuration information."""
        return {
            "crew_type": "Research Swarm",
            "description": "ML research, trends, and innovation analysis",
            "agents_available": 4,
            "tasks_available": 4,
            "specialization": "Academic and industry research analysis",
        }
