"""Spare parts catalog for Brightwell Packaging"""

class SparePartsCatalog:
    """Internal service for spare-parts-catalog."""

    def status(self) -> str:
        return "ok"


if __name__ == "__main__":
    print(SparePartsCatalog().status())
