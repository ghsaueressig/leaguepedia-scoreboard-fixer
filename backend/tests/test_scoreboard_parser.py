from backend.services.scoreboard_parser import extract_rpgids


def test_extracts_one_rpgid():
    assert extract_rpgids("{{Match|rpgid=BR1_3285112309}}") == ["BR1_3285112309"]


def test_extracts_multiple_rpgids():
    wikitext = "{{Match|rpgid=BR1_3285112309|rpgid=NA1_1234567890}}"
    assert extract_rpgids(wikitext) == ["BR1_3285112309", "NA1_1234567890"]


def test_allows_whitespace_around_rpgid_parameter():
    wikitext = "{{Match| rpgid \t = \n BR1_3285112309 }}"
    assert extract_rpgids(wikitext) == ["BR1_3285112309"]


def test_returns_empty_list_when_no_rpgid_exists():
    assert extract_rpgids("{{Match|team1=Example|team2=Other}}") == []


def test_preserves_input_order_and_duplicates():
    wikitext = "{{Match|rpgid=NA1_2|rpgid=BR1_1|rpgid=NA1_2}}"
    assert extract_rpgids(wikitext) == ["NA1_2", "BR1_1", "NA1_2"]