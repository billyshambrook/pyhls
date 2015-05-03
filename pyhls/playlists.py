"""Representations of HTTP Live Streaming playlists."""


class Master(object):

    """
    Represents a HLS master playlist.

    Attributes:
        filename (str): Master playlist filename

    Examples:
        >>> master_playlist = Master('master.m3u8')
    """

    def __init__(self, filename):
        """
        Initialise object.

        Args:
            filename (str): Master playlist filename
        """
        pass

    def add_stream(self, media_filename, media_playlist_filename):
        """
        Add a media stream to the master playlist.

        Will create a media playlist for the media file provided and attach it
        to the master playlist.

        Args:
            media_filename (str): Media file to generate a media playlist from.
            media_playlist_filename (str): Generated media playlist filename.
        """
        pass

    def add_media_playlist(self, media_playlist_filename):
        """
        """
        pass

    @classmethod
    def validate(cls, filename):
        """
        Validate a master playlist from file.

        Args:
            master_playlist (str): Master playlist filename.

        Returns:
            tuple: A list of errors and a list of warnings if any raised.

        Examples:
            >>> errors, warnings = Master.validate('master.m3u8')
        """
        pass


class Media(object):

    """
    Represents a HLS media playlist.

    Attributes:
        filename (str): Media playlist filename

    Examples:
        >>> media_playlist = Media('media.m3u8')
    """

    def __init__(self, filename):
        """
        Initialise object.

        Args:
            filename (str): Media playlist filename
        """
        pass

    @classmethod
    def validate(cls, filename):
        """
        Validate a media playlist from file.

        Args:
            media_playlist (str): Media playlist filename.

        Returns:
            tuple: A list of errors and a list of warnings if any raised.

        Examples:
            >>> errors, warnings = Media.validate('media.m3u8')
        """
        pass
