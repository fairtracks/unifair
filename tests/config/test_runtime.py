# from unifair.engine import Engine, Runtime
#
#
# class MockTaskDecorator(TaskDecorator):
#     def __init__(self, task_function, persist=False):
#
#
#
# class MockFlowDecorator(FlowDecorator):
#     pass
#
#
# class MockEngine(Engine):
#     def __init__(self, my_engine_parameter=True, **kwargs):
#         self.my_engine_parameter = my_engine_parameter
#         super(self, **kwargs).__init__()
#
#     def _create_engine(self):
#         return super(self)._configure(
#             task_decorator=MockTaskDecorator,
#             flow_decorator=MockFlowDecorator,
#         )
#
#     @staticmethod
#     def task_decorator() -> Callable:
#         return
#
#     @staticmethod
#     def result_persisting_task_decorator(result_dir: str) -> Callable:
#         pass
#
#     @staticmethod
#     def flow_decorator() -> Callable:
#         pass
#
#     @staticmethod
#     def executable_task_decorator() -> Callable:
#         pass
#
#
# def test_runtime_interface():
#     runtime = Runtime()
#     engine = MockEngine()
#
#     assert runtime.execution_mode == 'flow'
#     assert runtime.flow_mode == 'flow'
