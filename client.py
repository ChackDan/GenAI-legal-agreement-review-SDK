import requests
import base64

class LegalAnalyzerClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def parse_agreement(self, agreement_id, file_path, file_type):
        with open(file_path, "rb") as f:
            file_data = base64.b64encode(f.read()).decode("utf-8")
        payload = {
            "agreement_id": agreement_id,
            "file": file_data,
            "file_type": file_type
        }
        return requests.post(f"{self.base_url}/agreements/parse", json=payload).json()

    def map_clauses(self, agreement_id, clauses):
        payload = {
            "agreement_id": agreement_id,
            "clauses": clauses
        }
        return requests.post(f"{self.base_url}/clauses/map", json=payload).json()

    def search_similar_clauses(self, clauses, top_n=5):
        payload = {
            "clauses": clauses,
            "top_n": top_n
        }
        return requests.post(f"{self.base_url}/search/similar-clauses", json=payload).json()

    def analyze_with_llm(self, agreement_id, clauses, temperature=0.3, max_tokens=2048):
        payload = {
            "agreement_id": agreement_id,
            "clauses": clauses,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        return requests.post(f"{self.base_url}/llm/analyze", json=payload).json()

    def submit_feedback(self, agreement_id, feedbacks):
        payload = {
            "agreement_id": agreement_id,
            "feedbacks": feedbacks
        }
        return requests.post(f"{self.base_url}/feedback/submit", json=payload).json()

    def train_model(self, training_dataset_id, parameters=None):
        payload = {
            "training_dataset_id": training_dataset_id,
            "parameters": parameters or {}
        }
        return requests.post(f"{self.base_url}/model/train", json=payload).json()
