from typing import List, Dict
from pydantic import BaseModel, Field

class SEOOutput(BaseModel):
    """
    Schema for storing SEO and advertising outputs for a product.

    Attributes:
        seo_keywords (List[str]): Recommended SEO keywords for the product.
        ad_copies (List[str]): List of ad copy variations suitable for digital campaigns.
        upsell_products (List[str]): Suggested complementary or upsell products to increase revenue.
    """
    seo_keywords: List[str] = Field(..., description="List of recommended SEO keywords")
    ad_copies: List[str] = Field(..., description="Suggested advertisement copy texts")
    upsell_products: List[str] = Field(..., description="Related or complementary products for upselling")
