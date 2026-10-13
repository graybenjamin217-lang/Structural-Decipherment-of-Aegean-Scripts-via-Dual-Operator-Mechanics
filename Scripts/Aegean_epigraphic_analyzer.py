import numpy as np
from collections import defaultdict, Counter
import math

class EpigraphicScriptAnalyzer:
    def __init__(self, corpus_tokens: list[str]):
        """
        corpus_tokens: List of transcribed words/sign-groups 
                       e.g., ['PA-I-TO', 'KU-RO', 'PA-I-TO-DE']
        """
        self.corpus = corpus_tokens
        self.alphabet = sorted(list(set(''.join(corpus_tokens))))
        self.sign_to_idx = {sign: i for i, sign in enumerate(self.alphabet)}
        self.idx_to_sign = {i: sign for i, sign in enumerate(self.alphabet)}
        self.vocab_size = len(self.alphabet)
        
    def build_transition_matrix(self) -> np.ndarray:
        """Computes bigram transition probabilities P(Sign_j | Sign_i)."""
        transition_counts = np.zeros((self.vocab_size, self.vocab_size), dtype=np.float64)
        
        for token in self.corpus:
            signs = token.split('-') if '-' in token else list(token)
            for i in range(len(signs) - 1):
                if signs[i] in self.sign_to_idx and signs[i+1] in self.sign_to_idx:
                    u = self.sign_to_idx[signs[i]]
                    v = self.sign_to_idx[signs[i+1]]
                    transition_counts[u, v] += 1.0
                    
        row_sums = transition_counts.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        return transition_counts / row_sums

    def compute_positional_entropy(self) -> dict[str, float]:
        """Calculates forward conditional entropy to detect suffix/prefix boundaries."""
        transition_matrix = self.build_transition_matrix()
        sign_entropy = {}
        
        for i, sign in enumerate(self.alphabet):
            probs = transition_matrix[i]
            probs = probs[probs > 0]
            entropy = -np.sum(probs * np.log2(probs)) if len(probs) > 0 else 0.0
            sign_entropy[sign] = entropy
            
        return sign_entropy
