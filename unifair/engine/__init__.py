from abc import ABC, abstractmethod
from typing import Callable


class Engine(ABC):
    @staticmethod
    @abstractmethod
    def task_decorator() -> Callable:
        pass

    @staticmethod
    @abstractmethod
    def result_persisting_task_decorator(result_dir: str) -> Callable:
        pass

    @staticmethod
    @abstractmethod
    def flow_decorator() -> Callable:
        pass

    @staticmethod
    @abstractmethod
    def executable_task_decorator() -> Callable:
        pass
