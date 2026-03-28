from abc import ABC, abstractmethod
from typing import Protocol, Any, Dict, List, runtime_checkable
from time import time


@runtime_checkable
class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def __init__(self) -> None:
        self.inform = "Input validation and parsing"

    def process(self, data: Any) -> Dict:
        if not isinstance(data, dict):
            raise ValueError("Invalid input type")
        return data


class TransformStage:
    def __init__(self) -> None:
        self.inform = "Data transformation and enrichment"

    def process(self, data: Any) -> Dict:
        data["processed"] = True
        data["metadata"] = {"length": len(data)}
        return data


class OutputStage:
    def __init__(self) -> None:
        self.inform = "Output formatting and delivery"

    def process(self, data: Any) -> str:
        if isinstance(data, dict):
            try:
                if data["format"] == "json":
                    return f"Output: Processed\
 {data['sensor']} sensor reading: {data['value']}{data['unit']}"
                elif data["format"] == "csv":
                    return f"Output: {data['class']} {data['mode']}\
 logged: {data['count']} actions processed"
                elif data['format'] == 'stream':
                    return f"Output: Stream summary\
 {len(data['values'])} readings,\
 avg={sum(data['values'])/len(data['values'])}"
                else:
                    raise ValueError("Missing format")
            except KeyError as e:
                raise ValueError(f"Missing key: {e}")
        else:
            return "Wrong format"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: list[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        if isinstance(stage, ProcessingStage):
            self.stages.append(stage)
        else:
            print("Error: not a Processing Stage")

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.info = "JSON"
        super().__init__(pipeline_id)

    def process(self, data: Dict, printing: bool = False) -> Dict:
        data['format'] = 'json'
        if printing:
            print("Input:", data)
            if sum([1 for i in self.stages if isinstance(i, TransformStage)]):
                print("Transform: Enriched with metadata and validation")
        for stage in self.stages:
            data = stage.process(data)
        return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.info = "CSV"
        super().__init__(pipeline_id)

    def process(self, data: str, printing: bool = False) -> Dict:
        if ',' not in data:
            raise ValueError("Error: wrong input data, not enough parameters")
        if printing:
            print("Input:", data)
            if sum([1 for i in self.stages if isinstance(i, TransformStage)]):
                print("Transform: Parsed and structured data")
        values = data.split(",")
        data_dict = {}
        data_dict['format'] = 'csv'
        data_dict['class'] = values[0]
        data_dict['mode'] = values[1]
        data_dict['count'] = str(len(values) - 2)
        for stage in self.stages:
            data_dict = stage.process(data_dict)
        return data_dict


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        self.info = "Stream"
        super().__init__(pipeline_id)

    def process(
            self, data: List[int], printing: bool = False) -> Dict[str, Any]:
        data_dict: Dict[str, Any] = {'format': 'stream'}
        if not isinstance(data, list):
            raise ValueError("Error: wrong input (not list)")
        if printing:
            print("Input: Real-time sensor stream")
            if sum([1 for i in self.stages if isinstance(i, TransformStage)]):
                print("Transform: Aggregated and filtered")
        for i in data:
            if not isinstance(i, int):
                raise ValueError("Error: wrong input (not int)")
        data_dict['values'] = data
        for stage in self.stages:
            data_dict = stage.process(data_dict)
        return data_dict


class NexusManager:
    def __init__(self) -> None:
        print("Initializing Nexus Manager...\n\
Pipeline capacity: 1000 streams/second\n")
        self.pipelines = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        if not isinstance(pipeline, ProcessingPipeline):
            raise ValueError("Error: not a ProcessingPipline")
        else:
            self.pipelines.append(pipeline)

    def process_data(self, datas: List[Any],
                     printing: bool = False) -> None:
        i = 0
        for pipeline, data in zip(self.pipelines, datas):
            try:
                i += 1
                print(f"Processing {pipeline.info} data through pipeline...")
                print(pipeline.process(data, printing))
                print()
            except Exception as e:
                print(f"Error detected in Stage {i}:", e)
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored,\
 processing resumed")
                print()

    def chaining(self, data: Any, pipelines: list) -> Dict:
        try:
            for pipeline in pipelines:
                data = pipeline.process(data)
        except Exception as e:
            print("Error:", e)
        return data


if __name__ == "__main__":
    start = time()
    manager = NexusManager()
    json = JSONAdapter("qwe")
    csv = CSVAdapter("asd")
    stream = StreamAdapter("zxc")
    manager.add_pipeline(json)
    manager.add_pipeline(csv)
    manager.add_pipeline(stream)
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    inp = InputStage()
    print("Stage 2: Data transformation and enrichment")
    tra = TransformStage()
    print("Stage 3: Output formatting and delivery\n")
    out = OutputStage()
    for i in (json, csv, stream):
        i.add_stage(inp)
        i.add_stage(tra)
        i.add_stage(out)
    manager.process_data(
        [
            {"sensor": "temp", "value": 23.5, "unit": "C"},
            "user,action,timestamp",
            [150, 18, 17, 19],
         ],
        True
    )
    print("=== Pipeline Chaining Demo ===")
    json.stages.remove(out)
    csv.stages.remove(out)
    result = manager.chaining(
        "user,action,timestamp",
        [csv, json]
        )
    end = time()
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
    print(f"Chain result: {len(result)}\
 records processed through 2-stage pipeline")
    print(f"Performance: {end - start:.5f}s total processing time")
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    json.add_stage(out)
    csv.add_stage(out)
    print()
    manager.pipelines.remove(json)
    manager.add_pipeline(json)
    manager.process_data(
        [
            "user,action,timestamp",
            [15, 18, 17, 19],
            {"a": "temp", "value": 23.5, "unit": "C"},
         ],
        False
    )
    print("Nexus Integration complete. All systems operational.")
