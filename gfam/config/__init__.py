from gfam import gfam_api


gfam_api.config['DEBUG'] = True
gfam_api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gfam/sequences.db'


class SequenceConfig:
    filename = 'gfam/data.json'

