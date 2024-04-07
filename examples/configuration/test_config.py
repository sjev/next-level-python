""" run pytest to verify correct operation """

import os
from config import MyConfig


def test_defaults() -> None:

    cfg = MyConfig()

    assert cfg.param_a == "foo"
    assert cfg.param_b == [1, 2, 3]


def test_env_override() -> None:
    """
    use environment variables with prefix
    to override parameter values.
    """

    os.environ["myconfig_param_a"] = "bar"
    os.environ["myconfig_param_b"] = "[4,5,6]"

    cfg = MyConfig()

    assert cfg.param_a == "bar"
    assert cfg.param_b == [4, 5, 6]
