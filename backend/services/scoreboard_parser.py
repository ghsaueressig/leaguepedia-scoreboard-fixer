import re


_RPGID_PATTERN = re.compile(r"\brpgid\s*=\s*([A-Za-z0-9]+_[0-9]+)\b")


def extract_rpgids(wikitext: str) -> list[str]:
    return _RPGID_PATTERN.findall(wikitext)