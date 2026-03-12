from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer("all-MiniLM-L6-v2")


def detect_allergy_risk(user_allergies, ingredients):
    allergy_texts = [str(allergy).lower() for allergy in user_allergies]
    ingredient_texts = [str(ingredient).lower() for ingredient in ingredients]

    if not allergy_texts or not ingredient_texts:
        return False

    allergy_embeddings = model.encode(allergy_texts, convert_to_tensor=True)
    ingredient_embeddings = model.encode(ingredient_texts, convert_to_tensor=True)
    similarity_scores = util.cos_sim(allergy_embeddings, ingredient_embeddings)

    return float(similarity_scores.max()) > 0.6
