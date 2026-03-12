from .nlp_service import detect_allergy_risk


def generate_recommendations(user, menu_items, mood=None, time_of_day=None):
    recommended = []

    user_allergies = []
    if user.allergies:
        user_allergies = [a.strip().lower() for a in user.allergies.split(",")]

    for item in menu_items:
        ingredients = [i.strip().lower() for i in item.ingredients.split(",")]
        reasons = []

        score = 0
        if user_allergies:
            if detect_allergy_risk(user_allergies, ingredients):
                continue
            score += 10
            reasons.append("Safe for your allergies")
        else:
            score += 10
            reasons.append("Safe for your allergies")

        if mood and mood.lower() in (item.mood_tags or "").lower():
            score += 5
            reasons.append("Matches your mood preference")

        if (
            user.diet_preferences
            and user.diet_preferences.lower() in (item.diet_tags or "").lower()
        ):
            score += 3
            reasons.append("Fits your dietary preference")

        if time_of_day == "morning" and "healthy" in (item.mood_tags or ""):
            score += 4
            reasons.append("Recommended for morning healthy meals")
        elif time_of_day == "afternoon" and "comfort" in (item.mood_tags or ""):
            score += 4
            reasons.append("Great comfort food for afternoon")
        elif time_of_day == "night" and "light" in (item.mood_tags or ""):
            score += 4
            reasons.append("Light food suitable for night")
        elif time_of_day == "late-night" and "cheat" in (item.mood_tags or ""):
            score += 4
            reasons.append("Popular late-night snack")

        recommended.append(
            {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "diet_tags": item.diet_tags,
                "mood_tags": item.mood_tags,
                "score": score,
                "reason": reasons,
            }
        )

    recommended.sort(key=lambda x: x["score"], reverse=True)

    return recommended
