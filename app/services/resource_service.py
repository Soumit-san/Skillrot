from app.resources.resource_registry import RESOURCE_REGISTRY

def fetch_resources(skill_name: str, level: str):
    key = skill_name.lower()
    level = level.lower()

    resources = RESOURCE_REGISTRY.get(key)

    if resources:
        return [
            r for r in resources
            if r["difficulty"] in ["beginner", level]
        ]

    # ✅ FALLBACK FOR UNKNOWN SKILLS
    return [
        {
            "title": "General learning guide",
            "url": "https://www.coursera.org",
            "type": "general"
        },
        {
            "title": "YouTube educational content",
            "url": "https://www.youtube.com",
            "type": "general"
        }
    ]
