import io
import json
import logging
from fdk import response
from ads.jobs import Job, DataScienceJob, NotebookRuntime
import oci
import ads

def handler(ctx, data: io.BytesIO=None):
  logging.getLogger().info("Inside Python Hello World function")
  body = json.loads(data.getvalue())
  noteBook = body.get("noteBook")
  jobName = body.get("jobName")
  logGroupId = body.get("logGroupId")
  projectId = body.get("projectId")
  compartmentId = body.get("compartmentId")
  outputFolder = body.get("outputFolder")

  if (noteBook == None or logGroupId == None or projectId == None or compartmentId == None or outputFolder == None):
      resp_data = {"status":"400", "info":"Required parameters have not been supplied - noteBook, logGroupId, projectId, compatmentId, outputFolder need to be supplied"}
      return response.Response(
            ctx, response_data=resp_data, headers={"Content-Type": "application/json"}
      )


  ads.set_auth(auth='resource_principal')


  job = (
    Job(name=jobName)
    .with_infrastructure(
        DataScienceJob()
        # Configure logging for getting the job run outputs.
        .with_log_group_id(logGroupId)
        # Log resource will be auto-generated if log ID is not specified.
        #.with_log_id("<log_ocid>")
        # If you are in an OCI data science notebook session,
        # the following configurations are not required.
        # Configurations from the notebook session will be used as defaults.
        .with_compartment_id(compartmentId)
        .with_project_id(projectId)
        #.with_subnet_id("<subnet_ocid>")
        .with_shape_name("VM.Standard.E3.Flex")
        # Shape config details are applicable only for the flexible shapes.
        .with_shape_config_details(memory_in_gbs=16, ocpus=1)
        # Minimum/Default block storage size is 50 (GB).
        .with_block_storage_size(50)
    )
    .with_runtime(
        NotebookRuntime()
        .with_notebook(
            path=noteBook,
            encoding='utf-8'
        )
        .with_service_conda("tensorflow28_p38_cpu_v1")
        .with_environment_variable(GREETINGS="Welcome to OCI Data Science")
        .with_exclude_tag(["ignore", "remove"])
        .with_output(outputFolder)
    )
  )

  try:
    # Create the job on OCI Data Science
    job.create()
    # Start a job run
    run = job.run()

    # Returns the job run id (id) and the job id (jobId).
    returnResponse = json.loads("{\"id\":\"" + run.id + "\", \"jobId\":\"" + job.id + "\"}")

    return response.Response(
        ctx, response_data=returnResponse, headers={"Content-Type": "application/json"}
    )
  except oci.exceptions.ServiceError as inst:
      return response.Response( ctx, response_data=inst, headers={"Content-Type": "application/json"})



