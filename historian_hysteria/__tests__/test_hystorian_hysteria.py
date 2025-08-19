import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from historian_hysteria import hystorian_histeria

def test_hystorian_hysteria(left_list, second_list):
    assert hystorian_histeria(left_list, second_list) == 11