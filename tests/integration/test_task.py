import os.path
from tempfile import TemporaryDirectory

import pytest

# from unifair.config.runtime import runtime_task_decorator
from unifair.dataset.json import JsonDataset, JsonDatasetToTarFileSerializer
from unifair.engine import Runtime, runtime_task_decorator
from unifair.engine.prefect import PrefectEngine


@pytest.fixture
def runtime():
    return Runtime()


@pytest.fixture
def mock_task(runtime):
    @runtime_task_decorator(runtime)
    def mock_task() -> JsonDataset:
        json_dataset = JsonDataset()
        json_dataset['obj_type'] = '[{"a": 1, "b": 2}, {"a": 3, "b": 4}]'
        return json_dataset

    return mock_task


@pytest.fixture
def all_engines():
    return [
        PrefectEngine(dataset_type_to_serializer={'JsonDataset': JsonDatasetToTarFileSerializer})
    ]


def test_task_execution_all_engines(runtime, mock_task, all_engines):
    for engine in all_engines:

        runtime.set_engine(engine)
        runtime.set_execution_mode('task')

        output_data = mock_task()

        assert list(output_data.keys()) == ['obj_type']
        assert len(output_data['obj_type']) == 2
        assert output_data['obj_type'][0] == {'a': 1, 'b': 2}
        assert output_data['obj_type'][1] == {'a': 3, 'b': 4}


def test_task_execution_with_result_persistence_all_engines(runtime, mock_task, all_engines):
    for engine in all_engines:
        with TemporaryDirectory() as tmp_dir:

            runtime.set_engine(engine)
            runtime.set_result_persistence(result_dir=tmp_dir)
            runtime.set_execution_mode('task')

            mock_task()

            assert len(os.listdir(tmp_dir)) == 1
            result_file_name = os.listdir(tmp_dir)[0]
            assert result_file_name.startswith('mock_task_')
            assert result_file_name.endswith('.tar.gz')
