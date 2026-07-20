from abc import ABCMeta, abstractmethod


class BaseCommand(metaclass=ABCMeta):
    """This is the base class for a command."""

    @abstractmethod
    def execute(self):
        """Abstract method: child classes must implement it."""
        pass

    def __call__(self):
        """Calling the instance automatically calls execute()."""
        return self.execute()
