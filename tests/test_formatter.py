from colorizer.colorizer import Colorizer
# noinspection PyUnresolvedReferences
from colorizer.colors import *
from colorizer.formatter import COLOR_START, CHAR, COLOR_END, tokenize, format_color_string, ColorBracketOpenedButNotClosed
from pytest import fixture, raises


@fixture
def colorizer():
    return Colorizer()


def test_can_tokenize_a_basic_string():
    string = '<abc> <d>'
    expected = [
        (COLOR_START, '<'),
        (CHAR, 'a'),
        (CHAR, 'b'),
        (CHAR, 'c'),
        (COLOR_END, '>'),
        (CHAR, ' '),
        (COLOR_START, '<'),
        (CHAR, 'd'),
        (COLOR_END, '>')
    ]
    assert expected == tokenize(string)


def test_can_tokenize_a_string_with_escaped_brackets():
    string = '<a> <<>> <b>'
    expected = [
        (COLOR_START, '<'),
        (CHAR, 'a'),
        (COLOR_END, '>'),
        (CHAR, ' '),
        (CHAR, '<'),
        (CHAR, '>'),
        (CHAR, ' '),
        (COLOR_START, '<'),
        (CHAR, 'b'),
        (COLOR_END, '>')
    ]
    assert expected == tokenize(string)


def test_can_tokenize_a_string_with_escaped_brackets_in_color_sequence():
    string = '<h<<e>>llo> a<w>'
    expected = [
        (COLOR_START, '<'),
        (CHAR, 'h'),
        (CHAR, '<'),
        (CHAR, 'e'),
        (CHAR, '>'),
        (CHAR, 'l'),
        (CHAR, 'l'),
        (CHAR, 'o'),
        (COLOR_END, '>'),
        (CHAR, ' '),
        (CHAR, 'a'),
        (COLOR_START, '<'),
        (CHAR, 'w'),
        (COLOR_END, '>')
    ]
    assert expected == tokenize(string)


def test_identifies_right_bracket_as_char_when_color_not_started():
    string = '<a> z>'
    expected = [
        (COLOR_START, '<'),
        (CHAR, 'a'),
        (COLOR_END, '>'),
        (CHAR, ' '),
        (CHAR, 'z'),
        (CHAR, '>')
    ]
    assert expected == tokenize(string)


def test_can_identify_improperly_nested_brackets():
    string = '<asdf'
    with raises(ColorBracketOpenedButNotClosed):
        tokenize(string)


def test_can_format_a_regular_color_string(colorizer):
    string = '<hello> <world>'
    colors = [BRIGHT_RED_ON_MAGENTA, GREEN_ON_WHITE]
    assert format_color_string(string, colors) == '{}hello{} {}world'.format(BRIGHT_RED_ON_MAGENTA, DEFAULT_COLOR,
                                                                             GREEN_ON_WHITE)


def test_can_format_string_with_escaped_brackets(colorizer):
    string = '<hello> <<>> <world>'
    colors = [BRIGHT_RED_ON_MAGENTA, GREEN_ON_WHITE]
    assert format_color_string(string, colors) == '{}hello{} <> {}world'.format(BRIGHT_RED_ON_MAGENTA, DEFAULT_COLOR,
                                                                                GREEN_ON_WHITE)


def test_can_format_with_escaped_brackets_within_brackets(colorizer):
    string = '<hel<<>>lo> <world>'
    colors = [BRIGHT_RED_ON_MAGENTA, GREEN_ON_WHITE]
    assert format_color_string(string, colors) == '{}hel<>lo{} {}world'.format(BRIGHT_RED_ON_MAGENTA, DEFAULT_COLOR,
                                                                               GREEN_ON_WHITE)


def test_can_format_string_without_colors(colorizer):
    string = 'hello world'
    colors = []
    assert format_color_string(string, colors) == DEFAULT_COLOR + string


def test_plays_nicely_with_builtin_format(colorizer):
    string = '<{}> <{}>'.format('hello', 'world')
    colors = [BRIGHT_RED_ON_MAGENTA, GREEN_ON_WHITE]
    assert format_color_string(string, colors) == '{}hello{} {}world'.format(BRIGHT_RED_ON_MAGENTA, DEFAULT_COLOR,
                                                                             GREEN_ON_WHITE)


def test_plays_nicely_with_fstrings(colorizer):
    hello, world = 'hello', 'world'
    string = f'<{hello}> <{world}>'
    colors = [BRIGHT_RED_ON_MAGENTA, GREEN_ON_WHITE]
    assert format_color_string(string, colors) == '{}hello{} {}world'.format(BRIGHT_RED_ON_MAGENTA, DEFAULT_COLOR,
                                                                             GREEN_ON_WHITE)
