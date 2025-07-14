import uuid
from datetime import datetime


def generate_id(entity_type: str, identifier: str) -> str:
    namespace = uuid.NAMESPACE_DNS
    name = f"{entity_type}:{identifier}:{datetime.now().isoformat()}"
    return f"{entity_type}-{uuid.uuid5(namespace, name)}"
