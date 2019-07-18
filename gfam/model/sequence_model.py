class SequencesModel(object):
    version = None
    sequence_id = None
    sequence_name = None
    sequence = None

    def __init__(self, sequence_id, sequence_name, sequence, version):
        self.sequence = sequence
        self.sequence_id = sequence_id
        self.version = version
        self.sequence_name = sequence_name

    # def __dict__(self):
    #     return dict(
    #         sequence_id=self.sequence_id,
    #         sequence_name=self.sequence_name,
    #         sequence=self.sequence,
    #         version=self.version
    #     )


class Sequence:
    """A sample Sequence class"""

    def __init__(self, sequence_name, sequence, version):
        self.sequence_name = sequence_name
        self.sequence = sequence
        self.version = version



