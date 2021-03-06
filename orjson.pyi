from typing import Union

def dumps(obj: Union[str, bytes, dict, list, tuple, int, float, None]) -> bytes: ...

def loads(obj: Union[bytes, str]) -> Union[dict, list, int, float, str]: ...

class JSONDecodeError(ValueError): ...
