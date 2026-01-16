from app.services.resource_service import fetch_resources
from app.services.plan_service import generate_refresh_plan
from app.llm.prompt_builder import build_prompt
from app.llm.llm_client import call_llm

def generate_recommendation(skill, health, status):
    resources = fetch_resources(skill.name, skill.level)
    plan = generate_refresh_plan(status)

    prompt = build_prompt(skill.name, health, status, resources)
    llm_response = call_llm(prompt)

    if llm_response:
        try:
            content = llm_response["choices"][0]["message"]["content"]
            data = eval(content)
        except:
            data = None
    else:
        data = None

    if data:
      reason = data.get("reason")
      tips = data.get("tips")
      ranked_resources = data.get("ranked_resources")

    else:
     if status == "Stable":
        reason = "The skill is well-maintained with consistent recent practice."
        tips = [
            "Continue light periodic practice",
            "Occasionally revise fundamentals"
        ]

     elif status == "At-Risk":
        reason = "The skill shows early signs of decay due to reduced recent practice."
        tips = [
            "Increase practice frequency",
            "Revise key concepts",
            "Apply the skill in short exercises"
        ]

     else:  # Critical
        reason = "The skill has significantly decayed due to prolonged inactivity."
        tips = [
            "Restart with core fundamentals",
            "Practice daily with structured sessions",
            "Use guided learning resources"
        ]

     ranked_resources = resources


    return {
        "skill": skill.name,
        "health": health,
        "status": status,
        "reason": reason,
        "tips": tips,
        "resources": ranked_resources,
        "plan": plan
    }
