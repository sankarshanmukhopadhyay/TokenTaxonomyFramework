#!/usr/bin/env python3
"""Check local Markdown links for repository and GitHub Pages compatibility."""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

IGNORE_DIRS = {".git", "node_modules", "vendor", "_site"}
LINK_RE = re.compile(r"(?<!!)(?:\[[^\]]+\]\(([^)]+)\)|<([^>]+)>)")


def iter_markdown(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto"}


def normalize_target(target: str, *, autolink: bool = False) -> str | None:
    target = target.strip()
    if not target or target.startswith("#") or target == "-":
        return None
    if autolink and not is_external(target):
        # Avoid treating HTML tags such as <sub> as repository links.
        return None
    if target.startswith("{") or (" " in target and not target.startswith("./") and not target.startswith("../")):
        return None
    if ("," in target or "[" in target or "]" in target) and "/" not in target:
        return None
    if len(target) <= 3 and "/" not in target and "." not in target:
        return None
    if is_external(target):
        return None
    parsed = urlparse(target)
    path = unquote(parsed.path)
    if not path:
        return None
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local Markdown links")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failures: list[str] = []
    checked = 0

    for md_file in iter_markdown(root):
        text = md_file.read_text(encoding="utf-8", errors="ignore")
        for lineno, line in enumerate(text.splitlines(), start=1):
            if line.lstrip().startswith("```"):
                # The checker is intentionally conservative; formula grammar examples
                # and pseudo links in fenced blocks should not create repo failures.
                continue
            for match in LINK_RE.finditer(line):
                raw = match.group(1) or match.group(2) or ""
                target = normalize_target(raw, autolink=bool(match.group(2)))
                if target is None:
                    continue
                candidate = (md_file.parent / target).resolve()
                checked += 1
                if not str(candidate).startswith(str(root)):
                    failures.append(f"{md_file.relative_to(root)}:{lineno} -> {raw} leaves repository")
                    continue
                if candidate.exists():
                    continue
                # GitHub Pages can resolve directory links and markdown-to-html links;
                # check common repository-side equivalents before failing.
                alternates = []
                if candidate.suffix == "":
                    alternates.extend([candidate / "README.md", candidate / "Readme.md", candidate.with_suffix(".md")])
                if candidate.suffix == ".html":
                    alternates.append(candidate.with_suffix(".md"))
                if not any(alt.exists() for alt in alternates):
                    failures.append(f"{md_file.relative_to(root)}:{lineno} -> {raw}")

    if failures:
        print(f"Checked {checked} local Markdown links")
        print(f"Broken local links: {len(failures)}")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Checked {checked} local Markdown links")
    print("Broken local links: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
