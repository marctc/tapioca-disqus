from .applications import APPLICATIONS_MAPPING
from .blacklists import BLACKLISTS_MAPPING
from .category import CATEGORY_MAPPING
from .exports import EXPORTS_MAPPING
from .forums import FORUMS_MAPPING
from .imports import IMPORTS_MAPPING
from .posts import POSTS_MAPPING
from .threads import THREADS_MAPPING
from .topics import TOPICS_MAPPING
from .trends import TRENDS_MAPPING
from .users import USERS_MAPPING
from .whitelists import WHITELISTS_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(APPLICATIONS_MAPPING)
RESOURCE_MAPPING.update(BLACKLISTS_MAPPING)
RESOURCE_MAPPING.update(CATEGORY_MAPPING)
RESOURCE_MAPPING.update(EXPORTS_MAPPING)
RESOURCE_MAPPING.update(FORUMS_MAPPING)
RESOURCE_MAPPING.update(IMPORTS_MAPPING)
RESOURCE_MAPPING.update(POSTS_MAPPING)
RESOURCE_MAPPING.update(THREADS_MAPPING)
RESOURCE_MAPPING.update(TOPICS_MAPPING)
RESOURCE_MAPPING.update(TRENDS_MAPPING)
RESOURCE_MAPPING.update(USERS_MAPPING)
RESOURCE_MAPPING.update(WHITELISTS_MAPPING)

