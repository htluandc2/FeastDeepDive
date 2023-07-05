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

from features import *

features_group_v1 = FeatureService(
    name="features_group_v1",
    features=[
        credit_history_features,
        zipcode_features
    ]
)

features_group_v2 = FeatureService(
    name="feature_group_v2",
    features=[
        credit_history_features,
        zipcode_features,
        transform_new_feature
    ],
)

features_group_v3 = FeatureService(
    name="feature_group_v3",
    features=[
        credit_history_features,
        zipcode_features,
        transform_new_feature,
        transform_sum_of_due
    ],
)


