<h1>OCI Function Example to Invoke a Data Science Notebook</h1>
<h2>Introduction</h2>
This contains one OCI function to execute a sample Data Science notebook using OCI Data Science.

There are various properties parameterized for demonstration purposes, more could be done such as shape and subnet, but for a publicly available ipynb this is all that is needed;
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

<h2>Function Deployment</h2>

Follow the regular function deployment pattern. I will not go through this here, there are tutorials on Functions here;

[https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartguidestop.htm] (OCI Functions Quickstart)

<h2>Sample Execution</h2>

```
echo '{"jobName":"My Job", "logGroupId":"ocid1.loggroup.oc1.iad....", "compartmentId":"ocid1.compartment.oc1.....", "projectId":"ocid1.datascienceproject.oc1.iad.....",  "noteBook":"https://raw.githubusercontent.com/tensorflow/docs/master/site/en/tutorials/customization/basics.ipynb", "outputFolder":"oci://bucket@namespace/helloworld"}' | fn invoke yourapp notebook
```


<h2>Orchestrating from OCI Data Integration</h2>

See [https://blogs.oracle.com/dataintegration/post/oci-rest-task-collection-for-oci-data-integration] (Invoking Data Science via REST Tasks)

