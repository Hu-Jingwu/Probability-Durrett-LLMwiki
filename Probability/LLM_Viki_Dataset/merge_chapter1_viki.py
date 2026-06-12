#!/usr/bin/env python3
"""Merge Chapter 1 exercise viki records into the Chapter 1 knowledge base."""

from __future__ import annotations

import csv
import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
KNOWLEDGE_DIR = ROOT / "Probability/LLM_Viki_Dataset/Chapter1_Knowledge"
EXERCISE_DIR = ROOT / "Probability/LLM_Viki_Dataset/Chapter1_Exercise_Viki"

SOURCE_FILE = ROOT / "Probability/Textbook/Chapters/PTE-Chapter1.pdf"
SOURCE_TEX = ROOT / "Probability/Exercises/Chapter1/Chapter1Exercises.tex"
SOURCE_PDF = ROOT / "Probability/Exercises/Chapter1/Chapter1Exercises.pdf"


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def write_jsonl(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def copy_if_needed(src: Path, dst: Path) -> None:
    if src.resolve() == dst.resolve():
        return
    shutil.copy2(src, dst)


def normalize_kind(kind: str) -> str:
    if kind == "exercise-derived-method":
        return "exercise-pattern"
    return kind


def back_text(piece: dict) -> str:
    parts = [piece.get("summary", "")]
    if piece.get("exam_use"):
        parts.append(f"Exam use: {piece['exam_use']}")
    if piece.get("pitfalls"):
        parts.append(f"Pitfall: {piece['pitfalls']}")
    return " ".join(part for part in parts if part)


def write_flashcards(path: Path, pieces: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["id", "front", "back", "tags"])
        for piece in pieces:
            writer.writerow(
                [
                    piece["id"],
                    f"{piece['title']} ({piece['section']})",
                    back_text(piece),
                    ",".join(piece.get("tags", [])),
                ]
            )


def make_markdown(
    path: Path,
    section_guides: list[dict],
    pieces: list[dict],
    method_cards: list[dict],
    exercise_records: list[dict],
) -> None:
    lines: list[str] = []
    lines.extend(
        [
            "# Durrett Chapter 1 LLM Viki: Probability Foundations",
            "",
            "Source: local extracted PDF `Probability/Textbook/Chapters/PTE-Chapter1.pdf`.",
            "",
            "This unified Chapter 1 knowledge base includes the original textbook knowledge pieces plus exercise-derived method patterns from the solved Chapter 1 exercises.",
            "",
            "Exercise source: `Probability/Exercises/Chapter1/Chapter1Exercises.tex` and `Probability/Exercises/Chapter1/Chapter1Exercises.pdf`.",
            "",
            "These are curated study/LLM retrieval pieces, not verbatim textbook notes.",
            "",
            "## Section Guides",
            "",
        ]
    )

    for guide in section_guides:
        section_label = guide["section"]
        goal = guide.get("goal", guide.get("study_goal", ""))
        lines.extend(
            [
                f"### {section_label}",
                "",
                f"- Goal: {goal}",
                "",
                f"- Must master: {', '.join(guide.get('must_master', []))}",
                "",
                f"- Prelim angle: {guide['prelim_angle']}",
                "",
            ]
        )

    lines.extend(["## Knowledge Pieces", ""])
    for piece in pieces:
        lines.extend(
            [
                f"### {piece['title']}",
                "",
                f"- ID: `{piece['id']}`",
                "",
                f"- Section: {piece['section']}",
                "",
                f"- Kind: {piece['kind']}",
                "",
                f"- Summary: {piece['summary']}",
                "",
                f"- Proof idea: {piece.get('proof_idea', '')}",
                "",
                f"- Exam use: {piece.get('exam_use', '')}",
                "",
                f"- Pitfall: {piece.get('pitfalls', '')}",
                "",
                f"- Tags: {', '.join(piece.get('tags', []))}",
                "",
            ]
        )
        if piece.get("source_exercises"):
            lines.extend(
                [
                    f"- Source exercises: {', '.join(piece['source_exercises'])}",
                    "",
                ]
            )

    lines.extend(["## Exercise Method Cards", ""])
    for card in method_cards:
        lines.extend(
            [
                f"### {card['section']} {card['section_topic']}",
                "",
                f"- ID: `{card['id']}`",
                "",
                f"- Method: {card['method_summary']}",
                "",
                f"- Tags: {', '.join(card.get('method_tags', []))}",
                "",
                f"- New knowledge IDs: {', '.join(card.get('new_knowledge_ids', []))}",
                "",
            ]
        )

    by_section: dict[str, list[dict]] = defaultdict(list)
    for record in exercise_records:
        by_section[record["section"]].append(record)

    lines.extend(["## Exercise Record Index", ""])
    for section in sorted(by_section):
        first_topic = by_section[section][0].get("section_topic", "")
        lines.extend([f"### {section} {first_topic}", ""])
        for record in by_section[section]:
            lines.extend(
                [
                    f"- Exercise {record['exercise']}: method tags `"
                    + ", ".join(record.get("method_tags", []))
                    + "`; knowledge used `"
                    + ", ".join(record.get("knowledge_used_ids", []))
                    + "`; new knowledge `"
                    + ", ".join(record.get("new_knowledge_ids", []))
                    + "`.",
                ]
            )
        lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    KNOWLEDGE_DIR.mkdir(parents=True, exist_ok=True)

    current_pieces = read_jsonl(KNOWLEDGE_DIR / "chapter1_knowledge_pieces.jsonl")
    textbook_pieces = [
        piece for piece in current_pieces if not piece["id"].startswith("exercise_method_")
    ]
    write_jsonl(KNOWLEDGE_DIR / "chapter1_textbook_knowledge_pieces.jsonl", textbook_pieces)

    section_guides = read_jsonl(KNOWLEDGE_DIR / "chapter1_section_guides.jsonl")
    exercise_records = read_jsonl(EXERCISE_DIR / "chapter1_exercise_records.jsonl")
    method_cards = read_jsonl(EXERCISE_DIR / "chapter1_exercise_method_cards.jsonl")
    new_knowledge = read_jsonl(EXERCISE_DIR / "chapter1_exercise_new_knowledge.jsonl")

    for name in [
        "chapter1_exercise_records.jsonl",
        "chapter1_exercise_method_cards.jsonl",
        "chapter1_exercise_new_knowledge.jsonl",
        "chapter1_exercise_method_flashcards.tsv",
        "chapter1_exercise_viki.md",
    ]:
        copy_if_needed(EXERCISE_DIR / name, KNOWLEDGE_DIR / name)

    id_to_card: dict[str, dict] = {}
    for card in method_cards:
        for knowledge_id in card.get("new_knowledge_ids", []):
            id_to_card[knowledge_id] = card

    id_to_exercises: dict[str, set[str]] = defaultdict(set)
    id_to_related: dict[str, set[str]] = defaultdict(set)
    for record in exercise_records:
        for knowledge_id in record.get("new_knowledge_ids", []):
            id_to_exercises[knowledge_id].add(record["exercise"])
            id_to_related[knowledge_id].update(record.get("knowledge_used_ids", []))

    now = datetime.now(timezone.utc).isoformat()
    exercise_pieces: list[dict] = []
    for item in new_knowledge:
        card = id_to_card.get(item["id"], {})
        section = card.get("section", "1")
        section_topic = card.get("section_topic", "Chapter 1 exercises")
        exercise_pieces.append(
            {
                "id": item["id"],
                "source": "Solved Durrett Chapter 1 exercises and exercise viki records",
                "source_file": str(SOURCE_TEX),
                "source_pdf": str(SOURCE_PDF),
                "chapter": 1,
                "section": f"{section} Exercises: {section_topic}",
                "title": item["title"],
                "kind": normalize_kind(item.get("kind", "exercise-pattern")),
                "summary": item["summary"],
                "proof_idea": card.get(
                    "method_summary",
                    "Reusable proof or calculation pattern extracted from the solved exercises.",
                ),
                "exam_use": item.get("use_case", ""),
                "pitfalls": "Check the hypotheses before reusing the pattern; many Chapter 1 arguments depend on measurability, integrability, monotonicity, or nonnegativity.",
                "tags": item.get("tags", []),
                "related_ids": sorted(id_to_related.get(item["id"], set())),
                "source_exercises": sorted(id_to_exercises.get(item["id"], set())),
                "created_at": item.get("created_at", now),
                "merged_at": now,
            }
        )

    combined_pieces = textbook_pieces + exercise_pieces
    write_jsonl(KNOWLEDGE_DIR / "chapter1_knowledge_pieces.jsonl", combined_pieces)
    write_flashcards(KNOWLEDGE_DIR / "chapter1_flashcards.tsv", combined_pieces)
    make_markdown(
        KNOWLEDGE_DIR / "chapter1_viki.md",
        section_guides,
        combined_pieces,
        method_cards,
        exercise_records,
    )

    manifest = {
        "name": "durrett_chapter1_probability_foundations_llm_viki",
        "description": "Unified LLM/Viki-style knowledge base for Chapter 1 of Durrett Probability: Theory and Examples, including textbook knowledge pieces and exercise-derived method patterns.",
        "source_file": str(SOURCE_FILE),
        "source_tex": str(SOURCE_TEX),
        "source_pdf": str(SOURCE_PDF),
        "created_at": now,
        "piece_count": len(combined_pieces),
        "textbook_piece_count": len(textbook_pieces),
        "exercise_derived_piece_count": len(exercise_pieces),
        "section_count": len(section_guides),
        "exercise_record_count": len(exercise_records),
        "method_card_count": len(method_cards),
        "files": [
            "chapter1_knowledge_pieces.jsonl",
            "chapter1_textbook_knowledge_pieces.jsonl",
            "chapter1_section_guides.jsonl",
            "chapter1_viki.md",
            "chapter1_flashcards.tsv",
            "chapter1_exercise_records.jsonl",
            "chapter1_exercise_method_cards.jsonl",
            "chapter1_exercise_new_knowledge.jsonl",
            "chapter1_exercise_method_flashcards.tsv",
            "chapter1_exercise_viki.md",
            "manifest.json",
        ],
    }
    (KNOWLEDGE_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
