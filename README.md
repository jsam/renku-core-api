# renku core api


### Example of create data command lifecycle.
```
cmd = renku.Command(create_dataset)
   .set_project(project)
   .set_lock(CREATE_DATASET_LOCK)# defined by lock template, template defines which resources we lock
   .set_prehooks([track_uncommited_files])
   .set_log([renku.NewCommandLog()])
   .set_posthooks([persist_project_metadata, persist_graph_triple])
   .build()  # this operations ensure that .execute() can be successfully invoked

result = cmd.execute()
print(result.log)  # ResultObject() returned from each command
```

### Example of project lifecycle:
```
project = renku.Project('my-project-path')  # or renku.Project('git://github.com/jsam/myproject')
project.set_datasets_handlers([DefaultDatasetHandler, S3DatasetHandler, GCSDatasetHandler])
project.set_workflow_handlers([DefaultWorkflowHandler, CWLHandler, BPMNHandler])
project.set_graph_handlers([DefaultGraphHandler, CustomWriteToNeo4JHandler])
project.set_persistance([GitHandler, ExportToS3])
project.build()  # assembles all specified handlers into passable project context

```

### Example of users usage of API
```
project = Project('my-project-path')

# The following operation will provide all default implementations for each lifecycle state.
cmd = project.dataset.create('mydataset', options={})  
result = cmd.execute()

print(result.log)
```

### Example how user can customize and integrate with renku command:
```
custom_cmd = project\
   .dataset.create('mydataset', options={})\
   .add_posthooks([download_files_from_s3, my_add_files_to_dataset])
   .build()

result = custom_cmd.execute()
print(result.log)  # This will show results from both commands as well as the intermediary result.


# Where hooks implementation is the following
def my_add_files_to_dataset(project, cmd):
   """Custom post hook handler for renku command."""
   for f in cmd.log[-1]['files']:
       cmd = project.dataset.add_file(f, options={})
       cmd.log.append(cmd.execute())
```