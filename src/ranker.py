import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestRegressor
import os

class SmartRecruitmentSystem:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = pd.read_csv(dataset_path)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self._train_suitability_model()

    def _train_suitability_model(self):
        # Feature Engineering: Combine text features
        self.df['combined_features'] = (
            self.df['skills'] + ' ' + 
            self.df['education'] + ' ' + 
            self.df['domain'] + ' ' + 
            self.df['previous_role']
        )
        
        # TF-IDF Vectorization
        tfidf_matrix = self.vectorizer.fit_transform(self.df['combined_features'])
        
        # Feature matrix combining text vector + numerical experience
        exp_feature = self.df[['experience_years']].values
        X = np.hstack((tfidf_matrix.toarray(), exp_feature))
        y = self.df['suitability_score'].values

        # Train Random Forest Regressor
        self.model.fit(X, y)

    def rank_candidates(self, job_description, top_n=5):
        """
        Ranks candidates based on TF-IDF cosine similarity + ML predicted suitability score
        """
        # Job description vector
        job_vec = self.vectorizer.transform([job_description])
        
        # Candidate text vectors
        cand_vecs = self.vectorizer.transform(self.df['combined_features'])
        
        # Calculate Cosine Similarity
        similarity_scores = cosine_similarity(job_vec, cand_vecs).flatten()
        
        # Create results dataframe
        results = self.df.copy()
        results['relevance_similarity'] = similarity_scores
        results['final_match_score'] = (
            (results['relevance_similarity'] * 0.6) + 
            (results['suitability_score'] * 0.4)
        ) * 100

        # Sort candidates by final match score
        ranked = results.sort_values(by='final_match_score', ascending=False)
        return ranked[['candidate_id', 'name', 'experience_years', 'skills', 'final_match_score']].head(top_n)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(os.path.dirname(current_dir), 'data', 'candidates.csv')
    
    system = SmartRecruitmentSystem(data_path)
    job_req = "Seeking Python Machine Learning Engineer with Scikit-Learn, SQL, and Data Analytics experience."
    
    print("\n--- JOB REQUIREMENTS ---")
    print(job_req)
    print("\n--- TOP RANKED CANDIDATES ---")
    top_candidates = system.rank_candidates(job_req)
    print(top_candidates.to_string(index=False))
