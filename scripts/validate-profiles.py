#!/usr/bin/env python3
"""Validate Grok Bot profile packs against FORMAT.md / botTemplateSchema."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILES = ROOT / "profiles"

REQUIRED_FILES = (
    "profile.json",
    "recipe.json",
    "SOUL.md",
    "ADOPT.md",
    "connectors.md",
)

PROFILE_KEYS = ("name", "description", "title", "avatarShape", "avatarColor")
FORBIDDEN_KEYS = {
    "namedBy",
    "serverId",
    "harness",
    "settings.json",
    "store.db",
    "runs.json",
}

AVATAR_COLORS = {
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "violet",
    "magenta",
    "gray",
}
AVATAR_SHAPES = {
    "blob",
    "pebble",
    "bean",
    "egg",
    "squircle",
    "tablet",
    "capsule",
    "cylinder",
    "hex",
    "gem",
    "crystal",
    "wedge",
    "shield",
    "dome",
    "arch",
    "cloud",
    "teardrop",
    "leaf",
}
KNOWN_PLUGIN_IDS = {
    "github",
    "slack",
    "gmail",
    "google-calendar",
    "google-drive",
    "notion-workspace",
    "linear",
}


def fail(errors: list[str], path: Path, message: str) -> None:
    errors.append(f"{path}: {message}")


def walk_forbidden(obj: object, found: set[str]) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in FORBIDDEN_KEYS:
                found.add(key)
            walk_forbidden(value, found)
    elif isinstance(obj, list):
        for item in obj:
            walk_forbidden(item, found)


def validate_profile_obj(errors: list[str], path: Path, data: dict) -> None:
    if set(data.keys()) != set(PROFILE_KEYS):
        fail(
            errors,
            path,
            f"fields must be exactly {list(PROFILE_KEYS)}, got {sorted(data.keys())}",
        )
        return
    for key in PROFILE_KEYS:
        if not isinstance(data[key], str) or not data[key].strip():
            fail(errors, path, f"{key} must be a non-empty string")
    if data.get("avatarColor") not in AVATAR_COLORS:
        fail(errors, path, f"invalid avatarColor {data.get('avatarColor')!r}")
    if data.get("avatarShape") not in AVATAR_SHAPES:
        fail(errors, path, f"invalid avatarShape {data.get('avatarShape')!r}")
    sentences = [s for s in data.get("description", "").split(".") if s.strip()]
    if len(sentences) > 3:
        fail(errors, path, "description should be 1–3 sentences")


def validate_recipe(errors: list[str], path: Path, recipe: dict, profile: dict) -> None:
    expected = {"profile", "memory", "skills", "routines", "plugins"}
    if set(recipe.keys()) != expected:
        fail(
            errors,
            path,
            f"fields must be exactly {sorted(expected)}, got {sorted(recipe.keys())}",
        )
        return
    if recipe["profile"] != profile:
        fail(errors, path, "recipe.profile must match profile.json")

    memory = recipe["memory"]
    if not isinstance(memory, list) or len(memory) > 32:
        fail(errors, path, "memory must be a list of at most 32 items")
    else:
        for i, item in enumerate(memory):
            if not isinstance(item, dict):
                fail(errors, path, f"memory[{i}] must be an object")
                continue
            if set(item.keys()) != {"kind", "createdAt", "content"}:
                fail(errors, path, f"memory[{i}] fields must be kind, createdAt, content")
            if item.get("kind") not in {"profile", "log"}:
                fail(errors, path, f"memory[{i}].kind must be 'profile' or 'log'")
            if not isinstance(item.get("createdAt"), str) or len(item["createdAt"]) != 10:
                fail(errors, path, f"memory[{i}].createdAt must be YYYY-MM-DD")
            content = item.get("content", "")
            if not isinstance(content, str) or not content.strip():
                fail(errors, path, f"memory[{i}].content must be a non-empty string")
            elif len(content) > 500:
                fail(errors, path, f"memory[{i}].content is {len(content)} chars (max 500)")

    skills = recipe["skills"]
    if not isinstance(skills, list):
        fail(errors, path, "skills must be a list")
    else:
        for i, item in enumerate(skills):
            if not isinstance(item, dict) or set(item.keys()) != {"name", "description", "content"}:
                fail(errors, path, f"skills[{i}] fields must be name, description, content")
                continue
            for key in ("name", "description", "content"):
                if not isinstance(item[key], str) or not item[key].strip():
                    fail(errors, path, f"skills[{i}].{key} must be a non-empty string")

    routines = recipe["routines"]
    if not isinstance(routines, list) or len(routines) > 3:
        fail(errors, path, "routines must be a list of at most 3 items")
    else:
        for i, item in enumerate(routines):
            expected_r = {"name", "slug", "description", "content"}
            if not isinstance(item, dict) or set(item.keys()) != expected_r:
                fail(errors, path, f"routines[{i}] fields must be name, slug, description, content")
                continue
            for key in expected_r:
                if not isinstance(item[key], str) or not item[key].strip():
                    fail(errors, path, f"routines[{i}].{key} must be a non-empty string")

    plugins = recipe["plugins"]
    if not isinstance(plugins, list):
        fail(errors, path, "plugins must be a list")
    else:
        for i, item in enumerate(plugins):
            if not isinstance(item, dict) or set(item.keys()) != {"name", "pluginId"}:
                fail(errors, path, f"plugins[{i}] fields must be name, pluginId")
                continue
            if item["pluginId"] not in KNOWN_PLUGIN_IDS:
                fail(
                    errors,
                    path,
                    f"plugins[{i}].pluginId {item['pluginId']!r} is not a known marketplace id; omit it",
                )


def validate_pack(slug_dir: Path, errors: list[str]) -> None:
    for name in REQUIRED_FILES:
        if not (slug_dir / name).is_file():
            fail(errors, slug_dir / name, "missing required file")

    profile_path = slug_dir / "profile.json"
    recipe_path = slug_dir / "recipe.json"
    if not profile_path.is_file() or not recipe_path.is_file():
        return

    try:
        profile = json.loads(profile_path.read_text())
    except json.JSONDecodeError as exc:
        fail(errors, profile_path, f"invalid JSON: {exc}")
        return
    try:
        recipe = json.loads(recipe_path.read_text())
    except json.JSONDecodeError as exc:
        fail(errors, recipe_path, f"invalid JSON: {exc}")
        return

    if not isinstance(profile, dict) or not isinstance(recipe, dict):
        fail(errors, slug_dir, "profile.json and recipe.json must be objects")
        return

    forbidden: set[str] = set()
    walk_forbidden(profile, forbidden)
    walk_forbidden(recipe, forbidden)
    if forbidden:
        fail(errors, slug_dir, f"forbidden keys present: {sorted(forbidden)}")

    validate_profile_obj(errors, profile_path, profile)
    validate_recipe(errors, recipe_path, recipe, profile)


def main() -> int:
    if not PROFILES.is_dir():
        print("profiles/ is missing", file=sys.stderr)
        return 1
    errors: list[str] = []
    packs = sorted(p for p in PROFILES.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not packs:
        print("no profile packs found", file=sys.stderr)
        return 1
    for pack in packs:
        validate_pack(pack, errors)
    if errors:
        print(f"{len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    print(f"ok: {len(packs)} profile pack(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
