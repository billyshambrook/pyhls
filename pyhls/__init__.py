"""HTTP Live Streaming python library."""

__version__ = '0.1.0'


def create(master_playlist):
    """
    Create a HLS master playlist.

    Note:
        Best to not include any folder path to the filename, as can be chosen
        when writing the file out to disk.

    Args:
        master_playlist (str): Master playlist filename.

    Returns:
        :class:`pyhls.playlists.Master`: A `pyhls.playlists.Master` instance.

    Examples:
        >>> manifest = create('master.m3u8')
    """
    pass


def parse(master_playlist):
    """
    Parse a master playlist from file.

    Args:
        master_playlist (str): Master playlist filename.

    Returns:
        :class:`pyhls.playlists.Master`: A `pyhls.playlists.Master` instance.

    Examples:
        >>> manifest = parse('master.m3u8')
    """
    pass


def validate(master_playlist):
    """
    Validate a master playlist from file.

    Args:
        master_playlist (str): Master playlist filename.

    Returns:
        tuple: A list of errors and a list of warnings if any raised.

    Examples:
        >>> errors, warnings = validate('master.m3u8')
    """
    pass
