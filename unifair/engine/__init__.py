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


class Runtime:
    def __init__(self):
        self._engine = None
        self.execution_mode = 'flow'
        self.flow_mode = 'list'
        self._result_dir = None

    def set_engine(self, engine: Engine):
        self._engine = engine

    def set_result_persistence(self, result_dir: str):
        assert result_dir
        self._result_dir = result_dir

    def get_task_decorators(self):
        task_decorators = []

        if self._result_dir:
            task_decorators.append(self._engine.result_persisting_task_decorator(self._result_dir))
        else:
            task_decorators.append(self._engine.task_decorator())

        if self._execution_mode == 'task':
            task_decorators.append(self._engine.executable_task_decorator())

        return task_decorators

    def set_execution_mode(self, mode='flow'):
        assert mode in ['task', 'flow']
        self._execution_mode = mode

    def get_flow_decorators(self):
        return [self._engine.flow_decorator()]

    def set_flow_mode(self, flow_mode):
        assert flow_mode in ['list', 'function']
        self._flow_mode = flow_mode


def runtime_task_decorator(runtime: Runtime):
    class RuntimeTaskDecorator:
        def __init__(self, _task_func: Callable, _runtime: Runtime = runtime):
            self._task_func = _task_func
            self._runtime = _runtime

        def __call__(self, input=None):
            decorated_func = self._task_func
            for decorator in self._runtime.get_task_decorators():
                decorated_func = decorator(decorated_func)

            if input:
                return decorated_func(input)
            else:
                return decorated_func()

    return RuntimeTaskDecorator


def runtime_flow_decorator(runtime: Runtime):
    class RuntimeFlowDecorator:
        def __init__(self, _flow_func: Callable, _runtime: Runtime = runtime):
            self._flow_func = _flow_func
            self._runtime = _runtime

        def __call__(self):
            decorated_func = self._flow_func
            for decorator in self._runtime.get_flow_decorators():
                decorated_func = decorator(decorated_func)
            return decorated_func()

    return RuntimeFlowDecorator
