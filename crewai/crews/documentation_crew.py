"""
Documentation & Knowledge Management Crew Orchestration for CrewAI.
Manages documentation creation, knowledge organization, and content management workflows.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..config import config


class DocumentationCrew:
    """Main crew class for documentation and knowledge management workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the documentation crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized documentation and knowledge agents."""
        # Import here to avoid circular imports
        from ..agents.documentation_agents import (
            ContentOrganizerAgent,
            TechnicalWriterAgent,
            KnowledgeManagerAgent,
            DocumentationArchitectAgent,
            QualityAssuranceAgent,
        )

        return {
            "content_organizer": ContentOrganizerAgent.create(),
            "technical_writer": TechnicalWriterAgent.create(),
            "knowledge_manager": KnowledgeManagerAgent.create(),
            "documentation_architect": DocumentationArchitectAgent.create(),
            "quality_assurance": QualityAssuranceAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the documentation workflow tasks."""
        # Import here to avoid circular imports
        from ..tasks.documentation_tasks import get_documentation_workflow_tasks
        return get_documentation_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self, inputs: Optional[Dict[str, Any]] = None) -> Any:
        """Execute the documentation workflow."""
        try:
            print("📖 Starting Documentation & Knowledge Management Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print(f"Tasks: {len(self.tasks)}")
            print("-" * 50)

            # Use provided inputs or default
            crew_inputs = inputs or {
                "project_name": "CrewAI ML Agent Swarm",
                "documentation_type": "technical_documentation",
                "target_audience": "developers",
                "content_scope": "complete_system",
                "format_requirements": "markdown,pdf",
            }

            result = self.crew.kickoff(inputs=crew_inputs)

            print("-" * 50)
            print("📚 Documentation Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during documentation: {str(e)}")
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
        """Get description of the documentation workflow."""
        return """
        Documentation & Knowledge Management Workflow:
        1. Content Organizer: Structures and organizes information architecture
        2. Technical Writer: Creates clear, comprehensive documentation
        3. Knowledge Manager: Manages knowledge bases and information retrieval
        4. Documentation Architect: Designs documentation systems and workflows
        5. Quality Assurance: Reviews and validates documentation quality
        """

    @staticmethod
    def get_supported_doc_types() -> List[str]:
        """Get list of supported documentation types."""
        return [
            "api_documentation",
            "user_guides",
            "technical_documentation",
            "process_documentation",
            "knowledge_base",
            "training_materials",
            "release_notes",
            "architecture_diagrams",
            "code_documentation",
            "compliance_documentation",
            "policy_documentation",
            "research_documentation",
        ]

    @staticmethod
    def get_supported_formats() -> List[str]:
        """Get list of supported output formats."""
        return [
            "markdown",
            "html",
            "pdf",
            "confluence",
            "notion",
            "gitbook",
            "docusaurus",
            "sphinx",
            "readthedocs",
            "mkdocs",
            "latex",
            "word",
            "powerpoint",
        ]
