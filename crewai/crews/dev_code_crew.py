"""
Development & Code Review Crew Orchestration for CrewAI.
Manages code development, review, and optimization workflows.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..config import config


class DevCodeCrew:
    """Main crew class for development and code review workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the development code crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized development and code agents."""
        # Import here to avoid circular imports
        from ..agents.dev_code_agents import (
            CodeArchitectAgent,
            DeveloperAgent,
            CodeReviewerAgent,
            TestEngineerAgent,
            DevOpsAgent,
        )

        return {
            "code_architect": CodeArchitectAgent.create(),
            "developer": DeveloperAgent.create(),
            "code_reviewer": CodeReviewerAgent.create(),
            "test_engineer": TestEngineerAgent.create(),
            "devops": DevOpsAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the development code workflow tasks."""
        # Import here to avoid circular imports
        from ..tasks.dev_code_tasks import get_dev_code_workflow_tasks
        return get_dev_code_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self, inputs: Optional[Dict[str, Any]] = None) -> Any:
        """Execute the development code workflow."""
        try:
            print("💻 Starting Development & Code Review Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print(f"Tasks: {len(self.tasks)}")
            print("-" * 50)

            # Use provided inputs or default
            crew_inputs = inputs or {
                "project_type": "web_application",
                "tech_stack": "python,fastapi,react",
                "requirements": "Build a REST API for data processing",
                "code_quality": "high",
                "testing_level": "comprehensive",
            }

            result = self.crew.kickoff(inputs=crew_inputs)

            print("-" * 50)
            print("🎉 Development & Code Review Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during development: {str(e)}")
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
        """Get description of the development code workflow."""
        return """
        Development & Code Review Workflow:
        1. Code Architect: Designs system architecture and technical specifications
        2. Developer: Implements code according to specifications
        3. Code Reviewer: Performs code quality assessment and suggests improvements
        4. Test Engineer: Develops and validates test suites
        5. DevOps Engineer: Manages deployment, CI/CD, and infrastructure
        """

    @staticmethod
    def get_supported_languages() -> List[str]:
        """Get list of supported programming languages."""
        return [
            "python",
            "javascript",
            "typescript",
            "java",
            "cpp",
            "go",
            "rust",
            "php",
            "ruby",
            "swift",
            "kotlin",
            "scala",
        ]

    @staticmethod
    def get_supported_frameworks() -> List[str]:
        """Get list of supported frameworks and technologies."""
        return [
            "fastapi",
            "django",
            "flask",
            "react",
            "vue",
            "angular",
            "spring",
            "express",
            "laravel",
            "rails",
            "docker",
            "kubernetes",
            "aws",
            "azure",
            "gcp",
        ]
