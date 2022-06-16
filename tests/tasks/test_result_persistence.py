import os.path
from tempfile import TemporaryDirectory

from unifair.data.json import JsonDataset, JsonDatasetToTarFileSerializer
from unifair.engine.prefect import result_persisting_task_decorator, get_executable_task_decorator


def mock_task() -> JsonDataset:
    json_dataset = JsonDataset()
    json_dataset['obj_type'] = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'
    return json_dataset


def test_result_persistence():
    result_type_to_serializer_map = {'JsonDataset': JsonDatasetToTarFileSerializer}

    with TemporaryDirectory() as tmp_dir:
        result_persisting = result_persisting_task_decorator(
            result_dir=tmp_dir, result_type_to_serializer_map=result_type_to_serializer_map)
        executable = get_executable_task_decorator()

        decorated_task = executable(result_persisting(mock_task))
        decorated_task()

        assert os.path.exists(os.path.join(tmp_dir, 'something.tar.gz'))
