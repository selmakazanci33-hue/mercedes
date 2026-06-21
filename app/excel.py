runner name: run_intelligence_pipeline
2026-06-20 22:49:46,978 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — runner name: run_intelligence_pipeline
server present: True
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — server present: True
database present: True
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — database present: True
username present: True
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — username present: True
driver: ODBC Driver 17 for SQL Server
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — driver: ODBC Driver 17 for SQL Server
authentication mode: ActiveDirectoryInteractive
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — authentication mode: ActiveDirectoryInteractive
connection timeout: 300 seconds
2026-06-20 22:49:46,979 | INFO     | azure_reconciliation.azure_client | Azure connection diagnostic — connection timeout: 300 seconds
2026-06-20 22:49:46,990 | INFO     | azure_reconciliation.azure_client | Azure connection mode: ActiveDirectoryInteractive
2026-06-20 22:49:46,990 | INFO     | azure_reconciliation.azure_client | Azure connection timeout: 300 seconds (complete browser sign-in within this window)
CONNECTING TO AZURE
2026-06-20 22:49:46,990 | INFO     | azure_reconciliation.azure_client | CONNECTING TO AZURE
2026-06-20 22:49:59,969 | INFO     | azure_reconciliation.azure_client | Azure connection successful
Azure connection successful
2026-06-20 22:50:00,149 | INFO     | azure_reconciliation.discovery_engine | Candidate Azure tables for evaluation: 95
2026-06-20 22:50:00,149 | INFO     | azure_reconciliation.azure_mirror.discovery.xml_reference | No XML summary assets for issuer 13535
2026-06-20 22:50:00,313 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:50:01,375 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 21
2026-06-20 22:50:01,513 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=11
2026-06-20 22:50:01,526 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:01,533 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01               701            1027      1027
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02               701            1027      1027
st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01               701            1027      1027
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02               701            1027      1027
2026-06-20 22:50:01,565 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:01,568 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10               701            1027      1027
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11               701            1027      1027
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    12               701            1027      1027
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01               701            1027      1027
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02               701            1027      1027
st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10               701            1027      1027
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11               701            1027      1027
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    12               701            1027      1027
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01               701            1027      1027
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02               701            1027      1027
2026-06-20 22:50:01,604 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:01,607 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10               701            1027      1027
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10               701            1027      1027
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
2026-06-20 22:50:01,790 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_01312026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:50:18,723 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:50:19,514 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=31
2026-06-20 22:50:19,523 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:19,526 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10               786            1165      1165
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11               794            1181      1183
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    12               776            1144      1144
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              1078            1465      1465
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              1536            2088      2089
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10               786            1165      1165
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11               794            1181      1183
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    12               776            1144      1144
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              1078            1465      1465
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              1536            2088      2089
2026-06-20 22:50:19,553 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:19,555 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              3405            4067      4740
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              3405            4067      4740
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    12              3405            4067      4740
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              3405            4067      4740
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              3405            4067      4740
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              3405            4067      4740
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              3405            4067      4740
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    12              3405            4067      4740
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              3405            4067      4740
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              3405            4067      4740
2026-06-20 22:50:19,584 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:19,586 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10               550             762       764
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11               426             598       600
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    12              1116            1562      1568
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01               792            1068      1072
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02                55              91        91
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10               550             762       764
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11               426             598       600
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    12              1116            1562      1568
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01               792            1068      1072
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02                55              91        91
2026-06-20 22:50:19,767 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_02272026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:50:50,015 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:50:50,726 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=32
2026-06-20 22:50:50,738 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:50,741 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10               784            1163      1163
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11               792            1179      1181
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    12               774            1142      1142
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01               757            1068      1068
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              1170            1622      1622
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10               784            1163      1163
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11               792            1179      1181
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    12               774            1142      1142
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01               757            1068      1068
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              1170            1622      1622
2026-06-20 22:50:50,769 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:50,771 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              3072            3706      4313
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              3072            3706      4313
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    12              3072            3706      4313
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              3072            3706      4313
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              3072            3706      4313
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              3072            3706      4313
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              3072            3706      4313
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    12              3072            3706      4313
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              3072            3706      4313
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              3072            3706      4313
2026-06-20 22:50:50,802 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:50:50,804 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10               460             661       663
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11               346             505       507
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    12               954            1344      1350
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01               756            1012      1015
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02                90             133       133
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10               460             661       663
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11               346             505       507
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    12               954            1344      1350
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01               756            1012      1015
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02                90             133       133
2026-06-20 22:50:50,990 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_03312026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:51:29,955 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:51:30,766 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=34
2026-06-20 22:51:30,780 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:51:30,784 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    12               747            1106      1106
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              1250            1776      1782
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              1105            1536      1538
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    12               747            1106      1106
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              1250            1776      1782
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              1105            1536      1538
2026-06-20 22:51:30,814 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:51:30,816 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              3620            4480      5114
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              3620            4480      5114
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    12              3620            4480      5114
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              3620            4480      5114
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              3620            4480      5114
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              3620            4480      5114
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              3620            4480      5114
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    12              3620            4480      5114
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              3620            4480      5114
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              3620            4480      5114
2026-06-20 22:51:30,849 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:51:30,852 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10               678            1001      1003
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11               447             631       637
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    12              1131            1587      1600
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01               752            1017      1022
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02                94             140       140
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10               678            1001      1003
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11               447             631       637
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    12              1131            1587      1600
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01               752            1017      1022
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02                94             140       140
2026-06-20 22:51:31,055 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_04302026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:52:11,529 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:52:12,296 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=33
2026-06-20 22:52:12,307 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:12,309 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    12               746            1105      1105
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              1249            1773      1779
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              1106            1537      1539
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    12               746            1105      1105
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              1249            1773      1779
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              1106            1537      1539
2026-06-20 22:52:12,343 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:12,346 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              3656            4539      5165
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              3656            4539      5165
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    12              3656            4539      5165
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              3656            4539      5165
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              3656            4539      5165
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              3656            4539      5165
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              3656            4539      5165
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    12              3656            4539      5165
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              3656            4539      5165
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              3656            4539      5165
2026-06-20 22:52:12,377 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:12,379 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10               676             997       999
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11               446             631       637
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    12              1130            1584      1597
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01               755            1024      1029
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02                92             135       135
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10               676             997       999
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11               446             631       637
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    12              1130            1584      1597
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01               755            1024      1029
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02                92             135       135
2026-06-20 22:52:12,568 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_FEB10 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:52:43,113 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:52:43,946 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=32
2026-06-20 22:52:43,957 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:43,959 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10               786            1165      1165
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11               794            1181      1183
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12               776            1144      1144
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              1037            1425      1425
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              1472            2011      2011
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10               786            1165      1165
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11               794            1181      1183
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12               776            1144      1144
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              1037            1425      1425
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              1472            2011      2011
2026-06-20 22:52:43,989 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:43,991 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              3350            4011      4671
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              3350            4011      4671
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12              3350            4011      4671
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              3350            4011      4671
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              3350            4011      4671
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              3350            4011      4671
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              3350            4011      4671
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12              3350            4011      4671
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              3350            4011      4671
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              3350            4011      4671
2026-06-20 22:52:44,022 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:52:44,025 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10               527             741       743
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11               421             592       594
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    12              1095            1537      1543
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01               776            1042      1045
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02                65             101       101
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10               527             741       743
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11               421             592       594
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    12              1095            1537      1543
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01               776            1042      1045
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02                65             101       101
2026-06-20 22:52:44,225 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC31 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 22:53:19,564 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 22:53:20,315 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=31
2026-06-20 22:53:20,325 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:20,327 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10               793            1174      1174
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11               801            1190      1192
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12               784            1154      1154
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              1324            1854      1857
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              1247            1706      1706
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10               793            1174      1174
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11               801            1190      1192
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12               784            1154      1154
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              1324            1854      1857
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              1247            1706      1706
2026-06-20 22:53:20,360 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:20,362 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              3295            3934      4650
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              3295            3934      4650
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12              3295            3934      4650
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              3295            3934      4650
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              3295            3934      4650
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              3295            3934      4650
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              3295            3934      4650
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12              3295            3934      4650
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              3295            3934      4650
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              3295            3934      4650
2026-06-20 22:53:20,387 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:20,390 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10               706            1022      1024
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11               466             652       658
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    12              1168            1641      1645
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               434             584       587
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02                55              91        91
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10               706            1022      1024
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11               466             652       658
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    12              1168            1641      1645
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               434             584       587
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02                55              91        91
2026-06-20 22:53:20,597 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.DuplicateEnrollment_Overlap — cols=121 issuer=None year=None status=None action=None
2026-06-20 22:53:20,779 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_test — cols=80 issuer=GAA_HIOS_ID year=Coverage_Year status=enrolleeStatus action=actionCode
2026-06-20 22:53:22,357 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2025/10.
2026-06-20 22:53:22,389 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2025/11.
2026-06-20 22:53:22,411 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2025/12.
2026-06-20 22:53:22,433 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/01.
2026-06-20 22:53:22,459 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/02.
2026-06-20 22:53:22,485 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/03.
2026-06-20 22:53:22,511 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/04.
2026-06-20 22:53:22,536 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/05.
2026-06-20 22:53:22,557 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 1804 row(s) in 2026/06.
2026-06-20 22:53:22,576 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 25
2026-06-20 22:53:23,066 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=GAA_834_File_Date rows=25
2026-06-20 22:53:23,135 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,138 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    10              1316            1772      1844
1           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    11              1294            1750      1822
2           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    12              1287            1744      1815
3           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    01              1789            2241      2325
4           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    02              1499            1955      2032
st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    10              1316            1772      1844
1           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    11              1294            1750      1822
2           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    12              1287            1744      1815
3           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    01              1789            2241      2325
4           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    02              1499            1955      2032
2026-06-20 22:53:23,168 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,171 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    10              2251            2668      2795
1           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    11              2251            2668      2795
2           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    12              2251            2668      2795
3           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    01              2251            2668      2795
4           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    02              2251            2668      2795
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    10              2251            2668      2795
1           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    11              2251            2668      2795
2           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    12              2251            2668      2795
3           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    01              2251            2668      2795
4           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    02              2251            2668      2795
2026-06-20 22:53:23,199 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,201 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_test  2025    10                76              87        93
1           C  Event Date Logic  dbo.834_Inbound_test  2025    11                70              79        80
2           C  Event Date Logic  dbo.834_Inbound_test  2025    12               182             232       233
3           C  Event Date Logic  dbo.834_Inbound_test  2026    01               815            1155      1164
4           C  Event Date Logic  dbo.834_Inbound_test  2026    02               564             632       640
st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_test  2025    10                76              87        93
1           C  Event Date Logic  dbo.834_Inbound_test  2025    11                70              79        80
2           C  Event Date Logic  dbo.834_Inbound_test  2025    12               182             232       233
3           C  Event Date Logic  dbo.834_Inbound_test  2026    01               815            1155      1164
4           C  Event Date Logic  dbo.834_Inbound_test  2026    02               564             632       640
2026-06-20 22:53:23,228 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml D/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,231 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id      strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_test  2025    10               596             831       837
1           D  834 Inbound Logic  dbo.834_Inbound_test  2025    11               163             204       207
2           D  834 Inbound Logic  dbo.834_Inbound_test  2025    12               360             476       483
3           D  834 Inbound Logic  dbo.834_Inbound_test  2026    01               242             330       333
4           D  834 Inbound Logic  dbo.834_Inbound_test  2026    02               409             411       422
st_month head:
  strategy_id      strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_test  2025    10               596             831       837
1           D  834 Inbound Logic  dbo.834_Inbound_test  2025    11               163             204       207
2           D  834 Inbound Logic  dbo.834_Inbound_test  2025    12               360             476       483
3           D  834 Inbound Logic  dbo.834_Inbound_test  2026    01               242             330       333
4           D  834 Inbound Logic  dbo.834_Inbound_test  2026    02               409             411       422
2026-06-20 22:53:23,423 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_header_test — cols=23 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 22:53:23,878 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=GAA_834_File_Date rows=9
2026-06-20 22:53:23,912 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,914 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    10                 0               0       334
1           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    11                 0               0       334
2           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    12                 0               0       334
3           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    01                 0               0       334
4           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    02                 0               0       334
st_month head:
  strategy_id               strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    10                 0               0       334
1           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    11                 0               0       334
2           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    12                 0               0       334
3           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    01                 0               0       334
4           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    02                 0               0       334
2026-06-20 22:53:23,939 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,942 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_header_test  2025    10                 0               0        36
1           C  Event Date Logic  dbo.834_Inbound_header_test  2025    11                 0               0        32
2           C  Event Date Logic  dbo.834_Inbound_header_test  2025    12                 0               0        56
3           C  Event Date Logic  dbo.834_Inbound_header_test  2026    01                 0               0        60
4           C  Event Date Logic  dbo.834_Inbound_header_test  2026    02                 0               0        46
st_month head:
  strategy_id     strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_header_test  2025    10                 0               0        36
1           C  Event Date Logic  dbo.834_Inbound_header_test  2025    11                 0               0        32
2           C  Event Date Logic  dbo.834_Inbound_header_test  2025    12                 0               0        56
3           C  Event Date Logic  dbo.834_Inbound_header_test  2026    01                 0               0        60
4           C  Event Date Logic  dbo.834_Inbound_header_test  2026    02                 0               0        46
2026-06-20 22:53:23,972 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml D/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:53:23,974 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id      strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    10                 0               0        36
1           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    11                 0               0        32
2           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    12                 0               0        56
3           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    01                 0               0        60
4           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    02                 0               0        46
st_month head:
  strategy_id      strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    10                 0               0        36
1           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    11                 0               0        32
2           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    12                 0               0        56
3           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    01                 0               0        60
4           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    02                 0               0        46
2026-06-20 22:53:24,169 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 22:57:51,613 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:57:51,615 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
2026-06-20 22:57:51,810 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2026 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 22:58:32,951 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:58:32,954 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      8000
st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      8000
2026-06-20 22:58:33,150 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 22:59:30,831 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:59:30,833 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              1070            1585      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              1070            1585      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    12              1070            1585      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              1070            1585      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              1070            1585      8000
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              1070            1585      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              1070            1585      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    12              1070            1585      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              1070            1585      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              1070            1585      8000
2026-06-20 22:59:30,861 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 22:59:30,864 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10               819            1204      1204
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01               509             756       777
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02               812            1181      1252
st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10               819            1204      1204
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01               509             756       777
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02               812            1181      1252
2026-06-20 22:59:31,057 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_test — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:00:33,479 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:00:33,481 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10              1830            2641      9020
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11              1830            2641      9020
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    12              1830            2641      9020
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01              1830            2641      9020
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02              1830            2641      9020
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10              1830            2641      9020
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11              1830            2641      9020
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    12              1830            2641      9020
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01              1830            2641      9020
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02              1830            2641      9020
2026-06-20 23:00:33,509 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:00:33,512 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10               846            1245      1313
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11               822            1217      1261
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    12               792            1167      1167
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              1242            1773      1805
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02               814            1186      1259
st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10               846            1245      1313
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11               822            1217      1261
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    12               792            1167      1167
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              1242            1773      1805
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02               814            1186      1259
2026-06-20 23:00:33,700 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.AT_external_applications — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:00:33,872 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:00:38,112 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408_02 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:00:40,352 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_TXT_TEST1 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:00:46,392 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_All_test — cols=41 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:00:46,882 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Consolidated_Full_list — cols=40 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:00:47,478 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 9
2026-06-20 23:00:47,533 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=9
2026-06-20 23:00:47,543 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:00:47,546 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10                 2               2         4
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11                 2               2         4
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    12                 2               2         4
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01                 2               2         4
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02                 2               2         4
st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10                 2               2         4
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11                 2               2         4
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    12                 2               2         4
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01                 2               2         4
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02                 2               2         4
2026-06-20 23:00:47,571 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:00:47,573 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10                 4               2         8
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11                 4               2         8
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    12                 4               2         8
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01                 4               2         8
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02                 4               2         8
st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10                 4               2         8
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11                 4               2         8
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    12                 4               2         8
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01                 4               2         8
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02                 4               2         8
2026-06-20 23:00:47,596 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:00:47,598 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10                 2               2         4
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Consolidated_Full_list  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                 1               1         2
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10                 2               2         4
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Consolidated_Full_list  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                 1               1         2
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                 0               0         0
2026-06-20 23:00:47,784 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Demographics_Premium — cols=25 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:00:47,952 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollee_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:00:48,118 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollment_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:00:48,302 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_AETNA — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:00:50,764 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_Agent — cols=12 issuer=None year=None status=enrollment_status_description action=None
2026-06-20 23:00:50,929 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2025 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:00:51,426 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC17 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:01:29,561 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 27
2026-06-20 23:01:29,759 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=16
2026-06-20 23:01:29,769 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:01:29,771 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              1321            1860      1909
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              1167            1606      1648
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              1321            1860      1909
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              1167            1606      1648
2026-06-20 23:01:29,797 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:01:29,799 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              1326            1870      1921
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              1326            1870      1921
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12              1326            1870      1921
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              1326            1870      1921
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              1326            1870      1921
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              1326            1870      1921
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              1326            1870      1921
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12              1326            1870      1921
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              1326            1870      1921
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              1326            1870      1921
2026-06-20 23:01:29,824 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:01:29,826 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10               676             976       998
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               224             286       295
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    12               433             610       628
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10               676             976       998
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               224             286       295
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    12               433             610       628
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02                 0               0         0
2026-06-20 23:01:30,017 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC22 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:02:12,663 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:02:13,137 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=30
2026-06-20 23:02:13,147 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:13,149 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10               813            1202      1205
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11               823            1220      1225
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12               814            1195      1200
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              1323            1854      1856
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              1190            1632      1632
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10               813            1202      1205
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11               823            1220      1225
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12               814            1195      1200
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              1323            1854      1856
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              1190            1632      1632
2026-06-20 23:02:13,174 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:13,177 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              3226            3816      4558
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              3226            3816      4558
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12              3226            3816      4558
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              3226            3816      4558
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              3226            3816      4558
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              3226            3816      4558
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              3226            3816      4558
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12              3226            3816      4558
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              3226            3816      4558
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              3226            3816      4558
2026-06-20 23:02:13,207 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:13,210 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10               715            1025      1027
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11               469             644       651
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    12              1094            1540      1542
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                55              91        91
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10               715            1025      1027
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11               469             644       651
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    12              1094            1540      1542
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                55              91        91
2026-06-20 23:02:13,400 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV21 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:02:49,950 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 30
2026-06-20 23:02:50,373 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=33
2026-06-20 23:02:50,384 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:50,386 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10               859            1265      1268
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11               869            1284      1289
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12               877            1286      1291
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01               855            1230      1230
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02               813            1164      1164
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10               859            1265      1268
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11               869            1284      1289
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12               877            1286      1291
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01               855            1230      1230
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02               813            1164      1164
2026-06-20 23:02:50,410 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:50,412 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              2723            2944      3879
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              2723            2944      3879
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              2723            2944      3879
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              2723            2944      3879
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              2723            2944      3879
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              2723            2944      3879
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              2723            2944      3879
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              2723            2944      3879
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              2723            2944      3879
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              2723            2944      3879
2026-06-20 23:02:50,438 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:02:50,440 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10               719            1057      1060
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11               419             586       593
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    12               630             887       888
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02                55              91        91
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10               719            1057      1060
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11               419             586       593
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    12               630             887       888
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02                55              91        91
2026-06-20 23:02:50,625 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV30 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:03:32,636 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 30
2026-06-20 23:03:33,015 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=34
2026-06-20 23:03:33,025 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:03:33,027 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10               859            1265      1268
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11               869            1284      1289
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12               875            1279      1284
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01               901            1281      1281
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02               844            1183      1183
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10               859            1265      1268
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11               869            1284      1289
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12               875            1279      1284
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01               901            1281      1281
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02               844            1183      1183
2026-06-20 23:03:33,057 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:03:33,059 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              2771            3033      3932
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              2771            3033      3932
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              2771            3033      3932
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              2771            3033      3932
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              2771            3033      3932
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              2771            3033      3932
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              2771            3033      3932
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              2771            3033      3932
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              2771            3033      3932
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              2771            3033      3932
2026-06-20 23:03:33,088 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:03:33,091 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10               717            1047      1050
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11               469             649       656
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    12               630             887       888
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02                55              91        91
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10               717            1047      1050
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11               469             649       656
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    12               630             887       888
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               435             582       585
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02                55              91        91
2026-06-20 23:03:33,288 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_TEST — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:04:21,590 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:04:22,338 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=34
2026-06-20 23:04:22,349 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:22,351 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    12               746            1105      1105
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              1256            1781      1787
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              1113            1539      1541
st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10               778            1154      1154
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11               765            1143      1145
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    12               746            1105      1105
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              1256            1781      1787
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              1113            1539      1541
2026-06-20 23:04:22,380 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:22,383 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10              3713            4627      5245
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11              3713            4627      5245
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    12              3713            4627      5245
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01              3713            4627      5245
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02              3713            4627      5245
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10              3713            4627      5245
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11              3713            4627      5245
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    12              3713            4627      5245
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01              3713            4627      5245
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02              3713            4627      5245
2026-06-20 23:04:22,411 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:22,413 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10               681            1002      1004
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11               448             633       639
2           C  Event Date Logic  dbo.Enrollments_TEST  2025    12              1132            1587      1599
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    01               763            1029      1034
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    02                93             136       136
st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10               681            1002      1004
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11               448             633       639
2           C  Event Date Logic  dbo.Enrollments_TEST  2025    12              1132            1587      1599
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    01               763            1029      1034
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    02                93             136       136
2026-06-20 23:04:22,604 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:04:23,799 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Dental_ALL — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:23,801 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    10               791            1162      1162
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    11               791            1162      1162
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    12               791            1162      1162
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    01               791            1162      1162
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    02               791            1162      1162
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    10               791            1162      1162
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    11               791            1162      1162
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    12               791            1162      1162
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    01               791            1162      1162
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    02               791            1162      1162
2026-06-20 23:04:23,979 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:04:25,273 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Dental_ALL_2 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:25,276 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    10               791            1163      1163
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    11               791            1163      1163
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    12               791            1163      1163
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    01               791            1163      1163
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    02               791            1163      1163
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    10               791            1163      1163
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    11               791            1163      1163
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    12               791            1163      1163
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    01               791            1163      1163
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    02               791            1163      1163
2026-06-20 23:04:25,458 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:04:32,087 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:04:39,760 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_PY2025_PY2026 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:04:46,946 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_PY2025_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:46,948 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10              1624            1215      2419
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11              1624            1215      2419
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    12              1624            1215      2419
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01              1624            1215      2419
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02              1624            1215      2419
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10              1624            1215      2419
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11              1624            1215      2419
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    12              1624            1215      2419
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01              1624            1215      2419
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02              1624            1215      2419
2026-06-20 23:04:47,129 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GA_DEMOGRAPHICS — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:04:47,293 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:04:47,455 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound_test — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:04:47,617 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:04:47,773 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound_test — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:04:47,946 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:04:48,107 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:04:48,266 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:04:48,426 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound_test — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:04:48,591 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.HH_SSAP_AT2026 — cols=22 issuer=None year=coverage_year status=None action=None
2026-06-20 23:04:48,753 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Issuers_list_test — cols=2 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:04:49,125 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Issuers_list_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:49,128 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    12                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    12                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
2026-06-20 23:04:49,309 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Jan2025_Invoice — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:04:51,196 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2024_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:04:51,353 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:04:51,510 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:04:51,678 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:04:54,889 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 13
2026-06-20 23:04:54,959 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=10
2026-06-20 23:04:54,968 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:54,970 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10                 4               5         5
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11                 5               6         6
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    12                 4               5         5
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10                 4               5         5
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11                 5               6         6
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    12                 4               5         5
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
2026-06-20 23:04:54,990 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:54,993 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10                12              17        17
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11                12              17        17
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    12                12              17        17
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01                12              17        17
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02                12              17        17
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10                12              17        17
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11                12              17        17
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    12                12              17        17
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01                12              17        17
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02                12              17        17
2026-06-20 23:04:55,016 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:04:55,019 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11                 1               3         3
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    12                 4               6         6
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01                 2               3         3
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                 1               1         1
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11                 1               3         3
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    12                 4               6         6
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01                 2               3         3
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                 1               1         1
2026-06-20 23:04:55,203 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:05:05,150 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 18
2026-06-20 23:05:05,283 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=28
2026-06-20 23:05:05,293 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:05,295 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10               189             286       294
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11               193             291       300
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    12               181             273       281
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10               189             286       294
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11               193             291       300
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    12               181             273       281
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
2026-06-20 23:05:05,321 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:05,323 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10               473             624       678
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11               473             624       678
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    12               473             624       678
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01               473             624       678
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02               473             624       678
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10               473             624       678
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11               473             624       678
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    12               473             624       678
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01               473             624       678
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02               473             624       678
2026-06-20 23:05:05,351 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:05,354 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10                25              39        41
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11                66              94       100
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    12               103             159       164
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01                74             100       105
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02                29              35        35
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10                25              39        41
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11                66              94       100
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    12               103             159       164
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01                74             100       105
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02                29              35        35
2026-06-20 23:05:05,536 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:05:05,696 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026Applicants_with_tobacco_usage — cols=11 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:05,855 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:06,019 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:05:08,604 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 16
2026-06-20 23:05:08,672 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=13
2026-06-20 23:05:08,682 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:08,684 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01                 8              13        13
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02                 8              10        10
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01                 8              13        13
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02                 8              10        10
2026-06-20 23:05:08,705 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:08,707 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10                12              18        18
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11                12              18        18
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    12                12              18        18
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01                12              18        18
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02                12              18        18
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10                12              18        18
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11                12              18        18
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    12                12              18        18
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01                12              18        18
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02                12              18        18
2026-06-20 23:05:08,730 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:08,732 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10                 1               2         2
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                 2               2         2
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02                 2               3         3
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10                 1               2         2
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                 2               2         2
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02                 2               3         3
2026-06-20 23:05:08,927 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:05:18,731 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 26
2026-06-20 23:05:18,848 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=22
2026-06-20 23:05:18,859 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:18,861 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01               241             338       349
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02               169             239       246
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01               241             338       349
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02               169             239       246
2026-06-20 23:05:18,893 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:18,896 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10               359             506       521
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11               359             506       521
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    12               359             506       521
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01               359             506       521
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02               359             506       521
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10               359             506       521
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11               359             506       521
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    12               359             506       521
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01               359             506       521
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02               359             506       521
2026-06-20 23:05:18,921 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:05:18,923 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10                 1               2         4
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11                25              41        41
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    12                84             117       122
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01                93             131       133
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02                49              75        75
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10                 1               2         4
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11                25              41        41
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    12                84             117       122
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01                93             131       133
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02                49              75        75
2026-06-20 23:05:19,105 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Reinsurance_APR_PY2026 — cols=29 issuer=None year=None status=enrollee_status_description action=None
2026-06-20 23:05:19,273 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:05:19,431 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test_pp — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:05:19,591 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:05:19,754 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test_pp — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:05:19,910 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:05:20,069 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test_pp — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:05:20,228 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_current_and_old_rate — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:05:20,391 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:05:20,560 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income — cols=11 issuer=None year=None status=None action=None
2026-06-20 23:05:20,723 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:05:20,885 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new2 — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:05:21,050 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_income — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:05:21,209 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:05:21,368 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium_new — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:05:21,542 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:05:21,705 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL_NEW — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:05:21,872 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:05:22,037 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_1 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:05:22,202 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_2 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:05:22,367 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GW — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:05:22,539 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_RESULTS — cols=49 issuer=None year=None status=None action=None
2026-06-20 23:05:22,705 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_enrollments_cms — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:05:22,873 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_brokers — cols=19 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,049 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,207 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,373 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,535 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,696 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:05:23,860 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2025 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:09:58,540 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_PY2025 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:09:58,542 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    02                 0               0      8000
st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    02                 0               0      8000
2026-06-20 23:09:58,727 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority — cols=3 issuer=None year=None status=None action=None
2026-06-20 23:09:58,890 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority_test — cols=6 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:09:59,396 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_priority_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:09:59,398 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    10                 0               0      4032
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    11                 0               0      4032
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    12                 0               0      4032
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    01                 0               0      4032
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    02                 0               0      4032
st_month head:
  strategy_id               strategy_name                           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    10                 0               0      4032
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    11                 0               0      4032
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    12                 0               0      4032
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    01                 0               0      4032
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    02                 0               0      4032
2026-06-20 23:09:59,571 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority_test1 — cols=7 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:10:00,003 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_priority_test1 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:00,005 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    10                 0               0      2016
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    11                 0               0      2016
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    12                 0               0      2016
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    01                 0               0      2016
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    02                 0               0      2016
st_month head:
  strategy_id               strategy_name                            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    10                 0               0      2016
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    11                 0               0      2016
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    12                 0               0      2016
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    01                 0               0      2016
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    02                 0               0      2016
2026-06-20 23:10:00,189 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_test — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:10:35,361 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:35,364 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    10                 0               0      5587
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    11                 0               0      5587
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    12                 0               0      5587
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    01                 0               0      5587
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    02                 0               0      5587
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    10                 0               0      5587
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    11                 0               0      5587
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    12                 0               0      5587
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    01                 0               0      5587
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    02                 0               0      5587
2026-06-20 23:10:35,534 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.premium_change — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:10:35,696 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.sysdiagrams — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:10:35,887 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.test_834_in — cols=49 issuer=None year=None status=None action=None
2026-06-20 23:10:35,889 | INFO     | azure_reconciliation.discovery_engine | Selected Azure table=dbo.Enrollments_TEST strategy=A score=70.2 rows=5245 (evaluated 95 tables, 72 strategies)
2026-06-20 23:10:36,254 | INFO     | azure_reconciliation.discovery_engine | Candidate Azure tables for evaluation: 95
2026-06-20 23:10:36,255 | INFO     | azure_reconciliation.azure_mirror.discovery.xml_reference | No XML summary assets for issuer 15105
2026-06-20 23:10:36,423 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:10:49,009 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 14
2026-06-20 23:10:49,431 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=9
2026-06-20 23:10:49,442 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:49,445 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01              6284            8000      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02              6284            8000      8000
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    03              6284            8000      8000
st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01              6284            8000      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02              6284            8000      8000
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    03              6284            8000      8000
2026-06-20 23:10:49,473 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:49,476 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10              6284            8000      8000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11              6284            8000      8000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01              6284            8000      8000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02              6284            8000      8000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    03              6284            8000      8000
st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10              6284            8000      8000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11              6284            8000      8000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01              6284            8000      8000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02              6284            8000      8000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    03              6284            8000      8000
2026-06-20 23:10:49,503 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:49,506 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10              6284            8000      8000
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    03                 0               0         0
st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10              6284            8000      8000
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    03                 0               0         0
2026-06-20 23:10:49,698 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_01312026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:10:54,569 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 32
2026-06-20 23:10:55,860 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=25
2026-06-20 23:10:55,872 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:55,874 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              2741            3362      3366
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              2708            3320      3323
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              5335            7173      7173
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              5920            7988      8000
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    03              5814            7839      7839
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              2741            3362      3366
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              2708            3320      3323
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              5335            7173      7173
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              5920            7988      8000
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    03              5814            7839      7839
2026-06-20 23:10:55,909 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:55,912 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10             12276           15495     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11             12276           15495     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01             12276           15495     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02             12276           15495     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    03             12276           15495     16000
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10             12276           15495     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11             12276           15495     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01             12276           15495     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02             12276           15495     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    03             12276           15495     16000
2026-06-20 23:10:55,953 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:10:55,956 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10              8500           10698     10709
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11               452             759       759
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01              1162            1635      1636
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02               130             146       147
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    03               113             139       139
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10              8500           10698     10709
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11               452             759       759
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01              1162            1635      1636
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02               130             146       147
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    03               113             139       139
2026-06-20 23:10:56,146 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_02272026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:11:10,401 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 29
2026-06-20 23:11:11,845 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=24
2026-06-20 23:11:11,856 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:11,858 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              2740            3362      3366
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              2706            3319      3322
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              5739            6793      6793
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              6447            7669      7670
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    03              6386            7577      7580
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              2740            3362      3366
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              2706            3319      3322
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              5739            6793      6793
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              6447            7669      7670
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    03              6386            7577      7580
2026-06-20 23:11:11,892 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:11,894 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10             13072           13730     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11             13072           13730     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01             13072           13730     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02             13072           13730     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    03             13072           13730     16000
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10             13072           13730     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11             13072           13730     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01             13072           13730     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02             13072           13730     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    03             13072           13730     16000
2026-06-20 23:11:11,926 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:11,929 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10              8831            9206     10373
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11               604             933       935
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01              1244            1615      1626
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02               322             392       393
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    03               113             140       140
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10              8831            9206     10373
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11               604             933       935
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01              1244            1615      1626
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02               322             392       393
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    03               113             140       140
2026-06-20 23:11:12,128 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_03312026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:11:27,224 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 30
2026-06-20 23:11:28,732 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=24
2026-06-20 23:11:28,743 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:28,746 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              2881            3573      3579
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              2854            3542      3547
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              5523            6610      6708
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              4116            4856      4861
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    03              4046            4764      4767
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              2881            3573      3579
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              2854            3542      3547
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              5523            6610      6708
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              4116            4856      4861
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    03              4046            4764      4767
2026-06-20 23:11:28,783 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:28,786 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10             12844           13409     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11             12844           13409     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01             12844           13409     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02             12844           13409     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    03             12844           13409     16000
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10             12844           13409     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11             12844           13409     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01             12844           13409     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02             12844           13409     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    03             12844           13409     16000
2026-06-20 23:11:28,820 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:28,822 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10              8329            8831     10068
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11               613             930       935
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01              1180            1537      1545
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02               285             349       351
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    03               378             477       478
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10              8329            8831     10068
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11               613             930       935
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01              1180            1537      1545
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02               285             349       351
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    03               378             477       478
2026-06-20 23:11:29,121 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_04302026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:11:44,150 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 27
2026-06-20 23:11:45,636 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=24
2026-06-20 23:11:45,646 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:45,648 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              2886            3575      3581
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              2859            3544      3549
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              5399            6478      6576
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              2538            3175      3178
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    03              2539            3157      3162
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              2886            3575      3581
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              2859            3544      3549
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              5399            6478      6576
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              2538            3175      3178
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    03              2539            3157      3162
2026-06-20 23:11:45,680 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:45,682 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10             12821           14139     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11             12821           14139     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01             12821           14139     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02             12821           14139     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    03             12821           14139     16000
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10             12821           14139     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11             12821           14139     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01             12821           14139     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02             12821           14139     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    03             12821           14139     16000
2026-06-20 23:11:45,716 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:45,718 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10              8313            9329     10056
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11               588             903       908
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01              1101            1450      1457
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02               283             348       350
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    03               358             447       448
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10              8313            9329     10056
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11               588             903       908
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01              1101            1450      1457
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02               283             348       350
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    03               358             447       448
2026-06-20 23:11:45,920 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_FEB10 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:11:52,681 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 32
2026-06-20 23:11:54,135 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=25
2026-06-20 23:11:54,147 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:54,150 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              2743            3364      3368
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              2710            3322      3325
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              5922            7134      7134
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              6554            7930      7930
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    03              6543            7912      7912
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              2743            3364      3368
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              2710            3322      3325
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              5922            7134      7134
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              6554            7930      7930
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    03              6543            7912      7912
2026-06-20 23:11:54,187 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:54,189 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10             12975           15478     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11             12975           15478     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01             12975           15478     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02             12975           15478     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    03             12975           15478     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10             12975           15478     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11             12975           15478     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01             12975           15478     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02             12975           15478     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    03             12975           15478     16000
2026-06-20 23:11:54,227 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:11:54,230 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10              8902           10512     10534
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11               629             970       970
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01              1240            1657      1658
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02               207             246       247
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    03               112             138       138
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10              8902           10512     10534
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11               629             970       970
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01              1240            1657      1658
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02               207             246       247
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    03               112             138       138
2026-06-20 23:11:54,450 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC31 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:12:08,170 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 28
2026-06-20 23:12:09,534 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=25
2026-06-20 23:12:09,543 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:09,545 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              2739            3359      3363
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              2717            3329      3332
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              6160            7579      7701
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              4547            5514      5519
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    03              4522            5482      5482
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              2739            3359      3363
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              2717            3329      3332
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              6160            7579      7701
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              4547            5514      5519
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    03              4522            5482      5482
2026-06-20 23:12:09,579 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:09,582 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10             12755           13239     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11             12755           13239     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01             12755           13239     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02             12755           13239     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    03             12755           13239     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10             12755           13239     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11             12755           13239     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01             12755           13239     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02             12755           13239     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    03             12755           13239     16000
2026-06-20 23:12:09,621 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:09,623 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10              9077            9661     11091
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11               649             984       989
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               701             908       909
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02               130             146       147
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    03               113             139       139
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10              9077            9661     11091
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11               649             984       989
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               701             908       909
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02               130             146       147
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    03               113             139       139
2026-06-20 23:12:09,830 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.DuplicateEnrollment_Overlap — cols=121 issuer=None year=None status=None action=None
2026-06-20 23:12:10,010 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_test — cols=80 issuer=GAA_HIOS_ID year=Coverage_Year status=enrolleeStatus action=actionCode
2026-06-20 23:12:11,810 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2025/10.
2026-06-20 23:12:11,894 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2025/11.
2026-06-20 23:12:11,997 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/01.
2026-06-20 23:12:12,076 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/02.
2026-06-20 23:12:12,139 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/03.
2026-06-20 23:12:12,206 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/04.
2026-06-20 23:12:12,277 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/05.
2026-06-20 23:12:12,334 | WARNING  | azure_reconciliation.azure_mirror.query | Missing benefit dates; using coverage_year fallback for 8052 row(s) in 2026/06.
2026-06-20 23:12:12,390 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 18
2026-06-20 23:12:13,158 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=memberMaintEffectiveDate rows=22
2026-06-20 23:12:13,247 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:13,249 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    10              7205            8808      9366
1           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    11              7048            8623      9211
2           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    01              6764            8269      8666
3           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    02              6231            7725      8112
4           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    03              6174            7668      8055
st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    10              7205            8808      9366
1           A  Active Coverage Snapshot  dbo.834_Inbound_test  2025    11              7048            8623      9211
2           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    01              6764            8269      8666
3           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    02              6231            7725      8112
4           A  Active Coverage Snapshot  dbo.834_Inbound_test  2026    03              6174            7668      8055
2026-06-20 23:12:13,277 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:13,279 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    10              8718           10283     11065
1           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    11              8718           10283     11065
2           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    01              8718           10283     11065
3           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    02              8718           10283     11065
4           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    03              8718           10283     11065
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    10              8718           10283     11065
1           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2025    11              8718           10283     11065
2           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    01              8718           10283     11065
3           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    02              8718           10283     11065
4           B  Enrollment Status Snapshot  dbo.834_Inbound_test  2026    03              8718           10283     11065
2026-06-20 23:12:13,307 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:13,310 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_test  2025    10              4241            5144      5227
1           C  Event Date Logic  dbo.834_Inbound_test  2025    11               932            1086      1164
2           C  Event Date Logic  dbo.834_Inbound_test  2026    01               618             733       755
3           C  Event Date Logic  dbo.834_Inbound_test  2026    02               720            1019      1056
4           C  Event Date Logic  dbo.834_Inbound_test  2026    03               380             386       393
st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_test  2025    10              4241            5144      5227
1           C  Event Date Logic  dbo.834_Inbound_test  2025    11               932            1086      1164
2           C  Event Date Logic  dbo.834_Inbound_test  2026    01               618             733       755
3           C  Event Date Logic  dbo.834_Inbound_test  2026    02               720            1019      1056
4           C  Event Date Logic  dbo.834_Inbound_test  2026    03               380             386       393
2026-06-20 23:12:13,338 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml D/dbo.834_Inbound_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:13,340 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id      strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_test  2025    10              4233            5124      5227
1           D  834 Inbound Logic  dbo.834_Inbound_test  2025    11               927            1074      1164
2           D  834 Inbound Logic  dbo.834_Inbound_test  2026    01               614             725       755
3           D  834 Inbound Logic  dbo.834_Inbound_test  2026    02               713            1010      1056
4           D  834 Inbound Logic  dbo.834_Inbound_test  2026    03               378             364       393
st_month head:
  strategy_id      strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_test  2025    10              4233            5124      5227
1           D  834 Inbound Logic  dbo.834_Inbound_test  2025    11               927            1074      1164
2           D  834 Inbound Logic  dbo.834_Inbound_test  2026    01               614             725       755
3           D  834 Inbound Logic  dbo.834_Inbound_test  2026    02               713            1010      1056
4           D  834 Inbound Logic  dbo.834_Inbound_test  2026    03               378             364       393
2026-06-20 23:12:13,539 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_header_test — cols=23 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:12:14,104 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=GAA_834_File_Date rows=8
2026-06-20 23:12:14,142 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:14,144 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    10                 0               0      3102
1           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    11                 0               0      3102
2           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    01                 0               0      3102
3           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    02                 0               0      3102
4           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    03                 0               0      3102
st_month head:
  strategy_id               strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    10                 0               0      3102
1           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2025    11                 0               0      3102
2           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    01                 0               0      3102
3           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    02                 0               0      3102
4           B  Enrollment Status Snapshot  dbo.834_Inbound_header_test  2026    03                 0               0      3102
2026-06-20 23:12:14,165 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:14,167 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_header_test  2025    10                 0               0       376
1           C  Event Date Logic  dbo.834_Inbound_header_test  2025    11                 0               0       458
2           C  Event Date Logic  dbo.834_Inbound_header_test  2026    01                 0               0       478
3           C  Event Date Logic  dbo.834_Inbound_header_test  2026    02                 0               0       362
4           C  Event Date Logic  dbo.834_Inbound_header_test  2026    03                 0               0       320
st_month head:
  strategy_id     strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.834_Inbound_header_test  2025    10                 0               0       376
1           C  Event Date Logic  dbo.834_Inbound_header_test  2025    11                 0               0       458
2           C  Event Date Logic  dbo.834_Inbound_header_test  2026    01                 0               0       478
3           C  Event Date Logic  dbo.834_Inbound_header_test  2026    02                 0               0       362
4           C  Event Date Logic  dbo.834_Inbound_header_test  2026    03                 0               0       320
2026-06-20 23:12:14,189 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml D/dbo.834_Inbound_header_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:12:14,191 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id      strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    10                 0               0       376
1           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    11                 0               0       458
2           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    01                 0               0       478
3           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    02                 0               0       362
4           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    03                 0               0       320
st_month head:
  strategy_id      strategy_name                 source_table  year month  enrollment_count  enrollee_count  raw_rows
0           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    10                 0               0       376
1           D  834 Inbound Logic  dbo.834_Inbound_header_test  2025    11                 0               0       458
2           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    01                 0               0       478
3           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    02                 0               0       362
4           D  834 Inbound Logic  dbo.834_Inbound_header_test  2026    03                 0               0       320
2026-06-20 23:12:14,379 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:15:54,266 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:15:54,268 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    03                 0               0      8000
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    03                 0               0      8000
2026-06-20 23:15:54,454 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2026 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:16:29,550 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:16:29,553 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    03                 0               0      8000
st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    03                 0               0      8000
2026-06-20 23:16:29,747 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:17:16,315 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:17:16,317 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              5140            6642      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              5140            6642      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              5140            6642      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              5140            6642      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    03              5140            6642      8000
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              5140            6642      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              5140            6642      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              5140            6642      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              5140            6642      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    03              5140            6642      8000
2026-06-20 23:17:16,341 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:17:16,344 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10               103             140       140
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01                66              86        86
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02                53              64        64
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    03                54              67        71
st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10               103             140       140
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01                66              86        86
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02                53              64        64
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    03                54              67        71
2026-06-20 23:17:16,532 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_test — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:18:14,401 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:14,403 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10             12592           15594     16000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11             12592           15594     16000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01             12592           15594     16000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02             12592           15594     16000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    03             12592           15594     16000
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10             12592           15594     16000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11             12592           15594     16000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01             12592           15594     16000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02             12592           15594     16000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    03             12592           15594     16000
2026-06-20 23:18:14,438 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:14,441 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10                 0               0         0
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              6599            7990      8000
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02                 0               0         0
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    03                 0               0         0
st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10                 0               0         0
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              6599            7990      8000
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02                 0               0         0
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    03                 0               0         0
2026-06-20 23:18:14,624 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.AT_external_applications — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:18:14,793 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:18:15,575 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CMSFILE_202408 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:15,578 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    10                 0               0     16000
1           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    11                 0               0     16000
2           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    01                 0               0     16000
3           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    02                 0               0     16000
4           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    03                 0               0     16000
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    10                 0               0     16000
1           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    11                 0               0     16000
2           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    01                 0               0     16000
3           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    02                 0               0     16000
4           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    03                 0               0     16000
2026-06-20 23:18:15,778 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408_02 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:18:17,446 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_TXT_TEST1 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:18:18,332 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CMSFILE_TXT_TEST1 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:18,335 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    10                 0               0     16000
1           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    11                 0               0     16000
2           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    01                 0               0     16000
3           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    02                 0               0     16000
4           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    03                 0               0     16000
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    10                 0               0     16000
1           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    11                 0               0     16000
2           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    01                 0               0     16000
3           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    02                 0               0     16000
4           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    03                 0               0     16000
2026-06-20 23:18:18,518 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_All_test — cols=41 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:18:19,007 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Consolidated_Full_list — cols=40 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:19,544 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 19
2026-06-20 23:18:19,677 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=22
2026-06-20 23:18:19,686 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:19,688 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10               179             191       208
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11               168             179       187
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01               345             360       543
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02               332             342       518
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    03               332             342       518
st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10               179             191       208
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11               168             179       187
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01               345             360       543
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02               332             342       518
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    03               332             342       518
2026-06-20 23:18:19,711 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:19,713 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10               753             598      1209
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11               753             598      1209
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01               753             598      1209
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02               753             598      1209
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    03               753             598      1209
st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10               753             598      1209
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11               753             598      1209
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01               753             598      1209
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02               753             598      1209
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    03               753             598      1209
2026-06-20 23:18:19,738 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:19,741 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10               384             346       572
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11               233             244       465
2           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                47              49        51
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                10              11        12
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    03                 9               9        10
st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10               384             346       572
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11               233             244       465
2           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                47              49        51
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                10              11        12
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    03                 9               9        10
2026-06-20 23:18:19,927 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Demographics_Premium — cols=25 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:20,088 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollee_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:18:20,251 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollment_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:18:20,429 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_AETNA — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:21,318 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_Agent — cols=12 issuer=None year=None status=enrollment_status_description action=None
2026-06-20 23:18:21,488 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2025 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:21,979 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC17 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:29,822 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 21
2026-06-20 23:18:30,862 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=19
2026-06-20 23:18:30,873 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:30,876 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              4357            5417      5433
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              4358            5423      5439
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              6316            7843      7963
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4726            5795      5795
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    03              4724            5793      5793
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              4357            5417      5433
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              4358            5423      5439
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              6316            7843      7963
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4726            5795      5795
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    03              4724            5793      5793
2026-06-20 23:18:30,909 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:30,911 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10             12782           15434     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11             12782           15434     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01             12782           15434     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02             12782           15434     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    03             12782           15434     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10             12782           15434     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11             12782           15434     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01             12782           15434     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02             12782           15434     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    03             12782           15434     16000
2026-06-20 23:18:30,946 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:30,948 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10              7714            9317      9427
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               693            1094      1099
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01              1502            1816      1822
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02               246             297       298
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    03               249             286       289
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10              7714            9317      9427
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               693            1094      1099
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01              1502            1816      1822
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02               246             297       298
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    03               249             286       289
2026-06-20 23:18:31,152 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC22 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:37,043 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 23
2026-06-20 23:18:38,098 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=25
2026-06-20 23:18:38,109 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:38,111 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              2643            3565      3569
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              2625            3533      3538
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              6224            7721      7845
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              4608            5638      5642
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    03              4598            5624      5624
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              2643            3565      3569
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              2625            3533      3538
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              6224            7721      7845
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              4608            5638      5642
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    03              4598            5624      5624
2026-06-20 23:18:38,142 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:38,144 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10             12065           15360     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11             12065           15360     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01             12065           15360     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02             12065           15360     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    03             12065           15360     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10             12065           15360     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11             12065           15360     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01             12065           15360     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02             12065           15360     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    03             12065           15360     16000
2026-06-20 23:18:38,180 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:38,182 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10              9261           11722     11741
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11              1098            1756      1782
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               149             210       213
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                41              55        56
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    03                44              53        53
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10              9261           11722     11741
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11              1098            1756      1782
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               149             210       213
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                41              55        56
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    03                44              53        53
2026-06-20 23:18:38,375 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV21 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:50,853 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 22
2026-06-20 23:18:51,892 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=27
2026-06-20 23:18:51,903 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:51,905 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              2503            3109      3118
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              2477            3080      3088
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              6421            7963      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              5903            7326      7326
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    03              5903            7326      7326
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              2503            3109      3118
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              2477            3080      3088
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              6421            7963      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              5903            7326      7326
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    03              5903            7326      7326
2026-06-20 23:18:51,938 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:51,940 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10             12759           12695     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11             12759           12695     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01             12759           12695     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02             12759           12695     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    03             12759           12695     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10             12759           12695     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11             12759           12695     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01             12759           12695     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02             12759           12695     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    03             12759           12695     16000
2026-06-20 23:18:51,972 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:51,974 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10             10323           10885     12670
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11               859            1257      1276
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               269             311       321
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02               142             159       162
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    03               135             176       179
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10             10323           10885     12670
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11               859            1257      1276
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               269             311       321
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02               142             159       162
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    03               135             176       179
2026-06-20 23:18:52,175 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV30 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:18:58,737 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 22
2026-06-20 23:18:59,939 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=25
2026-06-20 23:18:59,949 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:59,951 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              2503            3111      3120
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              2478            3083      3091
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              6589            7954      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              5926            7136      7136
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    03              5926            7136      7136
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              2503            3111      3120
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              2478            3083      3091
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              6589            7954      8000
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              5926            7136      7136
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    03              5926            7136      7136
2026-06-20 23:18:59,987 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:18:59,989 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10             12924           13368     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11             12924           13368     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01             12924           13368     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02             12924           13368     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    03             12924           13368     16000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10             12924           13368     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11             12924           13368     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01             12924           13368     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02             12924           13368     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    03             12924           13368     16000
2026-06-20 23:19:00,023 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:00,025 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10             10343           11129     12530
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11               638             987       988
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               659             864       865
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02               136             157       158
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    03               118             149       149
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10             10343           11129     12530
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11               638             987       988
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               659             864       865
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02               136             157       158
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    03               118             149       149
2026-06-20 23:19:00,227 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_TEST — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:18,931 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 26
2026-06-20 23:19:20,604 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=24
2026-06-20 23:19:20,617 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:20,619 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10              2893            3582      3588
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11              2867            3554      3559
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              5318            6376      6473
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              2483            3094      3097
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    03              2447            3039      3043
st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10              2893            3582      3588
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11              2867            3554      3559
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              5318            6376      6473
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              2483            3094      3097
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    03              2447            3039      3043
2026-06-20 23:19:20,659 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:20,662 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10             12830           14222     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11             12830           14222     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01             12830           14222     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02             12830           14222     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    03             12830           14222     16000
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10             12830           14222     16000
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11             12830           14222     16000
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01             12830           14222     16000
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02             12830           14222     16000
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    03             12830           14222     16000
2026-06-20 23:19:20,700 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:20,702 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10              8254            9307      9983
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11               587             903       908
2           C  Event Date Logic  dbo.Enrollments_TEST  2026    01              1108            1456      1464
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    02               274             339       341
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    03               349             434       435
st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10              8254            9307      9983
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11               587             903       908
2           C  Event Date Logic  dbo.Enrollments_TEST  2026    01              1108            1456      1464
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    02               274             339       341
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    03               349             434       435
2026-06-20 23:19:20,898 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:19:21,529 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:19:22,168 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:19:25,285 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Health_ALL — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:25,287 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2025    10              6475            8000      8000
1           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2025    11              6475            8000      8000
2           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    01              6475            8000      8000
3           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    02              6475            8000      8000
4           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    03              6475            8000      8000
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2025    10              6475            8000      8000
1           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2025    11              6475            8000      8000
2           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    01              6475            8000      8000
3           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    02              6475            8000      8000
4           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL  2026    03              6475            8000      8000
2026-06-20 23:19:25,469 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:19:28,971 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Health_ALL_2 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:28,974 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2025    10              6244            8000      8000
1           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2025    11              6244            8000      8000
2           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    01              6244            8000      8000
3           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    02              6244            8000      8000
4           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    03              6244            8000      8000
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2025    10              6244            8000      8000
1           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2025    11              6244            8000      8000
2           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    01              6244            8000      8000
3           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    02              6244            8000      8000
4           B  Enrollment Status Snapshot  dbo.FPL_Health_ALL_2  2026    03              6244            8000      8000
2026-06-20 23:19:29,150 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_PY2025_PY2026 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:19:30,892 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_PY2025_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:30,894 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10             12639            8644     16000
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11             12639            8644     16000
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01             12639            8644     16000
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02             12639            8644     16000
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    03             12639            8644     16000
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10             12639            8644     16000
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11             12639            8644     16000
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01             12639            8644     16000
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02             12639            8644     16000
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    03             12639            8644     16000
2026-06-20 23:19:31,080 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GA_DEMOGRAPHICS — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:19:31,241 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:19:31,403 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound_test — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:19:31,565 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:19:31,724 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound_test — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:19:31,897 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:32,058 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:32,213 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:19:32,370 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound_test — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:19:32,526 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.HH_SSAP_AT2026 — cols=22 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:32,691 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Issuers_list_test — cols=2 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:19:33,056 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Issuers_list_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:33,059 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    03                 0               0         2
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    03                 0               0         2
2026-06-20 23:19:33,244 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Jan2025_Invoice — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:19:33,872 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Jan2025_Invoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:33,875 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name         source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    10                 0               0      5112
1           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    11                 0               0      5112
2           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    01                 0               0      5112
3           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    02                 0               0      5112
4           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    03                 0               0      5112
st_month head:
  strategy_id               strategy_name         source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    10                 0               0      5112
1           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    11                 0               0      5112
2           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    01                 0               0      5112
3           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    02                 0               0      5112
4           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    03                 0               0      5112
2026-06-20 23:19:34,045 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2024_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:34,198 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:19:34,347 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:34,515 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:35,620 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 12
2026-06-20 23:19:35,792 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=24
2026-06-20 23:19:35,802 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:35,804 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10               920            1315      1315
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11               916            1314      1314
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    03                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10               920            1315      1315
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11               916            1314      1314
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    03                 0               0         0
2026-06-20 23:19:35,829 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:35,831 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10              1816            2524      2760
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11              1816            2524      2760
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01              1816            2524      2760
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02              1816            2524      2760
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    03              1816            2524      2760
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10              1816            2524      2760
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11              1816            2524      2760
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01              1816            2524      2760
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02              1816            2524      2760
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    03              1816            2524      2760
2026-06-20 23:19:35,856 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:35,858 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10              1055            1569      1569
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11               127             290       292
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01               109             163       165
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                36              54        54
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    03                28              39        40
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10              1055            1569      1569
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11               127             290       292
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01               109             163       165
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                36              54        54
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    03                28              39        40
2026-06-20 23:19:36,044 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:40,715 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 14
2026-06-20 23:19:41,080 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=26
2026-06-20 23:19:41,089 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:41,091 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10              1751            2000      2020
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11              1684            1921      1941
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    03                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10              1751            2000      2020
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11              1684            1921      1941
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    03                 0               0         0
2026-06-20 23:19:41,116 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:41,118 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10              7044            7681      8000
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11              7044            7681      8000
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01              7044            7681      8000
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02              7044            7681      8000
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    03              7044            7681      8000
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10              7044            7681      8000
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11              7044            7681      8000
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01              7044            7681      8000
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02              7044            7681      8000
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    03              7044            7681      8000
2026-06-20 23:19:41,143 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:41,145 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10              3071            3461      3479
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11               640             834       835
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01              1200            1318      1324
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02               205             218       218
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    03               173             201       204
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10              3071            3461      3479
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11               640             834       835
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01              1200            1318      1324
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02               205             218       218
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    03               173             201       204
2026-06-20 23:19:41,320 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:19:41,473 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026Applicants_with_tobacco_usage — cols=11 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:41,630 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:41,796 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:42,693 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 21
2026-06-20 23:19:42,820 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=18
2026-06-20 23:19:42,830 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:42,832 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01               814            1199      1202
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02               313             489       490
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    03               293             446       449
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01               814            1199      1202
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02               313             489       490
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    03               293             446       449
2026-06-20 23:19:42,855 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:42,857 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10              1040            1555      1579
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11              1040            1555      1579
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01              1040            1555      1579
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02              1040            1555      1579
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    03              1040            1555      1579
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10              1040            1555      1579
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11              1040            1555      1579
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01              1040            1555      1579
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02              1040            1555      1579
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    03              1040            1555      1579
2026-06-20 23:19:42,881 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:42,883 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10               101             146       146
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                60              84        84
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                61              95        96
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02               287             431       436
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    03               127             205       206
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10               101             146       146
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                60              84        84
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                61              95        96
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02               287             431       436
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    03               127             205       206
2026-06-20 23:19:43,075 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:47,241 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 25
2026-06-20 23:19:47,598 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_confirmation_date rows=20
2026-06-20 23:19:47,609 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:47,611 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01              5359            6437      6619
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02              1974            2372      2392
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    03              1838            2192      2208
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01              5359            6437      6619
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02              1974            2372      2392
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    03              1838            2192      2208
2026-06-20 23:19:47,637 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:47,639 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10              6560            7747      8000
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11              6560            7747      8000
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01              6560            7747      8000
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02              6560            7747      8000
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    03              6560            7747      8000
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10              6560            7747      8000
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11              6560            7747      8000
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01              6560            7747      8000
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02              6560            7747      8000
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    03              6560            7747      8000
2026-06-20 23:19:47,667 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:19:47,669 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10              3535            4372      4401
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11               582             684       690
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01               475             567       569
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02               153             184       184
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    03               168             190       191
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10              3535            4372      4401
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11               582             684       690
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01               475             567       569
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02               153             184       184
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    03               168             190       191
2026-06-20 23:19:47,849 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Reinsurance_APR_PY2026 — cols=29 issuer=None year=None status=enrollee_status_description action=None
2026-06-20 23:19:48,024 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:19:48,184 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test_pp — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:19:48,343 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:48,507 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test_pp — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:48,667 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:19:48,828 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test_pp — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:19:48,988 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_current_and_old_rate — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:19:49,150 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:19:49,316 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income — cols=11 issuer=None year=None status=None action=None
2026-06-20 23:19:49,474 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:19:49,635 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new2 — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:49,798 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_income — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:19:49,962 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:19:50,127 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium_new — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:19:50,309 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:50,471 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL_NEW — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:19:50,634 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:19:50,805 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_1 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:19:50,969 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_2 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:19:51,130 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GW — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:19:51,295 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_RESULTS — cols=49 issuer=None year=None status=None action=None
2026-06-20 23:19:51,464 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_enrollments_cms — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:19:51,633 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_brokers — cols=19 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:51,800 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:51,965 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:52,133 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:52,289 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:52,447 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:19:52,604 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2025 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:23:41,693 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_PY2025 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:23:41,696 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    03                 0               0      8000
st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2025  2026    03                 0               0      8000
2026-06-20 23:23:41,985 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority — cols=3 issuer=None year=None status=None action=None
2026-06-20 23:23:42,165 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority_test — cols=6 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:23:42,739 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_priority_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:23:42,741 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    10                 0               0      4032
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    11                 0               0      4032
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    01                 0               0      4032
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    02                 0               0      4032
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    03                 0               0      4032
st_month head:
  strategy_id               strategy_name                           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    10                 0               0      4032
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2025    11                 0               0      4032
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    01                 0               0      4032
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    02                 0               0      4032
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test  2026    03                 0               0      4032
2026-06-20 23:23:42,930 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_priority_test1 — cols=7 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:23:43,338 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_priority_test1 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:23:43,341 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    10                 0               0      2016
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    11                 0               0      2016
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    01                 0               0      2016
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    02                 0               0      2016
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    03                 0               0      2016
st_month head:
  strategy_id               strategy_name                            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    10                 0               0      2016
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2025    11                 0               0      2016
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    01                 0               0      2016
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    02                 0               0      2016
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_priority_test1  2026    03                 0               0      2016
2026-06-20 23:23:43,561 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_test — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:24:01,014 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:01,017 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    03                 0               0      8000
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    01                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    02                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_test  2026    03                 0               0      8000
2026-06-20 23:24:01,233 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.premium_change — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:24:01,407 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.sysdiagrams — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:24:01,593 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.test_834_in — cols=49 issuer=None year=None status=None action=None
2026-06-20 23:24:01,596 | INFO     | azure_reconciliation.discovery_engine | Selected Azure table=dbo.Enrollments_PY2526_01312026 strategy=A score=75.0 rows=16000 (evaluated 95 tables, 75 strategies)
2026-06-20 23:24:03,292 | INFO     | azure_reconciliation.discovery_engine | Candidate Azure tables for evaluation: 95
2026-06-20 23:24:03,293 | INFO     | azure_reconciliation.azure_mirror.discovery.xml_reference | No XML summary assets for issuer 37001
2026-06-20 23:24:03,535 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:24:10,064 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 16
2026-06-20 23:24:11,035 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=11
2026-06-20 23:24:11,055 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:11,059 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01              2250            3020      3020
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02              2249            3019      3019
st_month head:
  strategy_id             strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    01              2250            3020      3020
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2026  2026    02              2249            3019      3019
2026-06-20 23:24:11,111 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:11,115 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10              2250            3020      3020
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11              2250            3020      3020
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    12              2250            3020      3020
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01              2250            3020      3020
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02              2250            3020      3020
st_month head:
  strategy_id               strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    10              2250            3020      3020
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    11              2250            3020      3020
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2025    12              2250            3020      3020
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    01              2250            3020      3020
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2026  2026    02              2250            3020      3020
2026-06-20 23:24:11,240 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:11,246 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10              2250            3020      3020
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name            source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2026  2025    10              2250            3020      3020
1           C  Event Date Logic  dbo.Enrollments_PY2026  2025    11                 0               0         0
2           C  Event Date Logic  dbo.Enrollments_PY2026  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Enrollments_PY2026  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2026  2026    02                 0               0         0
2026-06-20 23:24:11,453 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_01312026 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:24:32,140 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:24:35,722 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=33
2026-06-20 23:24:35,743 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:35,747 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              1643            2236      2237
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              1575            2143      2144
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    12              1476            2015      2015
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              3921            5202      5202
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              5170            6754      6755
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    10              1643            2236      2237
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    11              1575            2143      2144
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2025    12              1476            2015      2015
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    01              3921            5202      5202
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_01312026  2026    02              5170            6754      6755
2026-06-20 23:24:35,835 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:35,841 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10             11138           12899     14756
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11             11138           12899     14756
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    12             11138           12899     14756
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01             11138           12899     14756
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02             11138           12899     14756
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    10             11138           12899     14756
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    11             11138           12899     14756
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2025    12             11138           12899     14756
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    01             11138           12899     14756
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_01312026  2026    02             11138           12899     14756
2026-06-20 23:24:35,927 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_01312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:24:35,932 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10              4697            5647      6195
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11              1421            2035      2058
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    12              2736            3571      3582
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01              1615            2034      2041
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02                96             124       124
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    10              4697            5647      6195
1           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    11              1421            2035      2058
2           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2025    12              2736            3571      3582
3           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    01              1615            2034      2041
4           C  Event Date Logic  dbo.Enrollments_PY2526_01312026  2026    02                96             124       124
2026-06-20 23:24:36,162 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_02272026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:24:57,621 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:25:01,267 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=32
2026-06-20 23:25:01,287 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:01,293 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              1642            2237      2238
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              1577            2151      2152
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    12              1476            2020      2020
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              3413            4576      4576
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              4525            5956      5956
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    10              1642            2237      2238
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    11              1577            2151      2152
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2025    12              1476            2020      2020
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    01              3413            4576      4576
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_02272026  2026    02              4525            5956      5956
2026-06-20 23:25:01,379 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:01,383 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10             10614           12310     14112
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11             10614           12310     14112
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    12             10614           12310     14112
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01             10614           12310     14112
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02             10614           12310     14112
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    10             10614           12310     14112
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    11             10614           12310     14112
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2025    12             10614           12310     14112
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    01             10614           12310     14112
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_02272026  2026    02             10614           12310     14112
2026-06-20 23:25:01,466 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_02272026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:01,472 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10              4522            5456      5991
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11              1302            1887      1908
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    12              2484            3254      3265
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01              1515            1905      1912
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02               218             280       281
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    10              4522            5456      5991
1           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    11              1302            1887      1908
2           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2025    12              2484            3254      3265
3           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    01              1515            1905      1912
4           C  Event Date Logic  dbo.Enrollments_PY2526_02272026  2026    02               218             280       281
2026-06-20 23:25:01,733 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_03312026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:25:29,149 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:25:30,965 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=33
2026-06-20 23:25:30,975 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:30,978 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              1662            2250      2251
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              1596            2164      2165
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    12              1497            2040      2040
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              4437            5938      5962
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              4103            5450      5451
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    10              1662            2250      2251
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    11              1596            2164      2165
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2025    12              1497            2040      2040
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    01              4437            5938      5962
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_03312026  2026    02              4103            5450      5451
2026-06-20 23:25:31,017 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:31,019 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10             11802           13722     15674
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11             11802           13722     15674
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    12             11802           13722     15674
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01             11802           13722     15674
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02             11802           13722     15674
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    10             11802           13722     15674
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    11             11802           13722     15674
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2025    12             11802           13722     15674
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    01             11802           13722     15674
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_03312026  2026    02             11802           13722     15674
2026-06-20 23:25:31,059 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_03312026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:25:31,062 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10              5035            6122      6688
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11              1501            2126      2147
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    12              2811            3683      3699
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01              1539            1942      1951
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02               218             276       277
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    10              5035            6122      6688
1           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    11              1501            2126      2147
2           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2025    12              2811            3683      3699
3           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    01              1539            1942      1951
4           C  Event Date Logic  dbo.Enrollments_PY2526_03312026  2026    02               218             276       277
2026-06-20 23:25:31,260 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_04302026 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:25:58,873 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:26:00,769 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=34
2026-06-20 23:26:00,779 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:00,781 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              1664            2251      2252
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              1602            2169      2170
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    12              1502            2044      2044
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              4440            5939      5963
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              4111            5459      5460
st_month head:
  strategy_id             strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    10              1664            2251      2252
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    11              1602            2169      2170
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2025    12              1502            2044      2044
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    01              4440            5939      5963
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_04302026  2026    02              4111            5459      5460
2026-06-20 23:26:00,819 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:00,821 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10             11923           13886     15826
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11             11923           13886     15826
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    12             11923           13886     15826
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01             11923           13886     15826
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02             11923           13886     15826
st_month head:
  strategy_id               strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    10             11923           13886     15826
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    11             11923           13886     15826
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2025    12             11923           13886     15826
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    01             11923           13886     15826
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_04302026  2026    02             11923           13886     15826
2026-06-20 23:26:00,868 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_04302026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:00,871 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10              5048            6128      6696
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11              1498            2124      2145
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    12              2805            3679      3694
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01              1544            1938      1954
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02               214             272       273
st_month head:
  strategy_id     strategy_name                     source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    10              5048            6128      6696
1           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    11              1498            2124      2145
2           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2025    12              2805            3679      3694
3           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    01              1544            1938      1954
4           C  Event Date Logic  dbo.Enrollments_PY2526_04302026  2026    02               214             272       273
2026-06-20 23:26:01,077 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_FEB10 — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:26:31,079 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:26:32,843 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=33
2026-06-20 23:26:32,855 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:32,859 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              1661            2245      2246
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              1591            2151      2152
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12              1499            2035      2035
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              3413            4576      4576
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              4575            6024      6024
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10              1661            2245      2246
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11              1591            2151      2152
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12              1499            2035      2035
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01              3413            4576      4576
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02              4575            6024      6024
2026-06-20 23:26:32,895 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:32,897 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10             10603           12253     14054
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11             10603           12253     14054
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12             10603           12253     14054
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01             10603           12253     14054
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02             10603           12253     14054
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    10             10603           12253     14054
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    11             10603           12253     14054
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2025    12             10603           12253     14054
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    01             10603           12253     14054
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_FEB10  2026    02             10603           12253     14054
2026-06-20 23:26:32,934 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_FEB10 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:32,936 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10              4479            5405      5928
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11              1318            1888      1910
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    12              2506            3273      3284
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01              1565            1970      1978
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02               122             156       156
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    10              4479            5405      5928
1           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    11              1318            1888      1910
2           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2025    12              2506            3273      3284
3           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    01              1565            1970      1978
4           C  Event Date Logic  dbo.Enrollments_PY2526_FEB10  2026    02               122             156       156
2026-06-20 23:26:33,142 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC31 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:26:57,833 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:26:59,541 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=33
2026-06-20 23:26:59,554 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:59,556 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              1644            2237      2237
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              1577            2147      2147
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12              1559            2126      2126
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              4605            6127      6143
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              4458            5883      5883
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10              1644            2237      2237
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11              1577            2147      2147
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12              1559            2126      2126
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01              4605            6127      6143
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02              4458            5883      5883
2026-06-20 23:26:59,599 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:59,602 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10             10876           12500     14519
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11             10876           12500     14519
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12             10876           12500     14519
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01             10876           12500     14519
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02             10876           12500     14519
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    10             10876           12500     14519
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    11             10876           12500     14519
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2025    12             10876           12500     14519
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    01             10876           12500     14519
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC31  2026    02             10876           12500     14519
2026-06-20 23:26:59,636 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC31 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:26:59,639 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10              5114            6068      6685
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11              1567            2201      2225
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    12              2947            3842      3852
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               666             847       852
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02                99             127       127
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    10              5114            6068      6685
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    11              1567            2201      2225
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2025    12              2947            3842      3852
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    01               666             847       852
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC31  2026    02                99             127       127
2026-06-20 23:26:59,853 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.DuplicateEnrollment_Overlap — cols=121 issuer=None year=None status=None action=None
2026-06-20 23:27:00,031 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_test — cols=80 issuer=GAA_HIOS_ID year=Coverage_Year status=enrolleeStatus action=actionCode
2026-06-20 23:27:01,227 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.834_Inbound_header_test — cols=23 issuer=GAA_HIOS_ID year=None status=None action=None
2026-06-20 23:27:01,728 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:31:01,722 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:31:01,725 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    10                 0               0      8000
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    11                 0               0      8000
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2025    12                 0               0      8000
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    01                 0               0      8000
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy  2026    02                 0               0      8000
2026-06-20 23:31:01,920 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2026 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
2026-06-20 23:32:09,098 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.monthly_discrepancy_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:32:09,100 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      6630
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      6630
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    12                 0               0      6630
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      6630
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      6630
st_month head:
  strategy_id               strategy_name                    source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    10                 0               0      6630
1           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    11                 0               0      6630
2           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2025    12                 0               0      6630
3           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    01                 0               0      6630
4           B  Enrollment Status Snapshot  dbo.monthly_discrepancy_PY2026  2026    02                 0               0      6630
2026-06-20 23:32:09,284 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:32:56,994 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:32:56,996 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              2997            4014      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              2997            4014      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    12              2997            4014      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              2997            4014      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              2997            4014      8000
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    10              2997            4014      8000
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    11              2997            4014      8000
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2025    12              2997            4014      8000
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    01              2997            4014      8000
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice  2026    02              2997            4014      8000
2026-06-20 23:32:57,022 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:32:57,024 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10              2497            3331      3331
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01                28              39        44
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02                20              32        37
st_month head:
  strategy_id         strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    10              2497            3331      3331
1           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    01                28              39        44
4           E  CarrierInvoice Logic  dbo.CarrierInvoice  2026    02                20              32        37
2026-06-20 23:32:57,220 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_test — cols=40 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:33:58,683 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:33:58,686 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10              6699            8928     13027
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11              6699            8928     13027
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    12              6699            8928     13027
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01              6699            8928     13027
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02              6699            8928     13027
st_month head:
  strategy_id               strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    10              6699            8928     13027
1           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    11              6699            8928     13027
2           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2025    12              6699            8928     13027
3           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    01              6699            8928     13027
4           B  Enrollment Status Snapshot  dbo.CarrierInvoice_test  2026    02              6699            8928     13027
2026-06-20 23:33:58,715 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml E/dbo.CarrierInvoice_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:33:58,717 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10              2169            2873      3030
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              3766            5000      5027
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02                 0               0         0
st_month head:
  strategy_id         strategy_name             source_table  year month  enrollment_count  enrollee_count  raw_rows
0           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    10              2169            2873      3030
1           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    11                 0               0         0
2           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2025    12                 0               0         0
3           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    01              3766            5000      5027
4           E  CarrierInvoice Logic  dbo.CarrierInvoice_test  2026    02                 0               0         0
2026-06-20 23:33:58,910 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.AT_external_applications — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:33:59,085 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:34:00,704 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CMSFILE_202408 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:00,707 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    10                 0               0      8850
1           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    11                 0               0      8850
2           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    12                 0               0      8850
3           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    01                 0               0      8850
4           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    02                 0               0      8850
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    10                 0               0      8850
1           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    11                 0               0      8850
2           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2025    12                 0               0      8850
3           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    01                 0               0      8850
4           B  Enrollment Status Snapshot  dbo.CMSFILE_202408  2026    02                 0               0      8850
2026-06-20 23:34:00,898 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_202408_02 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:34:02,827 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CMSFILE_TXT_TEST1 — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:34:05,906 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.CMSFILE_TXT_TEST1 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:05,909 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    10                 0               0      8850
1           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    11                 0               0      8850
2           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    12                 0               0      8850
3           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    01                 0               0      8850
4           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    02                 0               0      8850
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    10                 0               0      8850
1           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    11                 0               0      8850
2           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2025    12                 0               0      8850
3           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    01                 0               0      8850
4           B  Enrollment Status Snapshot  dbo.CMSFILE_TXT_TEST1  2026    02                 0               0      8850
2026-06-20 23:34:06,096 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.CarrierInvoice_All_test — cols=41 issuer=hios_issuer_id year=invoice_year status=None action=None
2026-06-20 23:34:06,584 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Consolidated_Full_list — cols=40 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:07,076 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 9
2026-06-20 23:34:07,146 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_last_update_date rows=10
2026-06-20 23:34:07,157 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:07,160 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10                 1               1         1
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11                 1               1         1
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    12                 1               1         1
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01                 1               1         1
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02                 1               1         1
st_month head:
  strategy_id             strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    10                 1               1         1
1           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    11                 1               1         1
2           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2025    12                 1               1         1
3           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    01                 1               1         1
4           A  Active Coverage Snapshot  dbo.Consolidated_Full_list  2026    02                 1               1         1
2026-06-20 23:34:07,184 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:07,186 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10                 5               4         7
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11                 5               4         7
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    12                 5               4         7
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01                 5               4         7
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02                 5               4         7
st_month head:
  strategy_id               strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    10                 5               4         7
1           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    11                 5               4         7
2           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2025    12                 5               4         7
3           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    01                 5               4         7
4           B  Enrollment Status Snapshot  dbo.Consolidated_Full_list  2026    02                 5               4         7
2026-06-20 23:34:07,208 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Consolidated_Full_list — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:07,210 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10                 0               0         0
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11                 2               2         3
2           C  Event Date Logic  dbo.Consolidated_Full_list  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name                source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Consolidated_Full_list  2025    10                 0               0         0
1           C  Event Date Logic  dbo.Consolidated_Full_list  2025    11                 2               2         3
2           C  Event Date Logic  dbo.Consolidated_Full_list  2025    12                 0               0         0
3           C  Event Date Logic  dbo.Consolidated_Full_list  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Consolidated_Full_list  2026    02                 0               0         0
2026-06-20 23:34:07,405 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Demographics_Premium — cols=25 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:07,570 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollee_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:34:07,737 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollment_Premium — cols=9 issuer=None year=None status=None action=None
2026-06-20 23:34:07,907 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_AETNA — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:08,674 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_Agent — cols=12 issuer=None year=None status=enrollment_status_description action=None
2026-06-20 23:34:08,842 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2025 — cols=56 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:09,337 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC17 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:35,469 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 27
2026-06-20 23:34:36,092 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=16
2026-06-20 23:34:36,110 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:36,113 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              4587            6091      6182
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4230            5594      5665
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              4587            6091      6182
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4230            5594      5665
2026-06-20 23:34:36,152 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:36,155 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              4628            6141      6233
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              4628            6141      6233
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12              4628            6141      6233
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              4628            6141      6233
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4628            6141      6233
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    10              4628            6141      6233
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    11              4628            6141      6233
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2025    12              4628            6141      6233
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    01              4628            6141      6233
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC17  2026    02              4628            6141      6233
2026-06-20 23:34:36,192 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC17 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:36,196 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10              2253            2994      3032
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               853            1113      1133
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    12              1559            2044      2068
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02                 0               0         0
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    10              2253            2994      3032
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    11               853            1113      1133
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2025    12              1559            2044      2068
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    01                 0               0         0
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC17  2026    02                 0               0         0
2026-06-20 23:34:36,399 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_DEC22 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:34:56,012 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 37
2026-06-20 23:34:57,071 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=32
2026-06-20 23:34:57,082 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:57,085 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              1739            2313      2319
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              1670            2227      2233
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12              1648            2192      2198
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              4591            6108      6119
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              4298            5696      5696
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10              1739            2313      2319
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11              1670            2227      2233
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12              1648            2192      2198
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01              4591            6108      6119
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02              4298            5696      5696
2026-06-20 23:34:57,115 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:57,117 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10             10794           12268     14272
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11             10794           12268     14272
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12             10794           12268     14272
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01             10794           12268     14272
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02             10794           12268     14272
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    10             10794           12268     14272
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    11             10794           12268     14272
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2025    12             10794           12268     14272
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    01             10794           12268     14272
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_DEC22  2026    02             10794           12268     14272
2026-06-20 23:34:57,150 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_DEC22 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:34:57,153 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10              5068            5960      6521
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11              1534            2164      2179
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    12              2952            3839      3854
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               818            1005      1012
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                94             119       122
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    10              5068            5960      6521
1           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    11              1534            2164      2179
2           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2025    12              2952            3839      3854
3           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    01               818            1005      1012
4           C  Event Date Logic  dbo.Enrollments_PY2526_DEC22  2026    02                94             119       122
2026-06-20 23:34:57,348 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV21 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:35:13,773 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 25
2026-06-20 23:35:14,653 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=35
2026-06-20 23:35:14,664 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:14,667 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              1703            2301      2308
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              1706            2296      2303
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              1708            2298      2305
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              2846            3787      3791
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              2704            3600      3600
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              1703            2301      2308
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              1706            2296      2303
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              1708            2298      2305
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              2846            3787      3791
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              2704            3600      3600
2026-06-20 23:35:14,699 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:14,702 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              8808            9618     11791
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              8808            9618     11791
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              8808            9618     11791
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              8808            9618     11791
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              8808            9618     11791
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    10              8808            9618     11791
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    11              8808            9618     11791
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2025    12              8808            9618     11791
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    01              8808            9618     11791
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV21  2026    02              8808            9618     11791
2026-06-20 23:35:14,736 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV21 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:14,739 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10              5139            6074      6726
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11              1349            1933      1948
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    12              1066            1388      1391
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               654             833       838
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02                99             127       127
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    10              5139            6074      6726
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    11              1349            1933      1948
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2025    12              1066            1388      1391
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    01               654             833       838
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV21  2026    02                99             127       127
2026-06-20 23:35:14,931 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_PY2526_NOV30 — cols=52 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:35:45,051 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 30
2026-06-20 23:35:46,042 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_create_date rows=35
2026-06-20 23:35:46,053 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:46,055 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              1704            2300      2307
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              1706            2294      2301
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              1713            2302      2309
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              3032            4044      4049
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              2848            3793      3793
st_month head:
  strategy_id             strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              1704            2300      2307
1           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              1706            2294      2301
2           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              1713            2302      2309
3           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              3032            4044      4049
4           A  Active Coverage Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              2848            3793      3793
2026-06-20 23:35:46,094 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:46,097 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              8997            9899     12049
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              8997            9899     12049
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              8997            9899     12049
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              8997            9899     12049
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              8997            9899     12049
st_month head:
  strategy_id               strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    10              8997            9899     12049
1           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    11              8997            9899     12049
2           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2025    12              8997            9899     12049
3           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    01              8997            9899     12049
4           B  Enrollment Status Snapshot  dbo.Enrollments_PY2526_NOV30  2026    02              8997            9899     12049
2026-06-20 23:35:46,140 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_PY2526_NOV30 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:35:46,144 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10              5113            6038      6687
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11              1571            2224      2245
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    12              1065            1386      1389
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               654             834       839
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02                99             127       127
st_month head:
  strategy_id     strategy_name                  source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    10              5113            6038      6687
1           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    11              1571            2224      2245
2           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2025    12              1065            1386      1389
3           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    01               654             834       839
4           C  Event Date Logic  dbo.Enrollments_PY2526_NOV30  2026    02                99             127       127
2026-06-20 23:35:46,356 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Enrollments_TEST — cols=57 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:36:24,506 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 36
2026-06-20 23:36:26,311 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollment_create_date rows=35
2026-06-20 23:36:26,324 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:26,328 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10              1669            2251      2252
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11              1606            2172      2173
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    12              1512            2053      2053
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              4446            5935      5961
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              4124            5462      5463
st_month head:
  strategy_id             strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    10              1669            2251      2252
1           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    11              1606            2172      2173
2           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2025    12              1512            2053      2053
3           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    01              4446            5935      5961
4           A  Active Coverage Snapshot  dbo.Enrollments_TEST  2026    02              4124            5462      5463
2026-06-20 23:36:26,377 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:26,380 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10             12058           14086     15998
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11             12058           14086     15998
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    12             12058           14086     15998
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01             12058           14086     15998
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02             12058           14086     15998
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    10             12058           14086     15998
1           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    11             12058           14086     15998
2           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2025    12             12058           14086     15998
3           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    01             12058           14086     15998
4           B  Enrollment Status Snapshot  dbo.Enrollments_TEST  2026    02             12058           14086     15998
2026-06-20 23:36:26,431 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.Enrollments_TEST — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:26,434 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10              5037            6128      6683
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11              1504            2132      2154
2           C  Event Date Logic  dbo.Enrollments_TEST  2025    12              2816            3682      3697
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    01              1544            1931      1947
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    02               219             276       277
st_month head:
  strategy_id     strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.Enrollments_TEST  2025    10              5037            6128      6683
1           C  Event Date Logic  dbo.Enrollments_TEST  2025    11              1504            2132      2154
2           C  Event Date Logic  dbo.Enrollments_TEST  2025    12              2816            3682      3697
3           C  Event Date Logic  dbo.Enrollments_TEST  2026    01              1544            1931      1947
4           C  Event Date Logic  dbo.Enrollments_TEST  2026    02               219             276       277
2026-06-20 23:36:26,636 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:36:27,330 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Dental_ALL — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:27,332 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    10              2595            3472      3472
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    11              2595            3472      3472
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    12              2595            3472      3472
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    01              2595            3472      3472
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    02              2595            3472      3472
st_month head:
  strategy_id               strategy_name        source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    10              2595            3472      3472
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    11              2595            3472      3472
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2025    12              2595            3472      3472
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    01              2595            3472      3472
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL  2026    02              2595            3472      3472
2026-06-20 23:36:27,514 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Dental_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:36:28,081 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_Dental_ALL_2 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:28,085 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    10              2597            3480      3480
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    11              2597            3480      3480
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    12              2597            3480      3480
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    01              2597            3480      3480
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    02              2597            3480      3480
st_month head:
  strategy_id               strategy_name          source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    10              2597            3480      3480
1           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    11              2597            3480      3480
2           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2025    12              2597            3480      3480
3           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    01              2597            3480      3480
4           B  Enrollment Status Snapshot  dbo.FPL_Dental_ALL_2  2026    02              2597            3480      3480
2026-06-20 23:36:28,262 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL — cols=19 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:36:31,461 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_Health_ALL_2 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:36:35,224 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.FPL_PY2025_PY2026 — cols=23 issuer=hios_issuer_id year=coverage_year status=None action=None
2026-06-20 23:36:41,833 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.FPL_PY2025_PY2026 — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:41,837 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10              5183            3520      6955
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11              5183            3520      6955
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    12              5183            3520      6955
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01              5183            3520      6955
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02              5183            3520      6955
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    10              5183            3520      6955
1           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    11              5183            3520      6955
2           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2025    12              5183            3520      6955
3           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    01              5183            3520      6955
4           B  Enrollment Status Snapshot  dbo.FPL_PY2025_PY2026  2026    02              5183            3520      6955
2026-06-20 23:36:42,021 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GA_DEMOGRAPHICS — cols=6 issuer=None year=None status=None action=None
2026-06-20 23:36:42,184 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:36:42,351 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Inbound_test — cols=5 issuer=None year=None status=status action=None
2026-06-20 23:36:42,516 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:36:42,676 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GI_Outbound_test — cols=4 issuer=None year=None status=status action=None
2026-06-20 23:36:42,856 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:36:43,013 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Inbound_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:36:43,172 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:36:43,331 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.GW_Outbound_test — cols=19 issuer=None year=None status=None action=None
2026-06-20 23:36:43,491 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.HH_SSAP_AT2026 — cols=22 issuer=None year=coverage_year status=None action=None
2026-06-20 23:36:43,646 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Issuers_list_test — cols=2 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:36:44,016 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Issuers_list_test — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:44,019 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    12                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
st_month head:
  strategy_id               strategy_name           source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    10                 0               0         2
1           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    11                 0               0         2
2           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2025    12                 0               0         2
3           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    01                 0               0         2
4           B  Enrollment Status Snapshot  dbo.Issuers_list_test  2026    02                 0               0         2
2026-06-20 23:36:44,200 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Jan2025_Invoice — cols=21 issuer=Issuer_ID year=None status=None action=None
2026-06-20 23:36:44,876 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.Jan2025_Invoice — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:44,880 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name         source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    10                 0               0      1464
1           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    11                 0               0      1464
2           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    12                 0               0      1464
3           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    01                 0               0      1464
4           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    02                 0               0      1464
st_month head:
  strategy_id               strategy_name         source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    10                 0               0      1464
1           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    11                 0               0      1464
2           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2025    12                 0               0      1464
3           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    01                 0               0      1464
4           B  Enrollment Status Snapshot  dbo.Jan2025_Invoice  2026    02                 0               0      1464
2026-06-20 23:36:45,050 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2024_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:36:45,213 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:36:45,377 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:36:45,545 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:36:46,649 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 11
2026-06-20 23:36:46,758 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=16
2026-06-20 23:36:46,770 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:46,773 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10                12              14        14
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11                10              12        12
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    12                 8              10        10
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    10                12              14        14
1           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    11                10              12        12
2           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2025    12                 8              10        10
3           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPDOB  2026    02                 0               0         0
2026-06-20 23:36:46,798 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:46,801 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10                43              50        52
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11                43              50        52
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    12                43              50        52
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01                43              50        52
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02                43              50        52
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    10                43              50        52
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    11                43              50        52
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2025    12                43              50        52
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    01                43              50        52
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPDOB  2026    02                43              50        52
2026-06-20 23:36:46,827 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:46,830 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11                 8              11        11
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    12                 5               5         6
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01                11              15        15
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                 1               1         1
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    11                 8              11        11
2           C  Event Date Logic  dbo.PY2025_DUPDOB  2025    12                 5               5         6
3           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    01                11              15        15
4           C  Event Date Logic  dbo.PY2025_DUPDOB  2026    02                 1               1         1
2026-06-20 23:36:47,022 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2025_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:36:52,618 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 21
2026-06-20 23:36:52,912 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=30
2026-06-20 23:36:52,922 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:52,924 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10               569             821       842
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11               534             787       801
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    12               500             733       745
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    10               569             821       842
1           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    11               534             787       801
2           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2025    12               500             733       745
3           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    01                 0               0         0
4           A  Active Coverage Snapshot  dbo.PY2025_DUPSSN  2026    02                 0               0         0
2026-06-20 23:36:52,958 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:52,960 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10              2499            3254      3912
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11              2499            3254      3912
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    12              2499            3254      3912
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01              2499            3254      3912
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02              2499            3254      3912
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    10              2499            3254      3912
1           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    11              2499            3254      3912
2           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2025    12              2499            3254      3912
3           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    01              2499            3254      3912
4           B  Enrollment Status Snapshot  dbo.PY2025_DUPSSN  2026    02              2499            3254      3912
2026-06-20 23:36:52,993 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2025_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:52,995 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10                99             136       144
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11               569             965      1039
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    12               543             745       800
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01               453             689       708
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02                56              72        76
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    10                99             136       144
1           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    11               569             965      1039
2           C  Event Date Logic  dbo.PY2025_DUPSSN  2025    12               543             745       800
3           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    01               453             689       708
4           C  Event Date Logic  dbo.PY2025_DUPSSN  2026    02                56              72        76
2026-06-20 23:36:53,178 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026-Enrollments_All — cols=4 issuer=None year=coverage_year status=enrollment_status_description action=None
2026-06-20 23:36:53,339 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026Applicants_with_tobacco_usage — cols=11 issuer=None year=coverage_year status=None action=None
2026-06-20 23:36:53,495 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_Applicants — cols=10 issuer=None year=coverage_year status=None action=None
2026-06-20 23:36:53,666 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPDOB — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:36:54,514 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 16
2026-06-20 23:36:54,596 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=11
2026-06-20 23:36:54,615 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:54,618 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01                14              16        17
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02                 6               7         7
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    01                14              16        17
4           A  Active Coverage Snapshot  dbo.PY2026_DUPDOB  2026    02                 6               7         7
2026-06-20 23:36:54,646 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:54,648 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10                15              17        18
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11                15              17        18
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    12                15              17        18
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01                15              17        18
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02                15              17        18
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    10                15              17        18
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    11                15              17        18
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2025    12                15              17        18
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    01                15              17        18
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPDOB  2026    02                15              17        18
2026-06-20 23:36:54,676 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPDOB — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:36:54,680 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                 2               2         2
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    12                 2               2         2
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                 0               0         0
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02                 7               9         9
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    10                 1               1         1
1           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    11                 2               2         2
2           C  Event Date Logic  dbo.PY2026_DUPDOB  2025    12                 2               2         2
3           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    01                 0               0         0
4           C  Event Date Logic  dbo.PY2026_DUPDOB  2026    02                 7               9         9
2026-06-20 23:36:54,872 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.PY2026_DUPSSN — cols=55 issuer=hios_issuer_id year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:37:00,376 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy A summary rows: 27
2026-06-20 23:37:00,546 | INFO     | azure_reconciliation.azure_mirror.discovery.strategies | Strategy C best_date_col=enrollee_last_update_date rows=25
2026-06-20 23:37:00,556 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml A/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:37:00,559 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01               705             953       982
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02               532             735       744
st_month head:
  strategy_id             strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    10                 0               0         0
1           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    11                 0               0         0
2           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2025    12                 0               0         0
3           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    01               705             953       982
4           A  Active Coverage Snapshot  dbo.PY2026_DUPSSN  2026    02               532             735       744
2026-06-20 23:37:00,584 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml B/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:37:00,586 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10              1039            1382      1430
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11              1039            1382      1430
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    12              1039            1382      1430
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01              1039            1382      1430
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02              1039            1382      1430
st_month head:
  strategy_id               strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    10              1039            1382      1430
1           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    11              1039            1382      1430
2           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2025    12              1039            1382      1430
3           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    01              1039            1382      1430
4           B  Enrollment Status Snapshot  dbo.PY2026_DUPSSN  2026    02              1039            1382      1430
2026-06-20 23:37:00,619 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | score_strategy_vs_xml C/dbo.PY2026_DUPSSN — st_month.columns=['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows'] xml_month.columns=['year', 'month', 'enrollment_count', 'enrollee_count']
st_month.columns: ['strategy_id', 'strategy_name', 'source_table', 'year', 'month', 'enrollment_count', 'enrollee_count', 'raw_rows']
xml_month.columns: ['year', 'month', 'enrollment_count', 'enrollee_count']
2026-06-20 23:37:00,622 | INFO     | azure_reconciliation.azure_mirror.discovery.scoring | st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10                 3               3         5
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11               147             200       204
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    12               321             428       435
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01               198             257       260
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02                89             121       124
st_month head:
  strategy_id     strategy_name       source_table  year month  enrollment_count  enrollee_count  raw_rows
0           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    10                 3               3         5
1           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    11               147             200       204
2           C  Event Date Logic  dbo.PY2026_DUPSSN  2025    12               321             428       435
3           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    01               198             257       260
4           C  Event Date Logic  dbo.PY2026_DUPSSN  2026    02                89             121       124
2026-06-20 23:37:00,805 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.Reinsurance_APR_PY2026 — cols=29 issuer=None year=None status=enrollee_status_description action=None
2026-06-20 23:37:00,985 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:37:01,155 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_lms_test_pp — cols=20 issuer=None year=None status=None action=None
2026-06-20 23:37:01,329 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:37:01,498 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sircon_test_pp — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:37:01,675 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:37:01,834 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.agent_sisense_test_pp — cols=8 issuer=None year=None status=None action=None
2026-06-20 23:37:01,994 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_current_and_old_rate — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:37:02,157 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:37:02,330 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income — cols=11 issuer=None year=None status=None action=None
2026-06-20 23:37:02,491 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new — cols=12 issuer=None year=None status=None action=None
2026-06-20 23:37:02,659 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_fpl_with_income_new2 — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:37:02,828 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_income — cols=5 issuer=None year=None status=None action=None
2026-06-20 23:37:02,987 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:37:03,154 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.arpa_household_premium_new — cols=7 issuer=None year=None status=None action=None
2026-06-20 23:37:03,344 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:37:03,504 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_ALL_NEW — cols=26 issuer=None year=coverage_year status=enrollee_status_description action=None
2026-06-20 23:37:03,667 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:37:03,845 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_1 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:37:04,010 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GI_2 — cols=28 issuer=None year=None status=None action=None
2026-06-20 23:37:04,169 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_GW — cols=10 issuer=None year=None status=None action=None
2026-06-20 23:37:04,347 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_RESULTS — cols=49 issuer=None year=None status=None action=None
2026-06-20 23:37:04,510 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.concurrent_enrollments_cms — cols=13 issuer=None year=None status=None action=None
2026-06-20 23:37:04,681 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_brokers — cols=19 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:04,852 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:05,009 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:05,175 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_enrollees_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:05,332 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2025 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:05,493 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.hh_demographics_subscribers_PY2026 — cols=26 issuer=None year=coverage_year status=None action=None
2026-06-20 23:37:05,649 | INFO     | azure_reconciliation.azure_mirror.discovery.table_inspector | Inspected dbo.monthly_discrepancy_PY2025 — cols=24 issuer=GAA_HIOS_ID year=Coverage_Year status=Enrollment_Status action=None
