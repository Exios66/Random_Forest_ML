"""
Research & Content Creation Crew Orchestration for CrewAI.
Manages research, analysis, and content creation workflows.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..config import config


class ResearchContentCrew:
    """Main crew class for research and content creation workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the research content crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized research and content agents."""
        # Import here to avoid circular imports
        from ..agents.research_content_agents import (
            ResearchAnalystAgent,
            ContentStrategistAgent,
            FactCheckerAgent,
            EditorAgent,
            PublisherAgent,
        )

        return {
            "research_analyst": ResearchAnalystAgent.create(),
            "content_strategist": ContentStrategistAgent.create(),
            "fact_checker": FactCheckerAgent.create(),
            "editor": EditorAgent.create(),
            "publisher": PublisherAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the research content workflow tasks."""
        # Import here to avoid circular imports
        from ..tasks.research_content_tasks import get_research_content_workflow_tasks
        return get_research_content_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self, inputs: Optional[Dict[str, Any]] = None) -> Any:
        """Execute the research content workflow."""
        try:
            print("🔬 Starting Research & Content Creation Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print(f"Tasks: {len(self.tasks)}")
            print("-" * 50)

            # Use provided inputs or default
            crew_inputs = inputs or {
                "topic": "Artificial Intelligence Trends 2024",
                "content_type": "blog_post",
                "target_audience": "tech_professionals",
                "word_count": "2000",
            }

            result = self.crew.kickoff(inputs=crew_inputs)

            print("-" * 50)
            print("🎉 Research & Content Creation Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during content creation: {str(e)}")
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
    def get_workflow_description() -> str:
        """Get description of the research content workflow."""
        return """
        Research & Content Creation Workflow:
        1. Research Analyst: Conducts comprehensive research and analysis
        2. Content Strategist: Develops content strategy and outlines
        3. Fact Checker: Validates information accuracy and sources
        4. Editor: Refines content for clarity and engagement
        5. Publisher: Prepares content for publication and distribution
        """

    @staticmethod
    def get_supported_content_types() -> List[str]:
        """Get list of supported content types."""
        return [
            "blog_post",
            "research_report",
            "white_paper",
            "news_article",
            "tutorial",
            "case_study",
            "newsletter",
            "social_media",
            "video_script",
            "presentation",
        ]
