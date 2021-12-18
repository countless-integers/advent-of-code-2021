import pytest
from main import part1, part2


@pytest.mark.parametrize(
    "paths,expected_path_count",
    [
        pytest.param(
            [
                ('start', 'A'),
                ('start', 'b'),
                ('A', 'c'),
                ('A', 'b'),
                ('b', 'd'),
                ('A', 'end'),
                ('b', 'end'),
            ],
            10,
            id="Example 1"
        ),
        pytest.param(
            [
                ('dc', 'end'),
                ('HN', 'start'),
                ('start', 'kj'),
                ('dc', 'start'),
                ('dc', 'HN'),
                ('LN', 'dc'),
                ('HN', 'end'),
                ('kj', 'sa'),
                ('kj', 'HN'),
                ('kj', 'dc'),
            ],
            19,
            id="Example 2"
        ),
        pytest.param(
            [
                ('fs', 'end'),
                ('he', 'DX'),
                ('fs', 'he'),
                ('start', 'DX'),
                ('pj', 'DX'),
                ('end', 'zg'),
                ('zg', 'sl'),
                ('zg', 'pj'),
                ('pj', 'he'),
                ('RW', 'he'),
                ('fs', 'DX'),
                ('pj', 'RW'),
                ('zg', 'RW'),
                ('start', 'pj'),
                ('he', 'WI'),
                ('zg', 'he'),
                ('pj', 'fs'),
                ('start', 'RW'),
            ],
            226,
            id="Example 3"
        ),
    ]
)
def test_part1(paths: list[tuple[str, str]], expected_path_count : int) -> None:
    assert expected_path_count == part1(paths)


@pytest.mark.parametrize(
    "paths,expected_path_count",
    [
        pytest.param(
            [
                ('start', 'A'),
                ('start', 'b'),
                ('A', 'c'),
                ('A', 'b'),
                ('b', 'd'),
                ('A', 'end'),
                ('b', 'end'),
            ],
            36,
            id="Example 1"
        ),
        pytest.param(
            [
                ('dc', 'end'),
                ('HN', 'start'),
                ('start', 'kj'),
                ('dc', 'start'),
                ('dc', 'HN'),
                ('LN', 'dc'),
                ('HN', 'end'),
                ('kj', 'sa'),
                ('kj', 'HN'),
                ('kj', 'dc'),
            ],
            103,
            id="Example 2"
        ),
        pytest.param(
            [
                ('fs', 'end'),
                ('he', 'DX'),
                ('fs', 'he'),
                ('start', 'DX'),
                ('pj', 'DX'),
                ('end', 'zg'),
                ('zg', 'sl'),
                ('zg', 'pj'),
                ('pj', 'he'),
                ('RW', 'he'),
                ('fs', 'DX'),
                ('pj', 'RW'),
                ('zg', 'RW'),
                ('start', 'pj'),
                ('he', 'WI'),
                ('zg', 'he'),
                ('pj', 'fs'),
                ('start', 'RW'),
            ],
            3509,
            id="Example 3"
        ),
    ]
)
def test_part2(paths: list[tuple[str, str]], expected_path_count : int) -> None:
    assert expected_path_count == part2(paths)