# from unifair.engine import Engine
#
#
# class MockTaskDecorator(TaskDecorator):
#     def __init__(self, task_function, serializer=None):
#         self._task_function = task_function
#         self._serializer = serializer
#
#     def __call__(self, *args, **kwargs):
#         self._task_function(*args, **kwargs)
#
#
# class MockListFlowDecorator(ListFlowDecorator):
#     def __init__(self, task_list):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
#
# class MockFunctionFlowDecorator(FunctionFlowDecorator):
#     def __init__(self, flow_function):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
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
