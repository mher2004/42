from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
                    self, data_batch: List[Any],
                    criteria: Optional[str] = None
                    ) -> List[Any]:
        if criteria is not None:
            return [i for i in data_batch if i == criteria]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"data": self.count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: Environmental Data")
        self.temp_count = 0
        self.avg = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")
        try:
            for i in data_batch:
                if ":" not in i:
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            for i in data_batch:
                if i.split(":")[0] == "temp":
                    self.avg = self.avg * self.temp_count
                    self.avg += float(i.split(":")[1])
                    self.temp_count += 1
                    self.avg /= self.temp_count
            self.count += len(data_batch)
            return f"Sensor analysis: {self.count}\
 readings processed, avg temp: {self.avg}°C"

    def filter_data(
                    self, data_batch: List[Any],
                    criteria: Optional[float] = None
                    ) -> List[Any]:
        try:
            for i in data_batch:
                if ":" not in i:
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            if criteria is not None and isinstance(criteria, float):
                return [
                    i for i in data_batch if float(i.split(":")[1]) > criteria]
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"readings processed": self.count, "avg temp": self.avg}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: Financial Data")
        self.flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: {data_batch}")
        try:
            for i in data_batch:
                if ":" not in i:
                    raise TypeError("Error: Not right data format")
                if i.split(":")[0] != "buy" and i.split(":")[0] != "sell":
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            for i in data_batch:
                if i.split(":")[0] == "buy":
                    self.flow += float(i.split(":")[1])
                else:
                    self.flow -= float(i.split(":")[1])
            self.count += len(data_batch)
            return f"Transaction analysis: {self.count}\
 operations, net flow: {self.flow:+g} units"

    def filter_data(
                    self, data_batch: List[Any],
                    criteria: Optional[float] = None
                    ) -> List[Any]:
        try:
            for i in data_batch:
                if ":" not in i:
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            if criteria is not None and (
                    criteria == "buy" or criteria == "sell"):
                return [
                    i for i in data_batch if i.split(":")[0] == criteria]
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"operations processed": self.count, "net flow": self.flow}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"Stream ID: {stream_id}, Type: System Events")
        self.errors = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: {data_batch}")
        try:
            for i in data_batch:
                if i not in ["login", "logout", "error"]:
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            for i in data_batch:
                if i == "error":
                    self.errors += 1
            self.count += len(data_batch)
            return f"Event analysis: {self.count}\
 events, {self.errors} errors detected"

    def filter_data(
                    self, data_batch: List[Any],
                    criteria: Optional[float] = None
                    ) -> List[Any]:
        try:
            for i in data_batch:
                if i not in ["login", "logout", "error"]:
                    raise TypeError("Error: Not right data format")
        except TypeError as error:
            print(error)
        else:
            if criteria is not None:
                return [i for i in data_batch if i == criteria]
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"events processed": self.count, "errors": self.errors}


class StreamProcessor:
    pass
