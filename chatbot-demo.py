"""
Conversational AI Prototype — Intent-based dialogue management
Demonstrates: intent recognition, context handling, fallback logic
"""

class ConversationManager:
    def __init__(self):
        self.context = {}
        self.turn_count = 0

    def classify_intent(self, user_input: str) -> str:
        """Simple keyword-based intent classifier (demo)"""
        text = user_input.lower()
        if any(w in text for w in ["manufacture", "batch", "process"]):
            return "manufacturing"
        elif any(w in text for w in ["formulation", "excipient", "ingredient"]):
            return "formulation"
        elif any(w in text for w in ["regulation", "filing", "compliance"]):
            return "regulatory"
        return "out_of_scope"

    def handle(self, user_input: str) -> str:
        self.turn_count += 1
        intent = self.classify_intent(user_input)

        if intent == "out_of_scope":
            if self.turn_count >= 2:
                return "Let me connect you with a specialist. [Human handoff with context]"
            return "I can help with manufacturing, formulation, or regulatory questions. Which topic?"

        # Simulate RAG retrieval
        self.context["last_intent"] = intent
        return f"[RAG] Retrieved relevant {intent} documents. Generating contextual response..."

# Demo
bot = ConversationManager()
print(bot.handle("What is the batch manufacturing process?"))
print(bot.handle("Tell me about excipient ratios"))
print(bot.handle("What's the weather today?"))
