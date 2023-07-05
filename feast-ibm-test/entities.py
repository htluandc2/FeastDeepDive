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

zipcode = Entity(
    name="zipcode",
    join_keys=["zipcode"]
)

dob_ssn = Entity(
    name="dob_ssn",
    join_keys=["dob_ssn"],
    description="Date of birth and last four digits of social security number..."
)

