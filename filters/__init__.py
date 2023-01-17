from .group_filters import IsGroup
from dispatcher import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)