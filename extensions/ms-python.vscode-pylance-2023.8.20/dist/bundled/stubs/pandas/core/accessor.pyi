from typing import Any

class DirNamesMixin:
    def __dir__(self): ...

class PandasDelegate: ...

def delegate_names(
    delegate: Any, accessors: Any, typ: str, overwrite: bool = ...
) -> Any: ...

class CachedAccessor:
    def __init__(self, name: str, accessor: Any) -> None: ...
    def __get__(self, obj: Any, cls: Any): ...

def register_dataframe_accessor(name: Any): ...
def register_series_accessor(name: Any): ...
def register_index_accessor(name: Any): ...
