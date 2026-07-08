INBOUND AUTOMATION — CREATE TABLES (Phase 2A)
Azure config presence (no secrets):
  SERVER present: True
  DATABASE present: True
  USERNAME present: True
  DRIVER present: True
  AZURE_SQL_SCHEMA present: True
Pre-check table existence:
  dbo.inbound_automation: MISSING
  dbo.inbound_automation_run_log: MISSING
  dbo.inbound_automation_file_log: MISSING
Executing approved DDL from: C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\sql\inbound_automation_ddl.sql
Traceback (most recent call last):
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context                                                                                                                                 
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
pyodbc.ProgrammingError: ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]CREATE TABLE permission denied in database 'GAA CMS Data'. (262) (SQLExecDirectW)")                                                                                                                   

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\run_inbound_automation_load.py", line 32, in <module>
    raise SystemExit(main(argv))
                     ~~~~^^^^^^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\inbound_automation\cli.py", line 138, in main
    return create_phase2a_tables(ddl_path=ddl_path, runner_name="inbound_automation_create_tables")
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\inbound_automation\azure_ddl.py", line 157, in create_phase2a_tables                                                                                                                                                   
    _execute_ddl_file(engine=engine, ddl_path=ddl_path)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\inbound_automation\azure_ddl.py", line 86, in _execute_ddl_file
    conn.exec_driver_sql(batch)
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1781, in exec_driver_sql                                                                                                                                      
    ret = self._execute_context(
        dialect,
    ...<5 lines>...
        distilled_parameters,
    )
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1848, in _execute_context                                                                                                                                     
    return self._exec_single_context(
           ~~~~~~~~~~~~~~~~~~~~~~~~~^
        dialect, context, statement, parameters
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1988, in _exec_single_context                                                                                                                                 
    self._handle_dbapi_exception(
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        e, str_statement, effective_parameters, cursor, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 2365, in _handle_dbapi_exception                                                                                                                              
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\base.py", line 1969, in _exec_single_context                                                                                                                                 
    self.dialect.do_execute(
    ~~~~~~~~~~~~~~~~~~~~~~~^
        cursor, str_statement, effective_parameters, context
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "C:\Users\SelmaKazanci\Downloads\project\gaaccess-develop8\834_issuer_etl\.venv\Lib\site-packages\sqlalchemy\engine\default.py", line 952, in do_execute
    cursor.execute(statement, parameters)
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
sqlalchemy.exc.ProgrammingError: (pyodbc.ProgrammingError) ('42000', "[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]CREATE TABLE permission denied in database 'GAA CMS Data'. (262) (SQLExecDirectW)")                                                                                 
[SQL: -- =============================================================================                                                              
-- Azure SQL DDL: inbound_automation raw ingestion (NEW TABLES ONLY)                                                                                
-- =============================================================================                                                                    
-- Status: APPROVED schema — do not execute in production until DBA sign-off.                                                                       
-- Does NOT modify dbo.834_Inbound_test, Enrollments_*, or any existing table.                                                                      
--                                                                                                                                                  
-- Tables:                                                                                                                                          
--   1. dbo.inbound_automation          — one row per Parser834 enrollee                                                                            
--   2. dbo.inbound_automation_run_log  — one row per load run                                                                                      
--   3. dbo.inbound_automation_file_log — one row per successfully processed file                                                                   
--                                                                                                                                                  
-- Safety: CREATE TABLE IF NOT EXISTS only. No DROP / TRUNCATE / ALTER.                                                                             
-- =============================================================================                                                                    
                                                                                                                                                    
-- -----------------------------------------------------------------------------                                                                    
-- 1. dbo.inbound_automation                                                                                                                        
-- -----------------------------------------------------------------------------                                                                    
IF OBJECT_ID(N'dbo.inbound_automation', N'U') IS NULL                                                                                               
BEGIN                                                                                                                                               
    CREATE TABLE dbo.inbound_automation (                                                                                                           
        -- surrogate / run                                                                                                                          
        id                              BIGINT IDENTITY(1,1) NOT NULL,                                                                              
        load_run_id                     NVARCHAR(100)        NOT NULL,                                                                              
        loaded_at                       DATETIME2(3)         NOT NULL                                                                               
            CONSTRAINT DF_inbound_automation_loaded_at DEFAULT SYSUTCDATETIME(),                                                                    
                                                                                                                                                    
        -- automation lineage                                                                                                                       
        folder_year                     INT                  NOT NULL,                                                                              
        folder_month                    INT                  NOT NULL,                                                                              
        filename_file_year              INT                  NULL,                                                                                  
        filename_file_month             INT                  NULL,                                                                                  
        source_file                     NVARCHAR(500)        NOT NULL,                                                                              
        source_file_path                NVARCHAR(1000)       NOT NULL,                                                                              
        file_hash                       NVARCHAR(128)        NOT NULL,                                                                              
        row_number_in_file              INT                  NOT NULL,                                                                              
        raw_record_hash                 NVARCHAR(128)        NOT NULL,                                                                              
                                                                                                                                                    
        -- provenance / coverage (runner-added)                                                                                                     
        parser_version                  NVARCHAR(50)         NULL,                                                                                  
        runner_version                  NVARCHAR(50)         NULL,                                                                                  
        git_commit                      NVARCHAR(100)        NULL,                                                                                  
        coverage_year                   INT                  NULL,                                                                                  
        coverage_year_source            NVARCHAR(50)         NULL,                                                                                  
        warning_count                   INT                  NULL,                                                                                  
                                                                                                                                                    
        -- derived (not parser-native)                                                                                                              
        insurance_type                  NVARCHAR(50)         NULL,                                                                                  
        enrolleeStatus                  NVARCHAR(50)         NULL,                                                                                  
                                                                                                                                                    
        -- Parser834 keys (43) — exact snake_case names from parse_file()                                                                           
        issuer                          NVARCHAR(20)         NOT NULL,                                                                              
        year                            NVARCHAR(4)          NOT NULL,                                                                              
        month                           NVARCHAR(2)          NOT NULL,                                                                              
        file_name                       NVARCHAR(500)        NOT NULL,                                                                              
        raw_xml_path                    NVARCHAR(1000)       NOT NULL,                                                                              
        created_at                      NVARCHAR(40)         NOT NULL,                                                                              
                                                                                                                                                    
        policy_id                       NVARCHAR(100)        NULL,                                                                                  
        member_id                       NVARCHAR(100)        NULL,          -- PII: member identifier                                               
        subscriber_id                   NVARCHAR(100)        NULL,          -- PII: member identifier                                               
        exchg_assigned_enrollee_id      NVARCHAR(100)        NULL,          -- PII: member identifier                                               
        issuer_subscriber_identifier    NVARCHAR(100)        NULL,          -- PII: member identifier                                               
        issuer_indiv_identifier         NVARCHAR(100)        NULL,          -- PII: member identifier                                               
        member_first_name               NVARCHAR(200)        NULL,          -- PII                                                                  
        member_last_name                NVARCHAR(200)        NULL,          -- PII                                                                  
        relationship                    NVARCHAR(50)         NULL,                                                                                  
        subscriber_flag                 NVARCHAR(20)         NULL,                                                                                  
        enrollee_event_type_code        NVARCHAR(50)         NULL,                                                                                  
        enrollee_event_reason_code      NVARCHAR(50)         NULL,                                                                                  
        action_code                     NVARCHAR(50)         NULL,                                                                                  
        action_code_description         NVARCHAR(100)        NULL,                                                                                  
        maintenance_type_code           NVARCHAR(50)         NULL,                                                                                  
        additional_maint_reason_code    NVARCHAR(50)         NULL,                                                                                  
        coverage_status                 NVARCHAR(100)        NULL,                                                                                  
        benefit_effective_date          DATE                 NULL,                                                                                  
        benefit_end_date                DATE                 NULL,                                                                                  
        member_maint_effective_date     DATE                 NULL,                                                                                  
        last_premium_paid_date          NVARCHAR(20)         NULL,                                                                                  
        request_submit_timestamp        NVARCHAR(100)        NULL,                                                                                  
        total_premium_amount            DECIMAL(18,4)        NULL,                                                                                  
        individual_responsibility_amount DECIMAL(18,4)       NULL,                                                                                  
        aptc_amount                     DECIMAL(18,4)        NULL,                                                                                  
        user_fee_amount                 DECIMAL(18,4)        NULL,                                                                                  
        insurance_type_code             NVARCHAR(50)         NULL,                                                                                  
        health_coverage_policy_no       NVARCHAR(100)        NULL,                                                                                  
        household_or_employee_case_id   NVARCHAR(100)        NULL,                                                                                  
        rating_area                     NVARCHAR(50)         NULL,                                                                                  
        source_exchg_id                 NVARCHAR(100)        NULL,                                                                                  
        enrollment_action_code          NVARCHAR(50)         NULL,                                                                                  
        insurer_tax_id_number           NVARCHAR(50)         NULL,                                                                                  
        qtyn                            NVARCHAR(50)         NULL,                                                                                  
        qtyy                            NVARCHAR(50)         NULL,                                                                                  
        qtyt                            NVARCHAR(50)         NULL,                                                                                  
        raw_payload                     NVARCHAR(MAX)        NOT NULL,                                                                              
                                                                                                                                                    
        -- lossless enriched backup (parser row + automation + derived + provenance)                                                                
        raw_json                        NVARCHAR(MAX)        NOT NULL,                                                                              
                                                                                                                                                    
        CONSTRAINT PK_inbound_automation PRIMARY KEY CLUSTERED (id),                                                                                
        CONSTRAINT UQ_inbound_automation_file_row UNIQUE (file_hash, row_number_in_file)                                                            
    );                                                                                                                                              
END;]                                                                                                                                               
(Background on this error at: https://sqlalche.me/e/20/f405)                                                                                        
