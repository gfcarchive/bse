# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import mod
from schema import SchemaError  # type: ignore


def test_globals() -> None:
    h = """WebBanking {
  version = 1.0,
  url = "https://www.mysite.com",
  services = {"Service Name"},
  description = "Service Description"
}"""

    m = mod.LuaMod(h)
    assert m.version == 1.0
    assert m.url == "https://www.mysite.com"
    assert m.description == "Service Description"
    assert m.name == "Service Name"
    assert m.slug == "string"


@pytest.mark.parametrize(
    "script",
    [
        """WebBanking {
url = "https://www.mysite.com",
services = {"Service Name"},
description = "Service Description"
}""",
        """WebBanking {
version = 1.0,
services = {"Service Name"},
description = "Service Description"
}""",
        """WebBanking {
version = 1.0,
url = "https://www.mysite.com",
description = "Service Description"
}""",
        """WebBanking {
version = 1.0,
url = "https://www.mysite.com",
services = {"Service Name"},
}""",
    ],
)
def test_missing_global(script: str) -> None:
    with pytest.raises(SchemaError):
        mod.LuaMod(script)
