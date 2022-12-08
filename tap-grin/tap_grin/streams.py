"""Stream type classes for tap-grin."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

#from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_grin.client import grinStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")

class CampaignStream(grinStream):
    """Define custom stream."""
    name = "Campaign"
    path = "/campaigns"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "campaigns.json"


class Campaign_ConversionsStream(grinStream):
    """Define custom stream."""
    name = "Conversions"
    path = "/campaigns/campaignId/conversions"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "campaign-conversions.json"

class Campaign_DiscountStream(grinStream):
    """Define custom stream."""
    name = "Discount_codes_campaign"
    path = "/campaigns/{campaignId}/discount-codes"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "discount_codes_campaign.json"

class Campaign_OrdersStream(grinStream):
    """Define custom stream."""
    name = "orders"
    path = "/campaigns/{campaignId}/orders"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "orders.json"

class Campaign_PayablesStream(grinStream):
    """Define custom stream."""
    name = "Payables"
    path = "/campaigns/{campaignId}/payables"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "payables.json"

class Campaign_Product_selection_itemsStream(grinStream):
    """Define custom stream."""
    name = "Product-selection-items"
    path = "/campaigns/{campaignId}/product-selection-items"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product_selection_items.json"

class Campaign_Product_selectionsStream(grinStream):
    """Define custom stream."""
    name = "Product-selections"
    path = "/campaigns/{campaignId}/product-selections"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product_selections.json"

class PartnershipsStream(grinStream):
    """Define custom stream."""
    name = "Partnerships"
    path = "/partnerships"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "partnerships.json"

class ContentsStream(grinStream):
    """Define custom stream."""
    name = "content"
    path = "/content"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contents.json"

class Content_statsStream(grinStream):
    """Define custom stream."""
    name = "Content_stats"
    path = "/content-stats"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contents-stats.json"

class Media_library_contentStream(grinStream):
    """Define custom stream."""
    name = "media-library-content"
    path = "/media-library-content/{contentId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "media-library-content.json"


class Affiliate_linksStream(grinStream):
    """Define custom stream."""
    name = "affiliate-links"
    path = "/affiliate-links"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "affiliate-links.json"

class Affiliate_page_viewsStream(grinStream):
    """Define custom stream."""
    name = "affiliate-page-views"
    path = "/affiliate-page-views"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "affiliate-page-views.json"

class ConversionsStream(grinStream):
    """Define custom stream."""
    name = "conversions"
    path = "/conversions"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "conversions.json"

class Discount_code_groupsStream(grinStream):
    """Define custom stream."""
    name = "discount-code-groups"
    path = "/discount-code-groups"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "discount-code-groups.json"

class Discount_codesStream(grinStream):
    """Define custom stream."""
    name = "discount-codes"
    path = "/discount-codes"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "discount-codes.json"

class Product_collectionsStream(grinStream):
    """Define custom stream."""
    name = "product-collections"
    path = "/product-collections"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product-collections.json"

class Product_option_valuesStream(grinStream):
    """Define custom stream."""
    name = "product-option-values"
    path = "/product-option-values"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product-option-values.json"

class Product_variantsStream(grinStream):
    """Define custom stream."""
    name = "product-variants"
    path = "/product-variants"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product-variants.json"

class ProductsStream(grinStream):
    """Define custom stream."""
    name = "products"
    path = "/products"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "products.json"

class OrdersStream(grinStream):
    """Define custom stream."""
    name = "orders"
    path = "/orders"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "orders.json"

class Product_selection_itemsStream(grinStream):
    """Define custom stream."""
    name = "product-selection-items"
    path = "/product-selection-items"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "product_selection_items.json"

class Contact_networksStream(grinStream):
    """Define custom stream."""
    name = "contact-networks"
    path = "/contact-networks"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contact-networks.json"

class ContactsStream(grinStream):
    """Define custom stream."""
    name = "contacts"
    path = "/contacts"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contacts.json"
class Contacts_id_Stream(grinStream):
    """Define custom stream."""
    name = "contacts_id"
    path = "/contacts/{contactId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contacts_id.json"

class Contact_addressesStream(grinStream):
    """Define custom stream."""
    name = "contact-addresses"
    path = "/contact-addresses/{addressId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "contact-addresses.json"

class Campaign_tasksStream(grinStream):
    """Define custom stream."""
    name = "campaign-tasks"
    path = "/campaign-tasks/{taskId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "Campaign-tasks.json"

class Custom_propertiesStream(grinStream):
    """Define custom stream."""
    name = "custom-properties"
    path = "/custom-properties/{propertyId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "custom-properties.json"


class StagesStream(grinStream):
    """Define custom stream."""
    name = "stages"
    path = "/stages/{stageId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "stages.json"


class DepositsStream(grinStream):
    """Define custom stream."""
    name = "deposits"
    path = "/deposits"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "deposits.json"

class Deposits_id_Stream(grinStream):
    """Define custom stream."""
    name = "deposits_id"
    path = "/deposits/{depositId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "deposits_id.json"

class Deposits_id_Stream(grinStream):
    """Define custom stream."""
    name = "deposits_id"
    path = "/deposits/{depositId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "deposits_id.json"

class Deposits_id_Stream(grinStream):
    """Define custom stream."""
    name = "deposits_id"
    path = "/deposits/{depositId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "deposits_id.json"

class DomainsStream(grinStream):
    """Define custom stream."""
    name = "domains"
    path = "/domains"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "domains.json"

class Domains_id_Stream(grinStream):
    """Define custom stream."""
    name = "domains_id"
    path = "/domains/{domainId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "domains_id.json"

class TeamsStream(grinStream):
    """Define custom stream."""
    name = "teams"
    path = "/teams"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "teams.json"

class Teams_id_Stream(grinStream):
    """Define custom stream."""
    name = "teams_id"
    path = "/teams/{teamId}"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "teams_id.json"










