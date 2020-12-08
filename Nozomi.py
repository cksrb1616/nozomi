from pathlib import Path
from nozomi import api

# The tags that the posts retrieved must contain
positive_tags = ['asanagi', 'wallpaper']

# Gets all posts with the tags 'kimetsu_no_yaiba', 'wallpaper'
for post in api.get_posts(positive_tags):
    api.download_media(post, Path.cwd())