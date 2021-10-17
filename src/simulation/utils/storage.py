import os
import enum


class SizeUnit(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


def convert_unit(size_in_bytes: int, unit: SizeUnit) -> float:
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == SizeUnit.KB:
        out = size_in_bytes / 1024
    elif unit == SizeUnit.MB:
        out = size_in_bytes / (1024 * 1024)
    elif unit == SizeUnit.GB:
        out = size_in_bytes / (1024 * 1024 * 1024)
    else:
        out = size_in_bytes
    return round(out, 2)


def get_file_size(file_name: str, size_type=SizeUnit.MB) -> float:
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return convert_unit(size, size_type)
