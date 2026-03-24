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
        self.stream_type = "Sensor"

    def process_batch(self, data_batch: List[Any]) -> str:
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
            self.count = len(data_batch)
            return f"{self.count} readings processed"

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
                    isinstance(criteria, float) or isinstance(criteria, int)):
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
        self.stream_type = "Transaction"

    def process_batch(self, data_batch: List[Any]) -> str:
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
            self.count = len(data_batch)
            return f"{self.count} operations"

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
        self.stream_type = "Event"

    def process_batch(self, data_batch: List[Any]) -> str:
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
            self.count = len(data_batch)
            return f"{self.count} events"

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
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        try:
            if isinstance(stream, DataStream):
                self.streams.append(stream)
            else:
                raise ValueError("Error: not a stream")
        except ValueError as error:
            print(error)

    def process_all(self, data_batches: List[List[Any]]) -> None:
        try:
            if len(data_batches) != len(self.streams):
                raise ValueError("Error: not right quantity of data batches")
        except ValueError as error:
            print(error)
        else:
            for stream, batch in zip(self.streams, data_batches):
                result = stream.process_batch(batch)
                print(f"- {stream.stream_type}: {result}")

    def filter(
            self,
            data_batches: List[List[Any]],
            criteria: List[Optional[Any]]
            ) -> None:
        print("Stream filtering active: High-priority data only")
        print("Filtered results: ", end="")
        try:
            if len(data_batches) != len(self.streams):
                raise ValueError("Error: not right quantity of data batches")
        except ValueError as error:
            print(error)
        else:
            criteria.extend(
                [None for i in range(len(data_batches) - len(criteria))]
                )
            for i in range(len(data_batches)):
                filtered = self.streams[i].filter_data(
                    data_batches[i], criteria[i]
                    )
                print(f"{len(filtered)} {self.streams[i].stream_type}\
 alerts", end=", ")
            print()


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    data = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"],
            ]

    print("Initializing Sensor Stream...")
    str1 = SensorStream("123")
    print(f"Processing sensor batch: {data[0]}")
    print(
        "Sensor analysis:",
        str1.process_batch(data[0]),
        f", avg temp: {str1.avg}°C",
        )

    print("\nInitializing Transaction Stream...")
    str2 = TransactionStream("258")
    print(f"Processing transaction batch: {data[1]}")
    print(
        "Transaction analysis:",
        str2.process_batch(data[1]),
        f", net flow: {str2.flow:+g} units",
        )

    print("\nInitializing Event Stream...")
    str3 = EventStream("789")
    print(f"Processing event batch: {data[2]}")
    print("Event analysis:",
          str3.process_batch(data[2]),
          f", {str3.errors} errors detected",
          )

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    manager = StreamProcessor()
    manager.add_stream(str1)
    manager.add_stream(str2)
    manager.add_stream(str3)

    manager.process_all(data)
    print()
    manager.filter(data, [30, "sell", "error"])
    print("\nAll streams processed successfully. Nexus throughput optimal.")
