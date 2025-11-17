"""
Academic Research Crew Orchestration for CrewAI.
Manages academic research, literature review, and scholarly workflows.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..config import config


class ResearchAcademicCrew:
    """Main crew class for academic research workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the academic research crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized academic research agents."""
        # Import here to avoid circular imports
        from ..agents.research_academic_agents import (
            LiteratureReviewerAgent,
            ResearchDesignerAgent,
            DataAnalystAgent,
            MethodologyExpertAgent,
            AcademicWriterAgent,
        )

        return {
            "literature_reviewer": LiteratureReviewerAgent.create(),
            "research_designer": ResearchDesignerAgent.create(),
            "data_analyst": DataAnalystAgent.create(),
            "methodology_expert": MethodologyExpertAgent.create(),
            "academic_writer": AcademicWriterAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the academic research workflow tasks."""
        # Import here to avoid circular imports
        from ..tasks.research_academic_tasks import get_research_academic_workflow_tasks
        return get_research_academic_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self, inputs: Optional[Dict[str, Any]] = None) -> Any:
        """Execute the academic research workflow."""
        try:
            print("📚 Starting Academic Research Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print(f"Tasks: {len(self.tasks)}")
            print("-" * 50)

            # Use provided inputs or default
            crew_inputs = inputs or {
                "research_topic": "Machine Learning in Healthcare",
                "research_question": "How can ML improve diagnostic accuracy?",
                "methodology": "systematic_review",
                "target_journal": "Nature Medicine",
                "word_count": "8000",
            }

            result = self.crew.kickoff(inputs=crew_inputs)

            print("-" * 50)
            print("🎓 Academic Research Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during academic research: {str(e)}")
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
        """Get description of the academic research workflow."""
        return """
        Academic Research Workflow:
        1. Literature Reviewer: Conducts systematic literature review and analysis
        2. Research Designer: Develops research methodology and experimental design
        3. Data Analyst: Performs statistical analysis and data interpretation
        4. Methodology Expert: Validates research methods and ensures rigor
        5. Academic Writer: Produces scholarly manuscripts and publications
        """

    @staticmethod
    def get_supported_methodologies() -> List[str]:
        """Get list of supported research methodologies."""
        return [
            "systematic_review",
            "meta_analysis",
            "experimental_study",
            "quasi_experimental",
            "case_study",
            "survey_research",
            "qualitative_analysis",
            "mixed_methods",
            "longitudinal_study",
            "cross_sectional_study",
            "grounded_theory",
            "ethnographic_research",
        ]

    @staticmethod
    def get_supported_fields() -> List[str]:
        """Get list of supported academic fields."""
        return [
            "computer_science",
            "medicine",
            "biology",
            "physics",
            "chemistry",
            "mathematics",
            "statistics",
            "economics",
            "psychology",
            "sociology",
            "education",
            "engineering",
            "environmental_science",
            "political_science",
            "history",
            "philosophy",
        ]
