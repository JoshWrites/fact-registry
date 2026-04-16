# Methodology — LLM-Assisted Research

## Role of LLM Assistance

This project uses Claude (Anthropic) as a co-researcher. The LLM performs:

- **Literature survey** — searching for and synthesizing prior work, with human verification of sources
- **Experimental design** — proposing hypotheses and test methods, with human approval before execution
- **Code generation** — writing extraction scripts, migration tools, and analysis code
- **Synthesis** — compiling findings across research threads into structured documents

## What the LLM Does NOT Do

- Make final decisions about project direction
- Determine whether a result is meaningful (human judgment)
- Verify its own factual claims about prior work (human cross-checks sources)
- Replace domain expertise about the knowledge base content

## Attribution Convention

- Git commits include `Co-Authored-By: Claude` when LLM-generated code or text is committed
- Each research finding notes whether it came from LLM search, human observation, or both
- Prompts used for key findings are saved as artifacts in experiment directories

## Reproducibility

- LLM outputs are non-deterministic. Critical experiments note the model version and are run multiple times where feasible.
- All data processing scripts are committed and runnable.
- Sample data is anonymized for public reproducibility; full data remains in the private project repo.

## Tools Used

- **Claude Code** (Anthropic) — primary research and development interface
- **Claude API** — programmatic extraction and analysis at scale
- **Ollama** — local model inference for embedding and classification tasks
- **sentence-transformers** — local embedding models (E5, BGE)
- **SQLite** — data storage and querying
- **Python** — all tooling and scripts
