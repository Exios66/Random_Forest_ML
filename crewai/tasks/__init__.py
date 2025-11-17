"""
CrewAI ML Tasks Module
Contains task definitions for machine learning workflows.
"""

from .ml_tasks import (
    create_data_analysis_task,
    create_model_evaluation_task,
    create_feature_analysis_task,
    create_hyperparameter_task,
    create_report_generation_task,
    get_ml_workflow_tasks,
)
from .research_tasks import (
    create_literature_review_task,
    create_trend_analysis_task,
    create_innovation_scouting_task,
    create_research_synthesis_task,
    get_research_workflow_tasks,
)

__all__ = [
    # ML Tasks
    "create_data_analysis_task",
    "create_model_evaluation_task",
    "create_feature_analysis_task",
    "create_hyperparameter_task",
    "create_report_generation_task",
    "get_ml_workflow_tasks",
    # Research Tasks
    "create_literature_review_task",
    "create_trend_analysis_task",
    "create_innovation_scouting_task",
    "create_research_synthesis_task",
    "get_research_workflow_tasks",
]
