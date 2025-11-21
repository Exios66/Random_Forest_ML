"""
CrewAI Agents Module
Contains specialized agents for various workflows.
"""

# ML Agents
from .data_analyst import DataAnalystAgent
from .model_evaluator import ModelEvaluatorAgent
from .feature_engineer import FeatureEngineerAgent
from .hyperparameter_optimizer import HyperparameterOptimizerAgent
from .report_writer import ReportWriterAgent

# Research & Content Agents
from .research_content import (
    ResearchAnalystAgent as ContentResearchAnalystAgent,
    ContentStrategistAgent,
    FactCheckerAgent,
    EditorAgent,
    PublisherAgent,
)

# Development & Code Agents
from .dev_code import (
    CodeArchitectAgent,
    DeveloperAgent,
    CodeReviewerAgent,
    TestEngineerAgent,
    DevOpsAgent,
)

# Academic Research Agents
from .research_academic import (
    LiteratureReviewerAgent,
    ResearchDesignerAgent,
    AcademicDataAnalystAgent,
    MethodologyExpertAgent,
    AcademicWriterAgent,
)

# Business Intelligence Agents
from .business_intelligence import (
    MarketResearcherAgent,
    BusinessDataAnalystAgent,
    StrategyConsultantAgent,
    FinancialAnalystAgent,
    BusinessReporterAgent,
)

# Documentation Agents
from .documentation import (
    ContentOrganizerAgent,
    TechnicalWriterAgent,
    KnowledgeManagerAgent,
    DocumentationArchitectAgent,
    QualityAssuranceAgent,
)

__all__ = [
    # ML Agents
    "DataAnalystAgent",
    "ModelEvaluatorAgent",
    "FeatureEngineerAgent",
    "HyperparameterOptimizerAgent",
    "ReportWriterAgent",

    # Research & Content Agents
    "ContentResearchAnalystAgent",
    "ContentStrategistAgent",
    "FactCheckerAgent",
    "EditorAgent",
    "PublisherAgent",

    # Development & Code Agents
    "CodeArchitectAgent",
    "DeveloperAgent",
    "CodeReviewerAgent",
    "TestEngineerAgent",
    "DevOpsAgent",

    # Academic Research Agents
    "LiteratureReviewerAgent",
    "ResearchDesignerAgent",
    "AcademicDataAnalystAgent",
    "MethodologyExpertAgent",
    "AcademicWriterAgent",

    # Business Intelligence Agents
    "MarketResearcherAgent",
    "BusinessDataAnalystAgent",
    "StrategyConsultantAgent",
    "FinancialAnalystAgent",
    "BusinessReporterAgent",

    # Documentation Agents
    "ContentOrganizerAgent",
    "TechnicalWriterAgent",
    "KnowledgeManagerAgent",
    "DocumentationArchitectAgent",
    "QualityAssuranceAgent",
]
