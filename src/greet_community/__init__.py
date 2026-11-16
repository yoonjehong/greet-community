"""A small greeting package."""


def greet(name: str) -> str:
    """Return the greeting, using "world" for a blank name."""
    name = name.strip() or "world"
    return f"Hello, {name}!"
