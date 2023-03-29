<h1>OCI Function Example to Invoke a Data Science Notebook</h1>
<h2>Introduction</h2>
This contains one OCI function to execute a sample Data Science notebook using OCI Data Science.

There are various properties parameterized;
  * noteBook the Python notebook URL to use, for example you can use the sample provided here to test https://raw.githubusercontent.com/tensorflow/docs/master/site/en/tutorials/customization/basics.ipynb
  * jobName provide the job name for the OCI Data Science job that will be launched
  * logGroupId the log group Ocid to be used.
  * projectId the OCI Data Science project Ocid - create a project to be used
  * compartmentId the compartment Ocid where the job will be created
  * outputFolder the output folder in OCI to write the results ie. oci://bucketName@namespace/objectFolderName


<h2>Permissions</h2>
Example permissions to test from functions and from OCI Data Integration.

Resource principal for testing from OCI Functions for example;
* allow any-user to manage data-science-family in compartment YOURCOMPARTMENT where ALL {request.principal.type='fnfunc'}	
* allow any-user to manage log-groups in compartment YOURCOMPARTMENT where ALL {request.principal.type='fnfunc'}	
* allow any-user to manage log-content in compartment YOURCOMPARTMENT where ALL {request.principal.type='fnfunc'}	

Resource principal for testing from Workspaces for example;
* allow any-user to manage data-science-family in compartment YOURCOMPARTMENT where ALL {request.principal.type='disworkspace',request.principal.id='ocid1.disworkspace.oc1.iad....'}	
* allow any-user to manage log-groups in compartment YOURCOMPARTMENT where ALL {request.principal.type='disworkspace',request.principal.id='ocid1.disworkspace.oc1.iad....'}	
* allow any-user to manage log-content in compartment YOURCOMPARTMENT where ALL {request.principal.type='disworkspace',request.principal.id='ocid1.disworkspace.oc1.iad....'}	




