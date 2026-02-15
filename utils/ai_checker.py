from openai import OpenAI
import os
from settings.project_setting import AI_API_KEY

class AIChecker:
    def __init__(self):
        self.client = self.client = OpenAI(api_key=AI_API_KEY)

    def check_localization(self, page_text, target_lang="Ukrainian"):
        prompt = f"""
        Ти — експерт з локалізації QA. Проаналізуй текст сторінки:
        ---
        {page_text[:3000]}
        ---
        Завдання: Знайди слова або фрази, які НЕ написані мовою {target_lang}.
        Ігноруй назви брендів (Wikipedia, Google).
        Якщо все вірно, напиши 'OK'. Якщо є помилки, перелічи їх коротко.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini", # найдешевша і швидка модель
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content