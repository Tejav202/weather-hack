"""
IBM watsonx Orchestrate MCP Backend Server
Climate Risk Assessment and Mitigation Planning
"""

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Climate Risk Assessment Server")


@mcp.tool()
def get_climate_risk(location: str) -> str:
    """
    Get climate risk assessment for a given location.
    
    Args:
        location: The name of the location to assess (e.g., 'Mumbai', 'Delhi')
    
    Returns:
        A string describing the climate risk for the location
    """
    # Mock data based on location
    location_lower = location.lower().strip()
    
    if location_lower == 'mumbai':
        return "High Flood Risk"
    elif location_lower == 'delhi':
        return "Severe Heatwave"
    else:
        return "Low Risk"


@mcp.tool()
def generate_mitigation_plan(risk_type: str) -> str:
    """
    Generate a mitigation plan based on the risk type.
    
    Args:
        risk_type: The type of climate risk (e.g., 'Flood', 'Heatwave', 'Low')
    
    Returns:
        A string with mitigation advice for the given risk type
    """
    risk_lower = risk_type.lower().strip()
    
    if 'flood' in risk_lower:
        return """Flood Mitigation Plan:
- Elevate inventory and critical equipment above potential flood levels
- Install flood barriers and water-resistant doors
- Ensure proper drainage systems are in place
- Create emergency evacuation procedures
- Maintain flood insurance coverage
- Store important documents in waterproof containers"""
    
    elif 'heatwave' in risk_lower or 'heat' in risk_lower:
        return """Heatwave Mitigation Plan:
- Install cooling systems and ensure proper ventilation
- Provide adequate hydration stations for personnel
- Schedule critical operations during cooler hours
- Implement heat stress monitoring protocols
- Ensure backup power for cooling systems
- Create shaded rest areas for workers"""
    
    elif 'low' in risk_lower:
        return """Standard Risk Management Plan:
- Maintain regular monitoring of weather conditions
- Keep emergency supplies stocked
- Review and update emergency procedures annually
- Ensure adequate insurance coverage
- Conduct periodic risk assessments"""
    
    else:
        return f"""General Mitigation Plan for {risk_type}:
- Conduct detailed risk assessment
- Develop specific emergency response procedures
- Train staff on safety protocols
- Maintain emergency supplies and equipment
- Establish communication channels for alerts
- Review and update plans regularly"""


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()