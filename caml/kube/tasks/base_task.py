from abc import ABCMeta, abstractmethod


class BaseKubeTask(metaclass=ABCMeta):
    def __init__(self, config):
        self.config = config
        self.status = "pending"

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        The task logic
        """
        pass

    @abstractmethod
    def wait(self, *args, **kwargs):
        """
        The status logic - must be non-blocking polling
        """
        pass
