from pydantic import BaseModel


class BuildingFeatures(BaseModel):
    relative_compactness: float
    surface_area: float
    wall_area: float
    roof_area: float
    overall_height: float
    orientation: int
    glazing_area: float
    glazing_area_distribution: int