#skip & skipif marker
import pytest

@pytest.mark.skip(reason="This test is skipped temporarily as functionality is not yet developed")
def test_todo_feature():
    assert False  # This won't run

import sys
print(sys.platform)
@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only_feature():
    assert True
