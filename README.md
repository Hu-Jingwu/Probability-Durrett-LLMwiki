# Probability Durrett LLMviki Solutions

This repository is a study-oriented LLMviki for Rick Durrett's *Probability:
Theory and Examples*.

It organizes chapter knowledge, solved-exercise methods, reusable proof
patterns, and flashcards into formats that are easy for both humans and LLM/RAG
systems to search.

## What This Is

- A structured probability knowledge base built from Durrett Chapters 1-9.
- A collection of solved-exercise records and method cards for many textbook
  exercises.
- A retrieval-friendly dataset with Markdown, JSONL, and TSV files.
- A personal study companion for probability prelim preparation.

## Unified LLMviki

The main entry point is:

`Probability/LLM_Viki_Dataset/Probability_Knowledge/probability_viki.md`

This file merges the chapter-level LLMvikis into one probability-wide guide.
It currently includes:

- 9 chapters
- 65 section guides
- 523 knowledge pieces
- 357 solved-exercise records
- 53 exercise method cards
- 231 exercise-derived reusable knowledge pieces

The same corpus is also available as machine-readable files:

- `probability_knowledge_pieces.jsonl`
- `probability_section_guides.jsonl`
- `probability_exercise_records.jsonl`
- `probability_exercise_method_cards.jsonl`
- `probability_exercise_new_knowledge.jsonl`
- `probability_flashcards.tsv`
- `probability_exercise_method_flashcards.tsv`
- `manifest.json`

## Chapter-Level Datasets

The folder `Probability/LLM_Viki_Dataset/` also contains per-chapter knowledge
bases such as:

- `Chapter1_Knowledge/`
- `Chapter2_Knowledge/`
- ...
- `Chapter9_Knowledge/`

Each chapter folder contains some combination of:

- human-readable chapter viki Markdown
- section guides
- knowledge pieces
- exercise records
- method cards
- flashcards
- metadata manifests

## Rebuild

After updating any chapter-level LLMviki, rebuild the unified probability viki
with:

```bash
python3 build_probability_viki.py
```

The script regenerates `Probability/LLM_Viki_Dataset/Probability_Knowledge/`
from the chapter-level folders.

## Important Note

These notes and solutions were generated with LLM/Codex assistance and are being
used as a living study dataset. They may contain mistakes. Human checking,
correction, and improvement are expected over time.
