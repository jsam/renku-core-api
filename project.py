
class DatasetsCmdInvoker:

    def __init__(self):
        pass

    def create(self):
        return command.CreateDataset()


class WorkflowsCmdInvoker:

    def __init__():
        pass


class Project:

    def __init__(self, with_migrations=True):
        self.datasets = DatasetsCmdInvoker()
        self.workflows = WorkflowsCmdInvoker()
        
        self.migrations = DefaultProjectMigrations()

        if with_migrations:
            self.migrations.execute() # project level migrations

    @staticmethod
    def new(template_location):
        pass

    @staticmethod
    def from_filesystem(location):
        pass

    @staticmethod
    def from_remote(location):
        pass


    