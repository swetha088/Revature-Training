**what is delta live table?**



It is a declarative ETL framework.

Stored files in Delta Lake format.

Built data pipelines with notebooks.

Manage re-run after failures.



**What is incremental loading?**



Load all files exactly at one place.

Reusable pattern.





**What is Auto Loader?**



It is a framework to allow incremental loading of files.

 

**How delta live table differ from delta table?**



Delta Table - It is a data storage format.

&nbsp;             supports ACID Transactions , schema evolution and it can be create and manage by manually using spark or sql.

&nbsp;             Syntax:



Delta Live Table - It is a data pipeline framework created by databricks.

&nbsp;                  Automates ETL pipeline and continuously process and update the data.





**What's the use of decorators in delta live table?**

Decorators used to convert functions into pipelines

Decorators are like badges telling DLT what each function is supposed to do.

Without them, DLT cannot organize or automate the pipeline.





Building a house = Building a DLT pipeline



Workers = Python functions



Badges = DLT decorators



Badges you give:



@dlt.table → This worker builds a room (creates a table)



@dlt.view → This worker draws the plan (creates a view)



@dlt.expect → This worker checks quality (validates data)



With badges, Databricks knows:



Who does what



What order to work in



How to check quality



When to update





**How to create catalog and schema and what's the use of it?**



“**A catalog is the top-level container in Unity Catalog used for organizing and securing data across workspaces**.

CREATE CATALOG CATALOG\_NAME;

USE CATALOG CATALOG\_NAME;



**A schema is a logical container inside a catalog that holds tables, views, and other data objects**

CREATE SCHEMA SCHEMA\_NAME;

USE SCHEMA SCHEMA\_NAME;





**What is Delta Live Table(DLT) Expectations?**



DLT uses expectations enforce data quality rules on incoming data 



Raw data --> Expectations-two types



Expectations pass-> keeps records--> continue processing



Expectation fails --> Warn-> keeps data--> continue processing

&nbsp;                     Drop-> remove unnecessary rows and process clean  data only

&nbsp;                     Fail Flow -> Stops entire pipeline .





**What is a View?**



A View in Databricks is a logical / virtual table.



It does not store data

It runs the query every time you read it

Stored only as metadata in the metastore



**In a Databricks Delta Live Tables pipeline, the left side shows Explorations, Transformations, and Utilities. What are these sections and what are they used for?**



Explorations → For testing and previewing data.

Transformations → For defining pipeline tables/views using DLT decorators.

Utilities → For helper functions and shared logic used by the pipeline.





**What is batch view?**



A Batch View is produced using batch processing, not real-time.



Processes full or incremental batches

Runs on a schedule (e.g., hourly/daily)

Stored as a physical table

Typical for ETL Silver/Gold layers



 **What is a Streaming View?**

A Streaming View is built using Spark Structured Streaming or DLT Streaming Tables.



Continuously updates

Processes data in micro-batches

Handles late/out-of-order events

Supports exactly-once processing





Type	Stores Data?	Updates	Use Case

View	❌ No	Every query	Lightweight logic

Materialized View	✔ Yes	Incremental	Dashboards

Batch View	✔ Yes	Scheduled batch	ETL Silver/Gold

Streaming View	✔ Yes	Real-time	IoT, logs, events



**What is Streaming Table?**



spark.readStream.format(...)

\##Streaming Table 

This represents the \*\*real-time processing layer\*\* in a streaming pipeline.



A streaming table:



\- Continuously reads new incoming data  

\- Processes it as soon as it arrives  

\- Forwards the processed data to downstream tables  

\- Acts as the “live engine” of your pipeline  





**What is materialized view? Why and where to use and how its differ from normal view?**



A materialized view stores the result of a query physically for fast performance, while a normal view is just a saved query that runs every time. Use materialized views for heavy, repeated analytical queries.



Normal View - CREATE VIEW v1 AS SELECT \* FROM table;

&nbsp;

Materialized View - CREATE MATERIALIZED VIEW mv1 AS SELECT \* FROM table;

REFRESH MATERIALIZED VIEW mv1;



What is declarative pipeline?



It is also known as Delta Live Tables. Modern way to build data pipelines using sql or py.



Workflow in db:



It is an orchestrated sequence of taske such as notebooks, scripts, sql queries that run automatically in defined order.

&nbsp;

It is a collection of tasks that run in sequence or parallel to automate your data pipeline or ml pipeline.





running multiple notebooks- manual execution(without workflow

with workflow - automated



without work flow: Retry one failure-manual

&nbsp;                  Logging - difficult

&nbsp;                   Passing parameters-hard

&nbsp;                   external cron

&nbsp;      



with workflow: Built-in schedule(scheduling)

&nbsp;               auto retry policies

&nbsp;                centralized logs

&nbsp;                 easy

&nbsp;                 monitoring- UI dashboards





**What is workflow in databricks?**

A Workflow is a collection of tasks that run in sequence or parallel to automate your data pipeline or ML pipeline.



**What Can a Workflow Contain?**

Databricks Notebook

Python Script

SQL Query

Delta Live Tables

JAR/Scala

MLflow Runs

dbt Tasks

Webhooks/REST API call

Data Quality Tasks







What is Databricks joB?



A Databricks Job is used to run notebooks automatically, on a schedule, with multiple tasks, without you manually running anything.

Alarm + Auto-run button



You set the alarm → Databricks wakes up and runs the notebook for you.









Simple Steps: Create a Databricks Job with 2 Tasks

🔹 Task 1 → Producer (sets the value)



Create a job



Add first task



Name it task\_1



Select the first notebook (with dbutils.jobs.taskValues.set)



Choose a cluster



Click Create task



Task 1 is done.



🔹 Task 2 → Consumer (reads the value)



Click + Add task



Name it task\_2



Select the second notebook (with dbutils.jobs.taskValues.get)



Set Depends on = task\_1



Choose cluster



Click Create task



▶️ Run the Job



Click Run now



Open the run



Go to task\_2 logs



You will see:

Count of rows in the table : <number>







**What is dbutils.jobs.taskValues.set?**



It is a command you put in Task 1’s notebook to store a value so that Task 2 can read it later.



Think of it as:



“Save this value so the next task can use it.”





What is Widget?



A widget in Databricks is an input control that allows users to pass dynamic values to a notebook without changing the code.









