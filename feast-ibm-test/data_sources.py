from datetime import timedelta
from feast import (
    Entity, Feature,
    FeatureService, FeatureView,
    FileSource, ValueType, Field
)
import feast.types
import os

from feast.on_demand_feature_view import on_demand_feature_view
import feast.types
import os
import pandas as pd

from feast_ibm_db2.db2_fs_source import Db2ServerSource

zipcode_source = Db2ServerSource(
    name="zipcode_source",
    table_ref="zipcode",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

credit_history_source = Db2ServerSource(
    name="credit_history_source",
    table_ref="credit_history",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

