from typing import List, Dict
from pydantic import BaseModel, Field


class MarketingOutput(BaseModel):
    """
    Schema for storing generated marketing content for a product.

    Attributes:
        taglines (Dict[str, List[str]]): Taglines categorized by tone/style (e.g., Professional, Energetic, Playful, Tech, Luxury).
        winner_tagline (str): The selected best tagline from all generated options.
        short_description (str): Refined short product description optimized for marketing.
        long_description (str): Refined long product description optimized for e-commerce or promotional use.
    """
    taglines: Dict[str, List[str]] = Field(..., description="Dictionary of taglines categorized by style")
    winner_tagline: str = Field(..., description="The selected best tagline")
    short_description: str = Field(..., description="Refined short description for marketing")
    long_description: str = Field(..., description="Refined long description for e-commerce or ads")