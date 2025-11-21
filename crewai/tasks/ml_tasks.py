"""
ML Task Definitions for CrewAI workflows.
Contains tasks for complete Random Forest ML pipeline analysis.
"""

from crewai import Task
from typing import List, Dict, Any, Optional
from ..config import config


def create_data_analysis_task(agent) -> Task:
    """Create data analysis task for initial dataset assessment."""
    return Task(
        description="""Conduct a comprehensive analysis of the Random Forest dataset including:
        1. Dataset shape and basic statistics
        2. Missing values assessment and patterns
        3. Feature distributions and data types
        4. Class balance analysis (if classification)
        5. Outlier detection and potential data quality issues
        6. Correlation analysis between features
        7. Recommendations for data preprocessing steps

        Provide detailed insights that will inform the Random Forest model development.""",
        expected_output="Comprehensive data analysis report with statistics, visualizations descriptions, and preprocessing recommendations.",
        agent=agent,
        output_file=config.get_output_path("data_analysis_report.md"),
    )


def create_model_evaluation_task(agent) -> Task:
    """Create model evaluation task for performance assessment."""
    return Task(
        description="""Evaluate the Random Forest model's performance by analyzing:
        1. Accuracy, precision, recall, and F1-score metrics
        2. Confusion matrix analysis and misclassification patterns
        3. ROC curves and AUC scores (for binary classification)
        4. Cross-validation results and stability assessment
        5. Out-of-bag (OOB) score analysis
        6. Comparison with baseline models (if available)
        7. Training vs test performance analysis
        8. Recommendations for model improvement

        Provide actionable insights based on the evaluation results.""",
        expected_output="Detailed model performance evaluation with metrics, visualizations analysis, and improvement recommendations.",
        agent=agent,
        output_file=config.get_output_path("model_evaluation_report.md"),
        context=[create_data_analysis_task.__name__],  # Depends on data analysis
    )


def create_feature_analysis_task(agent) -> Task:
    """Create feature importance and engineering analysis task."""
    return Task(
        description="""Analyze feature importance and engineering opportunities:
        1. Gini importance and permutation importance rankings
        2. Feature correlation with target variable
        3. Identification of redundant or irrelevant features
        4. Potential feature interactions and engineering opportunities
        5. Feature scaling and transformation recommendations
        6. Dimensionality reduction suggestions
        7. Feature selection strategies for improved model performance

        Focus on how features impact Random Forest performance and provide specific engineering recommendations.""",
        expected_output="Feature importance analysis with rankings, engineering recommendations, and feature selection strategy.",
        agent=agent,
        output_file=config.get_output_path("feature_analysis_report.md"),
        context=[create_data_analysis_task.__name__, create_model_evaluation_task.__name__],
    )


def create_hyperparameter_task(agent) -> Task:
    """Create hyperparameter optimization task."""
    return Task(
        description="""Optimize Random Forest hyperparameters for maximum performance:
        1. Current hyperparameter settings analysis
        2. Grid search or random search recommendations
        3. Optimal ranges for key parameters (n_estimators, max_depth, etc.)
        4. Computational efficiency considerations
        5. Cross-validation strategy for hyperparameter tuning
        6. Performance vs complexity trade-off analysis
        7. Final hyperparameter recommendations with expected improvements

        Provide specific, implementable hyperparameter configurations.""",
        expected_output="Hyperparameter optimization analysis with recommended settings, expected performance improvements, and implementation guidance.",
        agent=agent,
        output_file=config.get_output_path("hyperparameter_optimization_report.md"),
        context=[create_model_evaluation_task.__name__],
    )


def create_report_generation_task(agent) -> Task:
    """Create comprehensive report generation task."""
    return Task(
        description="""Create a comprehensive, accessible report on the Random Forest ML project:
        1. Executive summary with key findings and recommendations
        2. Data analysis summary and preprocessing decisions
        3. Model performance evaluation and metrics
        4. Feature importance analysis and engineering insights
        5. Hyperparameter optimization results and settings
        6. Model limitations and potential improvements
        7. Production deployment recommendations
        8. Future work suggestions

        Write in clear, engaging language suitable for both technical and non-technical audiences.
        Include actionable insights and avoid unnecessary technical jargon.""",
        expected_output="Complete project report with executive summary, detailed analysis, and actionable recommendations in accessible language.",
        agent=agent,
        output_file=config.get_output_path("final_ml_report.md"),
        context=[
            create_data_analysis_task.__name__,
            create_model_evaluation_task.__name__,
            create_feature_analysis_task.__name__,
            create_hyperparameter_task.__name__,
        ],
    )


def get_ml_workflow_tasks(agents: Dict[str, Any]) -> List[Task]:
    """Get the complete ML workflow task list in execution order.

    Args:
        agents: Dictionary mapping agent roles to agent instances

    Returns:
        List of tasks in execution order
    """
    return [
        create_data_analysis_task(agents["data_analyst"]),
        create_model_evaluation_task(agents["model_evaluator"]),
        create_feature_analysis_task(agents["feature_engineer"]),
        create_hyperparameter_task(agents["hyperparameter_optimizer"]),
        create_report_generation_task(agents["report_writer"]),
    ]
