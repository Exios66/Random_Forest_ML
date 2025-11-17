"""
CrewAI Configuration Settings
Centralized configuration management for the ML agent swarm.
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not installed, continue without it
    pass


class Config:
    """Configuration class for CrewAI ML agents."""

    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    SERPER_API_KEY: Optional[str] = os.getenv("SERPER_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")

    # Local model configuration
    OPENAI_API_BASE: Optional[str] = os.getenv("OPENAI_API_BASE")
    OPENAI_MODEL_NAME: Optional[str] = os.getenv("OPENAI_MODEL_NAME")

    # CrewAI settings
    VERBOSE: bool = os.getenv("CREWAI_VERBOSE", "True").lower() == "true"
    PROCESS_TYPE: str = os.getenv("CREWAI_PROCESS", "sequential")

    # Project paths
    PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
    CREWAI_ROOT: Path = Path(__file__).parent.parent
    OUTPUTS_DIR: Path = CREWAI_ROOT / "outputs"

    # ML Configuration
    DEFAULT_RANDOM_STATE: int = 42
    DEFAULT_TEST_SIZE: float = 0.2
    DEFAULT_CV_FOLDS: int = 5

    @classmethod
    def validate_api_keys(cls) -> Dict[str, bool]:
        """Validate that required API keys are present."""
        keys_status = {
            "OPENAI_API_KEY": bool(cls.OPENAI_API_KEY),
            "SERPER_API_KEY": bool(cls.SERPER_API_KEY),
            "ANTHROPIC_API_KEY": bool(cls.ANTHROPIC_API_KEY),
            "GROQ_API_KEY": bool(cls.GROQ_API_KEY),
        }
        return keys_status

    @classmethod
    def get_llm_config(cls) -> Dict[str, Any]:
        """Get LLM configuration for CrewAI agents."""
        config = {}

        if cls.OPENAI_API_BASE:
            config.update({
                "base_url": cls.OPENAI_API_BASE,
                "api_key": cls.OPENAI_API_KEY or "sk-placeholder-key",
            })
            if cls.OPENAI_MODEL_NAME:
                config["model"] = cls.OPENAI_MODEL_NAME
        elif cls.OPENAI_API_KEY:
            config.update({
                "api_key": cls.OPENAI_API_KEY,
            })

        return config

    @classmethod
    def ensure_outputs_dir(cls) -> None:
        """Ensure the outputs directory exists."""
        cls.OUTPUTS_DIR.mkdir(exist_ok=True)

    @classmethod
    def get_output_path(cls, filename: str) -> Path:
        """Get full path for output file."""
        cls.ensure_outputs_dir()
        return cls.OUTPUTS_DIR / filename


# Global config instance
config = Config()
