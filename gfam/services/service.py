from gfam.model.DataModel import GeneData


def fetch_all_data():
    data = []
    fetched_data = GeneData.query.all()
    for one in fetched_data:
        temp = {}
        temp['id'] = one.id
        temp['gfam_id'] = one.gfam_id
        temp['name'] = one.name
        data.append(temp)
    return data


def fetch_by_gfamid(gfam_id):
    data = GeneData.query.filter_by(gfam_id=gfam_id).first()
    temp={}
    temp['id'] = data.id
    temp['gfam_id'] = data.gfam_id
    temp['name'] = data.name
    return temp


def fetch_by_id(id):
    data = GeneData.query.filter_by(id=id).first()
    temp={}
    temp['id'] = data.id
    temp['gfam_id'] = data.gfam_id
    temp['name'] = data.name
    return temp

