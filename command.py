
class CommandInterface(abc.Abc):

    def execute(self):
        pass


class CommandResult():
    """this can be used to persists locally, until user decides to commit ... based on this file we could determine which operations have been executed and potentially either save few, all or rollback"""
    def __init__(self, log):
        self._log = log

    def _clean():
        """Filter out un-wanted data content which we don't want to return to the client invoking the command."""
        pass

    @property
    def log(self):
        return self._clean(self._log)

class Command:

    def __init__(name, lock_template, lock_resources, default_persist=False):
        self.name = name
        self.lock_template = lock_template
        self.lock_resources = lock_resources
        self.default_persist = default_persist

        self.log = []
        self.migrations = []
        self.pre_hooks = []
        self.post_hooks = []

    def _render_lock():
        # take lock template and render them with resources
        pass

    def compose(funcs):
        pass

    def lock():
        # check if lock exists, if not create it .. it if exists we raise
        pass

    def set_pre_hooks(hooks: list):
        """Calculate git state,determine merge strategy, build graph, ... """
        pass

    def set_post_hooks(hooks: list):
        pass

    def set_migrations(migrations: list):
        """This is only for command level migrations."""
        pass

    def build():
        # TODO: all checks if command has been correctely assembled should occur here, 
        # if not, we raise
        pass

    def run():
        with self.lock():
            self.compose(self.migrations + self.pre_hooks)
            self.execute(log, *args, **kwargs)
            self.compose(self.post_hooks)

        return CommandResult(self.log)


class CreateDataset(Command):

    def __init__(self):
        self.command = Command('create-dataset', CREATE_DATASET_LOCK, {})
        self.command.set_pre_hooks([])
        self.command.set_migrations([default_dataset_migrations(),])
        self.command.set_post_hooks([])

    def execute(self):
        pass