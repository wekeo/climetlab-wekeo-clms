#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations

from climetlab.decorators import normalize

from climetlab_wekeo_clms.main import Main


class cgls_hourly_lst_global_v2(Main):
    name = "EO:CLMS:DAT:CGLS_HOURLY_LST_GLOBAL_V2"
    dataset = "EO:CLMS:DAT:CGLS_HOURLY_LST_GLOBAL_V2"

    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    def __init__(
        self,
        start="2021-01-18T00:00:00Z",
        end="2023-07-17T00:00:00Z",
    ):
        super().__init__(
            start=start,
            end=end,
        )
