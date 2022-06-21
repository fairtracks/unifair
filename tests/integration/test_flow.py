from unifair.config.runtime import (runtime_flow_decorator,
                                    runtime_task_decorator)
from unifair.dataset.json import JsonDataset, JsonDatasetToTarFileSerializer
from unifair.engine import Runtime
from unifair.engine.prefect import PrefectEngine


def test_function_as_flow():
    prefect_engine = PrefectEngine(
        dataset_type_to_serializer={'JsonDataset': JsonDatasetToTarFileSerializer})
    runtime = Runtime()

    @runtime_task_decorator(runtime)
    def mock_task_1() -> JsonDataset:
        json_dataset = JsonDataset()
        json_dataset['obj_type'] = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'
        return json_dataset

    @runtime_task_decorator(runtime)
    def mock_task_2(json_data: JsonDataset) -> JsonDataset:
        for obj_type in json_data.values():
            for obj in obj_type:
                obj['a'] += 1
        return json_data

    # @runtime_flow_decorator(runtime)
    # def mock_flow_as_function():
    #     return mock_task_2(mock_task_1())

    @runtime_flow_decorator(runtime)
    def mock_flow_as_list():
        return [mock_task_1, mock_task_2]

    # flow = function_as_flow_decorator(mock_flow)
    runtime.set_engine(prefect_engine)
    runtime.set_execution_mode('flow')
    runtime.set_flow_mode('list')

    output_data = mock_flow_as_list()

    assert list(output_data.keys()) == ['obj_type']
    assert len(output_data['obj_type']) == 2
    assert output_data['obj_type'][0]['a'] == 2
    assert output_data['obj_type'][1]['a'] == 4
