from ..models import Video

def read_tsv(path):
    """Given a file path to a tsv, return the header and data"""

    data = open(path).read()
    data = data.split("\n")
    data = [row.split("\t") for row in data]
    
    header = data[0]
    data = data[1:]
    
    return (header, data)


def get_video_data_mapping(video_info):
    """Given a set of video info return a dict of id -> data

    :param video_info: list - [genre, id, title, url, duration]
    """
    
    video_info_mapping = {}
    for info in video_info:
        video_info_mapping[info[1]] = info
        
    return video_info_mapping


def get_rating_data_mapping(annotation_data):
    """Given a set of annotations, return a dict of id-> ratings

    :param annotation_info: list - [id, genre, [anno1, anno2, ...]]
    """
    
    rating_data = {}
    for row in annotation_data:
        if len(row) < 3:
            break
        video_id = row[0]
        ratings = [int(rating) for rating in row[2].split(",")]
        
        if video_id in rating_data:
            rating_data[video_id].append(ratings)
        else:
            rating_data[video_id] = [ratings]
    return rating_data


def get_video_objects(video_mapping, rating_mapping):
    """Given both mappings for video info and ratings, create
       a list of video objects

    :param video_mapping: dict - {id: [genre, id, title, url, duration]}
    :param rating_mapping: dict - {id: [[ratings1], [ratings2]]}
    """
    
    videos = []
    for video_id, ratings in rating_data.items():
        video = Video(video_info_mapping[video_id], ratings)
        videos.append(video)

    return videos
