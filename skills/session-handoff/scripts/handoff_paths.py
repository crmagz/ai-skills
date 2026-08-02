"""Storage helpers for Codex handoffs with read compatibility for legacy files."""

from pathlib import Path


def primary_handoffs_dir(project_path: str) -> Path:
    """Return the write location for new Codex handoffs."""

    return Path(project_path) / ".codex" / "handoffs"


def handoff_dirs(project_path: str) -> list[Path]:
    """Return readable handoff locations, newest format first."""

    project = Path(project_path)
    return [project / ".codex" / "handoffs", project / ".claude" / "handoffs"]


def project_root_for_handoff(handoff_path: str | Path) -> Path:
    """Infer the repository root from either supported handoff location."""

    path = Path(handoff_path).resolve()
    if path.parent.name == "handoffs" and path.parent.parent.name in {".codex", ".claude"}:
        return path.parent.parent.parent
    return path.parent
