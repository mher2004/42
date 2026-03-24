from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: List[int]) -> str:
        try:
            a = [int(i) for i in data]
        except ValueError:
            return "Error: not integer type value"
        else:
            return self.format_output(f"Processed {len(a)} numeric\
 values, sum={sum(a)}, avg={sum(a)/len(a)}")

    def validate(self, data: List[int]) -> bool:
        try:
            data = [int(i) for i in data]
        except ValueError:
            print("Validation: Error: not integer type value")
            return False
        else:
            print("Validation: Numeric data verified")
            return True


class TextProcessor(DataProcessor):
    def process(self, data: str) -> str:
        try:
            a = ""
            for i in data:
                a += str(i)
        except ValueError:
            return "Error: not str type value"
        else:
            return self.format_output(f"Processed text: {len(a)}\
 characters,{len(a.split(' '))} words")

    def validate(self, data: str) -> bool:
        try:
            a = ""
            for i in data:
                a += str(i)
        except ValueError:
            print("Validation: Error: not str type value")
            return False
        else:
            print("Validation: Text data verified")
            return True


class LogProcessor(DataProcessor):
    def validate(self, data: str) -> bool:
        try:
            if not sum([log in data for log in ("Error", "Info")]):
                raise ValueError
        except ValueError:
            print("Validation: Error: not Log type value")
            return False
        else:
            print("Validation: Log entry verified")
            return True

    def process(self, data: str) -> str:
        try:
            if not sum([log in data for log in ("ERROR", "INFO")]):
                raise ValueError
        except ValueError:
            return "Error: not Log type value"
        else:
            txt = ""
            if "Error" in data:
                txt += "[ALERT]"
            else:
                txt += "[INFO] "
            txt += f"{data.split(':')[0]} level detected:{data.split(':')[1]}"
            return txt


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    nums = [5, 7, 5, 11]
    num_proc = NumericProcessor()
    print(f"Processing data: {nums}")
    num_proc.validate(nums)
    print(num_proc.process(nums), "\n")

    print("Initializing Text Processor...")
    text = "Hello Everybody"
    txt_proc = TextProcessor()
    print(f"Processing data: {text}")
    txt_proc.validate(text)
    print(txt_proc.process(text), "\n")

    print("Initializing Log Processor...")
    log = "ERROR: Connection timeout"
    log_proc = LogProcessor()
    print(f"Processing data: {log}")
    log_proc.validate(log)
    print(log_proc.process(log), "\n")

    print("=== Polymorphic Processing Demo ===\n")
    processors = [num_proc, txt_proc, log_proc]
    data = [nums, text, log]
    for i in range(3):
        print(f"Result {i + 1}:", processors[i].process(data[i]))

    print("\nFoundation systems online. Nexus ready for advanced streams.")
