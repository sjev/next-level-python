#!/usr/bin/env python3
"""
  example configuration using pydantic_settings
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class MyConfig(BaseSettings):

    # configure env variable prefix
    model_config = SettingsConfigDict(env_prefix="myconfig_")

    param_a: str = "foo"
    param_b: list = [1, 2, 3]
