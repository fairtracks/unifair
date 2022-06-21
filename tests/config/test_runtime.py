from unifair.engine import Engine, Runtime


class MockEngine(Engine):
    def get_supported_flow_modes():
        return ['task']


def test_runtime_interface():
    runtime = Runtime()
    engine = MockEngine()

    assert runtime.execution_mode == 'flow'
    assert runtime.flow_mode == 'flow'