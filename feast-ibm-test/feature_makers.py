from datetime import timedelta
from feast import (
    Entity, Feature,
    FeatureService, FeatureView,
    FileSource, ValueType, Field
)
from feast.on_demand_feature_view import on_demand_feature_view
import feast.types
import os 
import pandas as pd 

from feast_ibm_db2.db2_fs_source import Db2ServerSource

common_tags= {
    "owner": "luanht1",
    "team": "ops"
}


loan_entity = Entity(
    name="loan_entity",
    join_keys=["loan_id"] # Must to lower cases in this version
)

loan_source = Db2ServerSource(
    name="loan_source",
    table_ref="loan",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp",
)

loan_fv = FeatureView(
    name="loan_fv",
    entities=[loan_entity],
    source=loan_source,
    ttl=timedelta(days=36500),
    schema=[
        Field(
            name="person_home_ownership",
            dtype=feast.types.String,
            description="City to which",
        ),
        Field(
            name="person_age",
            dtype=feast.types.Int32,
            description="City to which",
        ),
    ],
    online=True,
    tags=common_tags
)



feature_group_v1 = FeatureService(
    name='feature_group_v1',
    features=[
        loan_fv
    ]
)