# CrewAI Multi-Agent Swarm System

A comprehensive multi-agent framework using CrewAI, featuring multiple specialized agent swarms for different domains including machine learning, research, development, business intelligence, and documentation.

## 🤖 Overview

This project implements a versatile multi-agent system where different specialized agent swarms collaborate on complex workflows. Each swarm contains domain-specific agents designed for particular tasks and industries.

## 🚀 Available Agent Swarms

### 1. 🤖 ML Analysis Swarm
**Specialization**: Random Forest and machine learning evaluation
**Agents**: 5 specialized ML agents
- **Data Analyst**: Dataset exploration and preprocessing recommendations
- **Model Evaluator**: Performance assessment and comparison analysis
- **Feature Engineer**: Feature importance analysis and engineering suggestions
- **Hyperparameter Optimizer**: Parameter tuning and optimization strategies
- **Report Writer**: Comprehensive report generation for stakeholders

### 2. 🔬 Research Swarm
**Specialization**: ML research, trends, and innovation
**Agents**: 4 research-focused agents
- **Literature Reviewer**: Academic paper analysis and scholarly research
- **Trend Analyzer**: Industry trends and market developments
- **Innovation Scout**: Novel applications and breakthrough technologies
- **Research Summarizer**: Synthesis of research findings

### 3. 🎓 Academic Research Swarm
**Specialization**: Scholarly research and academic analysis
**Agents**: 5 academic research agents
- **Literature Reviewer**: Comprehensive academic literature review
- **Research Designer**: Experimental design and methodology
- **Academic Data Analyst**: Statistical analysis for research
- **Methodology Expert**: Research methodology validation
- **Academic Writer**: Scholarly paper and report writing

### 4. ✍️ Content Research Swarm
**Specialization**: Content creation and research
**Agents**: 5 content-focused agents
- **Research Analyst**: Content research and data gathering
- **Content Strategist**: Content planning and strategy development
- **Fact Checker**: Information verification and validation
- **Editor**: Content editing and quality assurance
- **Publisher**: Content publishing and distribution

### 5. 💼 Business Intelligence Swarm
**Specialization**: Market analysis and business intelligence
**Agents**: 5 business intelligence agents
- **Market Researcher**: Market analysis and competitive intelligence
- **Business Data Analyst**: Business metrics and KPI analysis
- **Strategy Consultant**: Strategic planning and recommendations
- **Financial Analyst**: Financial modeling and forecasting
- **Business Reporter**: Business report generation

### 6. 💻 Development & Code Swarm
**Specialization**: Software development and coding workflows
**Agents**: 5 development-focused agents
- **Code Architect**: System design and architecture planning
- **Developer**: Code implementation and development
- **Code Reviewer**: Code review and quality assurance
- **Test Engineer**: Testing strategy and implementation
- **DevOps Agent**: Deployment and infrastructure management

### 7. 📚 Documentation Swarm
**Specialization**: Technical writing and documentation
**Agents**: 5 documentation-focused agents
- **Content Organizer**: Information architecture and organization
- **Technical Writer**: Technical documentation creation
- **Knowledge Manager**: Knowledge base management
- **Documentation Architect**: Documentation system design
- **Quality Assurance**: Documentation review and validation

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or navigate to the crewai directory
cd crewai

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Copy environment template
cp config/.env.example .env

# Edit .env with your API keys
# At minimum, you need OPENAI_API_KEY
```

### 3. Run Agent Swarms

```bash
# Check status and available swarms
python main.py --status
python main.py --list-crews

# Setup environment
python main.py --setup

# Run different swarms
python main.py --run ml                    # ML analysis
python main.py --run research              # Research trends
python main.py --run research_academic     # Academic research
python main.py --run business_intelligence # Business analysis
python main.py --run dev_code              # Development workflows
python main.py --run documentation         # Technical docs

# Or run default ML analysis
python main.py
```

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key (or compatible local model setup)
- Optional: Serper.dev API key for web search functionality

## 🏗️ Architecture

### Directory Structure

```
crewai/
├── config/                 # Configuration management
│   ├── __init__.py
│   ├── settings.py        # Centralized settings
│   └── .env.example       # Environment template
├── agents/                # Specialized ML agents
│   ├── __init__.py
│   ├── data_analyst.py
│   ├── model_evaluator.py
│   ├── feature_engineer.py
│   ├── hyperparameter_optimizer.py
│   └── report_writer.py
├── tasks/                 # ML workflow tasks
│   ├── __init__.py
│   └── ml_tasks.py
├── tools/                 # Custom ML tools
│   ├── __init__.py
│   └── ml_tools.py
├── crews/                 # Crew orchestration
│   ├── __init__.py
│   └── ml_crew.py
├── outputs/               # Generated reports
├── requirements.txt       # Dependencies
├── main.py               # Entry point
└── README.md            # This file
```

### Agent Specializations

#### 1. Data Analyst Agent
- **Role**: Senior Data Analyst
- **Focus**: Data quality assessment, statistical analysis, preprocessing recommendations
- **Tools**: Dataset analysis, statistical validation

#### 2. Model Evaluator Agent
- **Role**: ML Model Evaluator
- **Focus**: Performance metrics, model comparison, validation strategies
- **Tools**: Performance analysis, cross-validation assessment

#### 3. Feature Engineer Agent
- **Role**: Feature Engineering Specialist
- **Focus**: Feature importance, engineering opportunities, selection strategies
- **Tools**: Feature analysis, correlation assessment

#### 4. Hyperparameter Optimizer Agent
- **Role**: Hyperparameter Optimization Expert
- **Focus**: Parameter tuning, optimization strategies, performance trade-offs
- **Tools**: Parameter search, validation curves

#### 5. Report Writer Agent
- **Role**: ML Project Report Writer
- **Focus**: Technical writing, stakeholder communication, comprehensive reporting
- **Tools**: Document generation, content structuring

## 🔧 Configuration

### Environment Variables

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional - Web search
SERPER_API_KEY=your_serper_api_key_here

# Optional - Local models (Ollama)
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_MODEL_NAME=your_local_model

# Optional - Alternative providers
ANTHROPIC_API_KEY=your_anthropic_key
GROQ_API_KEY=your_groq_key

# CrewAI settings
CREWAI_VERBOSE=True
CREWAI_PROCESS=sequential
```

### Process Types

- **Sequential**: Tasks execute in order (default)
- **Hierarchical**: Manager agent coordinates delegation

## 📊 Workflow Tasks

The ML analysis workflow consists of 5 sequential tasks:

1. **Data Analysis**: Comprehensive dataset assessment
2. **Model Evaluation**: Performance metrics and validation
3. **Feature Analysis**: Importance ranking and engineering
4. **Hyperparameter Optimization**: Parameter tuning recommendations
5. **Report Generation**: Complete project documentation

## 🛠️ Usage Examples

### Basic Usage

```python
# Command line usage
python main.py --run ml  # Run ML analysis swarm

# Or programmatically
from crews import MLCrew

crew = MLCrew()
result = crew.kickoff()
print(result)
```

### Running Different Swarms

```python
from crews import (
    ResearchCrew,
    BusinessIntelligenceCrew,
    DevCodeCrew,
    DocumentationCrew
)

# Research swarm for ML trends
research_crew = ResearchCrew()
research_results = research_crew.kickoff()

# Business intelligence analysis
bi_crew = BusinessIntelligenceCrew()
bi_results = bi_crew.kickoff()

# Development workflow
dev_crew = DevCodeCrew()
dev_results = dev_crew.kickoff()
```

### Custom Configuration

```python
from crews import get_crew_class
from config import config

# Dynamically select crew type
crew_type = "research_academic"
crew_class = get_crew_class(crew_type)

# Configure for hierarchical process
crew = crew_class(process="hierarchical")

# Check environment
from crews import MLCrew
status = MLCrew.validate_environment()
print("Environment ready:", all(status.values()))

# Run analysis
result = crew.kickoff()
```

### Individual Agent Access

```python
from crews import MLCrew

crew = MLCrew()

# Access specific agents
data_agent = crew.get_agent("data_analyst")
eval_agent = crew.get_agent("model_evaluator")

# Access specific tasks
analysis_task = crew.get_task(0)  # Data analysis
```

## 📁 Output Files

Each swarm generates specialized reports in the `outputs/` directory. Report names vary by swarm type:

### ML Analysis Swarm Reports
- `data_analysis_report.md` - Dataset analysis and preprocessing recommendations
- `model_evaluation_report.md` - Performance metrics and evaluation results
- `feature_analysis_report.md` - Feature importance and engineering insights
- `hyperparameter_optimization_report.md` - Parameter tuning recommendations
- `final_ml_report.md` - Complete project report for stakeholders

### Research Swarm Reports
- `literature_review_report.md` - Academic literature analysis
- `trend_analysis_report.md` - Industry trend assessment
- `innovation_scouting_report.md` - Novel applications and breakthroughs
- `research_synthesis_report.md` - Integrated research findings

### Other Swarm Reports
Reports are automatically named based on the swarm type and contain specialized content relevant to each domain (business intelligence, development, documentation, etc.).

## 🔍 Troubleshooting

### Common Issues

1. **Missing API Keys**
   ```bash
   python main.py --status     # Check configuration
   python main.py --setup      # Guided setup
   python main.py --list-crews # See available swarms
   ```

2. **Import Errors**
   ```bash
   pip install -r requirements.txt
   ```

3. **Network Issues**
   - Check API key validity
   - Verify internet connectivity
   - Check rate limits

4. **Unknown Crew Type**
   ```bash
   python main.py --list-crews  # See available crew types
   python main.py --run ml      # Use correct crew name
   ```

5. **Local Model Setup**
   ```bash
   # For Ollama
   OPENAI_API_BASE=http://localhost:11434/v1
   OPENAI_MODEL_NAME=your-model-name
   ```

6. **Swarm-Specific Issues**
   - **ML Swarm**: Ensure scikit-learn and pandas are installed
   - **Research Swarm**: Requires SerperDevTool for web search
   - **Dev/Code Swarm**: May need additional development tools
   - **Documentation Swarm**: Focuses on content generation

### Debug Mode

```bash
# Enable verbose logging
export CREWAI_VERBOSE=True
python main.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of the Random Forest ML analysis suite.

## 🔗 Related Projects

- [CrewAI Framework](https://github.com/crewAIInc/crewAI)
- [Random Forest ML Project](../README.md)
- [CrewAI Examples](https://github.com/crewAIInc/crewAI-examples)

## 📞 Support

For issues specific to this CrewAI implementation:
1. Check the troubleshooting section
2. Review the generated logs
3. Open an issue with error details and configuration

For CrewAI framework questions, refer to the [official documentation](https://docs.crewai.com).
