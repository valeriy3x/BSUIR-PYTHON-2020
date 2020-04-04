from JSON.to_json import to_json
import pytest
import json


def test_dict():
    to_dump = {5: "cucumber", 7: True, 10: [2, 4, 5]}
    assert to_json(to_dump) == json.dumps(to_dump)


def test_list_tuple():
    to_dump_list = [2, 5, 5.5, "Hello"]
    to_dump_tuple = (4, 6)
    assert to_json(to_dump_list) == json.dumps(to_dump_list)
    assert to_json(to_dump_tuple) == json.dumps(to_dump_tuple)


def test_string():
    assert to_json("I'm Lovin' it") == json.dumps("I'm Lovin' it")


def test_bool():
    assert to_json(True) == json.dumps(True)
    assert to_json(False) == json.dumps(False)


def test_null():
    assert to_json(None) == json.dumps(None)


def test_incorrect_type():
    with pytest.raises(TypeError):
        to_json({2, 4, 5})


def test_incorrect_key():
    with pytest.raises(TypeError):
        to_json({2: "Something", [4, 5]: "Yo"})
