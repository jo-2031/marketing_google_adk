from typing import List, Dict
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    """
    Schema for storing extracted product information from an image.

    Attributes:
        product (str): Name of the detected product (e.g., "Boo Headset").
        category (str): High-level product category (e.g., "Headphones").
        features (List[str]): List of key visual or functional features of the product.
        audience (List[str]): Target audience segments likely to buy the product.
        mood (str): Aesthetic or stylistic mood of the product (e.g., "Modern", "Luxury").
        keywords (List[str]): Semantic keywords extracted from the image or product description.
        short_description (str): Concise product description (1-2 sentences).
        long_description (str): Detailed product description suitable for e-commerce or marketing pages.
    """
    product: str = Field(..., description="Name of the detected product")
    category: str = Field(..., description="High-level product category")
    features: List[str] = Field(..., description="List of key visual or functional features")
    audience: List[str] = Field(..., description="Target audience segments for the product")
    mood: str = Field(..., description="Aesthetic or stylistic mood of the product")
    keywords: List[str] = Field(..., description="Semantic keywords from the image or product")
    short_description: str = Field(..., description="Concise short description for marketing")
    long_description: str = Field(..., description="Detailed long description for e-commerce")

