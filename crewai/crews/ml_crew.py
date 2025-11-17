"""
ML Crew Orchestration for CrewAI.
Manages the complete Random Forest ML analysis workflow.
"""

from crewai import Crew, Process
from typing import Dict, Any, Optional, List
from ..agents import (
    DataAnalystAgent,
    ModelEvaluatorAgent,
    FeatureEngineerAgent,
    HyperparameterOptimizerAgent,
    ReportWriterAgent,
)
from ..tasks import get_ml_workflow_tasks
from ..config import config


class MLCrew:
    """Main crew class for orchestrating ML analysis workflows."""

    def __init__(self, process: str = "sequential"):
        """Initialize the ML crew with agents and tasks.

        Args:
            process: Process type ("sequential" or "hierarchical")
        """
        self.process = Process.sequential if process == "sequential" else Process.hierarchical
        self.agents = self._create_agents()
        self.tasks = self._create_tasks()
        self.crew = self._create_crew()

    def _create_agents(self) -> Dict[str, Any]:
        """Create all specialized ML agents."""
        return {
            "data_analyst": DataAnalystAgent.create(),
            "model_evaluator": ModelEvaluatorAgent.create(),
            "feature_engineer": FeatureEngineerAgent.create(),
            "hyperparameter_optimizer": HyperparameterOptimizerAgent.create(),
            "report_writer": ReportWriterAgent.create(),
        }

    def _create_tasks(self) -> List[Any]:
        """Create the ML workflow tasks."""
        return get_ml_workflow_tasks(self.agents)

    def _create_crew(self) -> Crew:
        """Create the main crew with all agents and tasks."""
        return Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=config.VERBOSE,
            process=self.process,
        )

    def kickoff(self) -> Any:
        """Execute the ML analysis workflow."""
        try:
            print("🚀 Starting ML Analysis Crew...")
            print(f"Process: {self.process}")
            print(f"Agents: {len(self.agents)}")
            print(f"Tasks: {len(self.tasks)}")
            print("-" * 50)

            result = self.crew.kickoff()

            print("-" * 50)
            print("✅ ML Analysis Complete!")
            return result

        except Exception as e:
            print(f"❌ Error during ML analysis: {str(e)}")
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
    def validate_environment() -> Dict[str, bool]:
        """Validate that the environment is properly configured."""
        return config.validate_api_keys()

    @staticmethod
    def get_status() -> Dict[str, Any]:
        """Get crew status and configuration information."""
        env_status = MLCrew.validate_environment()

        return {
            "environment_ready": all(env_status.values()),
            "api_keys_configured": env_status,
            "config": {
                "verbose": config.VERBOSE,
                "process_type": config.PROCESS_TYPE,
                "outputs_dir": str(config.OUTPUTS_DIR),
            },
            "agents_available": 5,  # Fixed number of agents
            "tasks_available": 5,   # Fixed number of tasks
        }
