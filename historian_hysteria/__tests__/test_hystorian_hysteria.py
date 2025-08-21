import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from historian_hysteria import hystorian_histeria, open_inputs_file

def test_open_inputs_file():
    result = open_inputs_file("historian_hysteria/__tests__/inputs.txt")

    assert isinstance(result, list)
    assert len(result) > 0

def test_hystorian_hysteria():
    assert hystorian_histeria(left_list, second_list) == 11