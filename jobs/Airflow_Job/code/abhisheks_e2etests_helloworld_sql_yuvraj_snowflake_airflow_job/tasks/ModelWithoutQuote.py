from abhisheks_e2etests_helloworld_sql_yuvraj_snowflake_airflow_job.utils import *

def ModelWithoutQuote():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "ModelWithoutQuote",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": True,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "model",
          "entity_kind": "model",
          "entity_name": "baseModel",
          "project_id": "53023",
          "git_entity": "branch",
          "git_entity_value": "dev",
          "git_ssh_url": "https://github.com/yuvrajprophecy/HelloWorld_SQL_Yuvraj_Snowflake",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile_snowflake --vars {\"config1\":\"TestingModelWithoutQuote_{{var.value.config2}}\"}",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"}
        },
    )
