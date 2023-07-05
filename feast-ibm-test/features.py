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

from entities import *
from data_sources import *

zipcode_features = FeatureView(
    name="zipcode_features",
    entities=[zipcode],
    ttl=timedelta(days=36500),
    schema=[
        Field(name="city", dtype=feast.types.String, description="abc"),
        Field(name="state", dtype=feast.types.String, description="state"),
        Field(name="location_type", dtype=feast.types.String),
        Field(name="tax_returns_filed", dtype=feast.types.Int64),
        Field(name="population", dtype=feast.types.Int64),
        Field(name="total_wages", dtype=feast.types.Int64)
    ],
    online=True,
    source=zipcode_source,
    tags={
        "owner": "luanht1",
        "team": "Ops"
    }
)

credit_history_features = FeatureView(
    name="credit_history",
    entities=[dob_ssn],
    ttl=timedelta(days=36500),
    schema=[
        Field(name="credit_card_due", dtype=feast.types.Int64),
        Field(name="mortgage_due", dtype=feast.types.Int64),
        Field(name="student_loan_due", dtype=feast.types.Int64),
        Field(name="vehicle_loan_due", dtype=feast.types.Int64),
        Field(name="hard_pulls", dtype=feast.types.Int64),
        Field(name="missed_payments_2y", dtype=feast.types.Int64),
        Field(name="missed_payments_1y", dtype=feast.types.Int64),
        Field(name="missed_payments_6m", dtype=feast.types.Int64),
        Field(name="bankruptcies", dtype=feast.types.Int64)
    ],
    online=True,
    source=credit_history_source,
    tags={
        "owner": "luanht1",
        "team": "Ops"
    }
)

@on_demand_feature_view(
    sources=[credit_history_features],
    description="Example: make new features",
    tags={},
    schema=[Field(name='new_feature', dtype=feast.types.Int64)])
def transform_new_feature(inputs: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df['new_feature'] = inputs["missed_payments_2y"] + 10
    return df

@on_demand_feature_view(
    sources=[credit_history_features],
    description="Example: sum of due",
    tags={},
    schema=[Field(name='sum_of_due', dtype=feast.types.Int64)])
def transform_sum_of_due(inputs: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame()
    df['sum_of_due'] = inputs['student_loan_due'] + inputs['vehicle_loan_due'] + \
        inputs['mortgage_due'] + inputs['credit_card_due']
    return df


