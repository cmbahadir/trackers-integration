# Copyright (c) 2022 Alexander Todorov <atodorov@MrSenko.com>

# Licensed under the GPL 3.0: https://www.gnu.org/licenses/gpl-3.0.txt
# pylint: disable=undefined-variable

if "trackers_integration.openproject.Integration" not in EXTERNAL_BUG_TRACKERS:   # noqa: F821
    EXTERNAL_BUG_TRACKERS.append("trackers_integration.openproject.Integration")  # noqa: F821
