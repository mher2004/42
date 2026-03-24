from abc import ABC, abstractmethod
from typing import Protocol, Any, Dict


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def __init__(self):
        self.inform = "Input validation and parsing"

    def process(self, data: Any) -> Dict:
        pass


class TransformStage:
    def __init__(self):
        self.inform = "Data transformation and enrichment"

    def process(self, data: Any) -> Dict:
        pass


class OutputStage:
    def __init__(self):
        self.inform = "Output formatting and delivery"

    def process(self, data: Any) -> str:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        if isinstance(stage, ProcessingStage):
            self.stages.append(stage)
            print(f"Stage {len(self.stages)}:", stage.inform)
        else:
            print("Error: not a Processing Stage")

    @abstractmethod
    def process(data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(data):
        return super().process()


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(data):
        return super().process()


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(data):
        return super().process()
