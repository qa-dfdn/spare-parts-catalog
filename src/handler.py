"""Request handler for spare-parts-catalog."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "spare-parts-catalog"}
