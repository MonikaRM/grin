"""grin tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# Import your custom stream types here:
from tap_grin.streams import (
    grinStream,
    CampaignStream,
    Campaign_ConversionsStream,
    Campaign_DiscountStream,
    Campaign_OrdersStream,
    Campaign_PayablesStream,
    Campaign_Product_selection_itemsStream,
    Campaign_Product_selectionsStream,
    PartnershipsStream,
    ContentsStream,
    Content_statsStream,
    Media_library_contentStream,
    Affiliate_linksStream,
    Affiliate_page_viewsStream,
    ConversionsStream,
    Discount_code_groupsStream,
    Discount_codesStream,
    Product_collectionsStream,
    Product_option_valuesStream,
    Product_variantsStream,
    ProductsStream,
    OrdersStream,
    Product_selection_itemsStream,
    Contact_networksStream,
    ContactsStream,
    Contact_addressesStream,
    Campaign_tasksStream,
    Custom_propertiesStream,
    StagesStream,
    DepositsStream,
    Deposits_id_Stream,
    DomainsStream,
    Domains_id_Stream,
    TeamsStream,
    Teams_id_Stream,
)
# Compile a list of custom stream types here
# OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    CampaignStream,
    Campaign_ConversionsStream,
    Campaign_DiscountStream,
    Campaign_OrdersStream,
    Campaign_PayablesStream,
    Campaign_Product_selection_itemsStream,
    Campaign_Product_selectionsStream,
    PartnershipsStream,
    ContentsStream,
    Content_statsStream,
    Media_library_contentStream,
    Affiliate_linksStream,
    Affiliate_page_viewsStream,
    ConversionsStream,
    Discount_code_groupsStream,
    Discount_codesStream,
    Product_collectionsStream,
    Product_option_valuesStream,
    Product_variantsStream,
    ProductsStream,
    OrdersStream,
    Product_selection_itemsStream,
    Contact_networksStream,
    ContactsStream,
    Contact_addressesStream,
    Campaign_tasksStream,
    Custom_propertiesStream,
    StagesStream,
    DepositsStream,
    Deposits_id_Stream,
    DomainsStream,
    Domains_id_Stream,
    TeamsStream,
    Teams_id_Stream,

]


class Tapgrin(Tap):
    """grin tap class."""
    name = "tap-grin"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True
        ),
        th.Property(
            "start_date",
            th.DateTimeType
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
