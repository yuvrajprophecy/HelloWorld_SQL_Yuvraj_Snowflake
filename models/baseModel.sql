{{
  config({    
    "materialized": "table",
    "schema":  var('config1') 
  })
}}

WITH raw_payments AS (

  SELECT * 
  
  FROM {{ ref('raw_payments')}}

)

SELECT *

FROM raw_payments
