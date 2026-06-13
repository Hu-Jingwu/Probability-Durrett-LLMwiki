#!/usr/bin/env python3
"""Build one unified Probability LLM Viki from chapter-level viki datasets."""

from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATASET_DIR = ROOT / "Probability/LLM_Viki_Dataset"
OUTPUT_DIR = DATASET_DIR / "Probability_Knowledge"


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists() or not path.is_file():
        return []
    records: list[dict] = []
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


def read_tsv_records(path: Path) -> list[dict[str, str]]:
    if not path.exists() or not path.is_file():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv_records(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def first_existing(*paths: Path) -> Path | None:
    for path in paths:
        if path.exists():
            return path
    return None


def load_manifest(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def chapter_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def demote_markdown(markdown: str, levels: int = 1) -> str:
    lines: list[str] = []
    for line in markdown.splitlines():
        if line.startswith("#"):
            match = re.match(r"^(#+)(\s.*)$", line)
            if match:
                hashes, rest = match.groups()
                line = f"{hashes}{'#' * levels}{rest}"
        lines.append(line)
    return "\n".join(lines).strip()


def sort_key_for_section(record: dict) -> tuple[int, str]:
    chapter = int(record.get("chapter") or 0)
    return chapter, str(record.get("section") or "")


def sort_key_for_piece(record: dict) -> tuple[int, str, str]:
    chapter = int(record.get("chapter") or 0)
    return chapter, str(record.get("section") or ""), str(record.get("id") or "")


def unique_by_id(records: list[dict]) -> list[dict]:
    seen: set[str] = set()
    output: list[dict] = []
    for record in records:
        record_id = str(record.get("id") or "")
        if record_id and record_id in seen:
            continue
        if record_id:
            seen.add(record_id)
        output.append(record)
    return output


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chapters: list[dict] = []
    all_section_guides: list[dict] = []
    all_pieces: list[dict] = []
    all_exercise_records: list[dict] = []
    all_method_cards: list[dict] = []
    all_exercise_knowledge: list[dict] = []
    all_flashcards: list[dict[str, str]] = []
    all_method_flashcards: list[dict[str, str]] = []

    for chapter in range(1, 10):
        knowledge_dir = DATASET_DIR / f"Chapter{chapter}_Knowledge"
        exercise_dir = DATASET_DIR / f"Chapter{chapter}_Exercise_Viki"
        if not knowledge_dir.exists():
            continue

        chapter_manifest = load_manifest(knowledge_dir / "manifest.json")
        viki_path = knowledge_dir / f"chapter{chapter}_viki.md"
        exercise_viki_path = first_existing(
            knowledge_dir / f"chapter{chapter}_exercise_viki.md",
            exercise_dir / f"chapter{chapter}_exercise_viki.md",
        )

        viki_text = viki_path.read_text(encoding="utf-8") if viki_path.exists() else ""
        exercise_viki_text = (
            exercise_viki_path.read_text(encoding="utf-8") if exercise_viki_path else ""
        )

        section_guides = read_jsonl(knowledge_dir / f"chapter{chapter}_section_guides.jsonl")
        pieces = read_jsonl(knowledge_dir / f"chapter{chapter}_knowledge_pieces.jsonl")
        exercise_records = read_jsonl(
            first_existing(
                knowledge_dir / f"chapter{chapter}_exercise_records.jsonl",
                exercise_dir / f"chapter{chapter}_exercise_records.jsonl",
            )
            or Path()
        )
        method_cards = read_jsonl(
            first_existing(
                knowledge_dir / f"chapter{chapter}_exercise_method_cards.jsonl",
                exercise_dir / f"chapter{chapter}_exercise_method_cards.jsonl",
            )
            or Path()
        )
        exercise_knowledge = read_jsonl(
            first_existing(
                knowledge_dir / f"chapter{chapter}_exercise_new_knowledge.jsonl",
                exercise_dir / f"chapter{chapter}_exercise_new_knowledge.jsonl",
            )
            or Path()
        )
        flashcards = read_tsv_records(knowledge_dir / f"chapter{chapter}_flashcards.tsv")
        method_flashcards = read_tsv_records(
            first_existing(
                knowledge_dir / f"chapter{chapter}_exercise_method_flashcards.tsv",
                exercise_dir / f"chapter{chapter}_exercise_method_flashcards.tsv",
            )
            or Path()
        )

        chapters.append(
            {
                "chapter": chapter,
                "title": chapter_title(viki_text, f"Durrett Chapter {chapter}"),
                "knowledge_dir": str(knowledge_dir.relative_to(ROOT)),
                "exercise_dir": str(exercise_dir.relative_to(ROOT)) if exercise_dir.exists() else None,
                "section_count": len(section_guides),
                "knowledge_piece_count": len(pieces),
                "exercise_record_count": len(exercise_records),
                "method_card_count": len(method_cards),
                "has_exercise_viki": bool(exercise_viki_text),
                "manifest": chapter_manifest,
                "viki_text": viki_text,
                "exercise_viki_text": exercise_viki_text,
            }
        )

        all_section_guides.extend(section_guides)
        all_pieces.extend(pieces)
        all_exercise_records.extend(exercise_records)
        all_method_cards.extend(method_cards)
        all_exercise_knowledge.extend(exercise_knowledge)
        all_flashcards.extend(flashcards)
        all_method_flashcards.extend(method_flashcards)

    all_section_guides = sorted(all_section_guides, key=sort_key_for_section)
    all_pieces = unique_by_id(sorted(all_pieces, key=sort_key_for_piece))
    all_exercise_records = unique_by_id(sorted(all_exercise_records, key=sort_key_for_piece))
    all_method_cards = unique_by_id(sorted(all_method_cards, key=sort_key_for_piece))
    all_exercise_knowledge = unique_by_id(sorted(all_exercise_knowledge, key=sort_key_for_piece))

    write_jsonl(OUTPUT_DIR / "probability_section_guides.jsonl", all_section_guides)
    write_jsonl(OUTPUT_DIR / "probability_knowledge_pieces.jsonl", all_pieces)
    write_jsonl(OUTPUT_DIR / "probability_exercise_records.jsonl", all_exercise_records)
    write_jsonl(OUTPUT_DIR / "probability_exercise_method_cards.jsonl", all_method_cards)
    write_jsonl(OUTPUT_DIR / "probability_exercise_new_knowledge.jsonl", all_exercise_knowledge)
    write_tsv_records(
        OUTPUT_DIR / "probability_flashcards.tsv",
        all_flashcards,
        ["id", "front", "back", "tags"],
    )
    write_tsv_records(
        OUTPUT_DIR / "probability_exercise_method_flashcards.tsv",
        all_method_flashcards,
        ["id", "front", "back", "tags"],
    )

    now = datetime.now(timezone.utc).isoformat()
    manifest = {
        "name": "durrett_probability_unified_llm_viki",
        "description": "Unified Probability LLM/Viki knowledge base assembled from Durrett chapter-level knowledge and exercise viki datasets.",
        "created_at": now,
        "chapter_count": len(chapters),
        "section_count": len(all_section_guides),
        "knowledge_piece_count": len(all_pieces),
        "exercise_record_count": len(all_exercise_records),
        "method_card_count": len(all_method_cards),
        "exercise_derived_knowledge_count": len(all_exercise_knowledge),
        "flashcard_count": len(all_flashcards),
        "exercise_method_flashcard_count": len(all_method_flashcards),
        "chapters": [
            {key: value for key, value in chapter.items() if not key.endswith("_text")}
            for chapter in chapters
        ],
        "files": [
            "probability_viki.md",
            "probability_knowledge_pieces.jsonl",
            "probability_section_guides.jsonl",
            "probability_exercise_records.jsonl",
            "probability_exercise_method_cards.jsonl",
            "probability_exercise_new_knowledge.jsonl",
            "probability_flashcards.tsv",
            "probability_exercise_method_flashcards.tsv",
            "manifest.json",
        ],
    }
    (OUTPUT_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines: list[str] = [
        "# Durrett Probability LLM Viki",
        "",
        "Source: local Durrett chapter PDFs and solved exercise files under `Probability/`.",
        "",
        "This is the unified Probability LLM/Viki knowledge base assembled from the chapter-level viki datasets. It keeps each chapter's original retrieval notes, then appends exercise method viki material where available.",
        "",
        "These are curated study/LLM retrieval pieces, not verbatim textbook notes.",
        "",
        "## Corpus Index",
        "",
    ]
    for chapter in chapters:
        exercise_note = (
            f"; {chapter['exercise_record_count']} solved-exercise records"
            if chapter["exercise_record_count"]
            else ""
        )
        lines.append(
            f"- Chapter {chapter['chapter']}: {chapter['title']} "
            f"({chapter['section_count']} sections, {chapter['knowledge_piece_count']} knowledge pieces"
            f"{exercise_note})."
        )

    lines.extend(
        [
            "",
            "## Unified Files",
            "",
            "- `probability_knowledge_pieces.jsonl`: all chapter knowledge pieces.",
            "- `probability_section_guides.jsonl`: all section study guides.",
            "- `probability_exercise_records.jsonl`: all available solved-exercise records.",
            "- `probability_exercise_method_cards.jsonl`: all available exercise method cards.",
            "- `probability_exercise_new_knowledge.jsonl`: all exercise-derived reusable knowledge pieces.",
            "- `probability_flashcards.tsv`: all chapter flashcards.",
            "- `probability_exercise_method_flashcards.tsv`: all exercise method flashcards.",
            "- `manifest.json`: corpus counts and chapter provenance.",
            "",
        ]
    )

    for chapter in chapters:
        lines.extend(
            [
                f"## Chapter {chapter['chapter']}",
                "",
                demote_markdown(chapter["viki_text"], levels=2),
                "",
            ]
        )
        if chapter["exercise_viki_text"]:
            lines.extend(
                [
                    f"### Chapter {chapter['chapter']} Exercise Viki",
                    "",
                    demote_markdown(chapter["exercise_viki_text"], levels=3),
                    "",
                ]
            )

    (OUTPUT_DIR / "probability_viki.md").write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
