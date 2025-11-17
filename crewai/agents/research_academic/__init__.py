"""
Academic Research Agents Module
"""

from .literature_reviewer import LiteratureReviewerAgent
from .research_designer import ResearchDesignerAgent
from .data_analyst import DataAnalystAgent as AcademicDataAnalystAgent
from .methodology_expert import MethodologyExpertAgent
from .academic_writer import AcademicWriterAgent

__all__ = [
    "LiteratureReviewerAgent",
    "ResearchDesignerAgent",
    "AcademicDataAnalystAgent",
    "MethodologyExpertAgent",
    "AcademicWriterAgent",
]
