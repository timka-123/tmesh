class Subsystem:
    """MESh subsystems
    """
    id: int
    "Subsystem ID"

    title: str
    "Display subsystem name"

    url: str
    "Link to subsystem"

    mnemonic: str
    "Internal code for subsystem"

    description: str
    "Description for subsystem"

    is_mobile: bool = False
    "idk"

    sort_order: int
    "Weight for subsystem sorting"
    